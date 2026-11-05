"""Builds Presentation/179.pptx on the organisers' MCAIT 2026 template.

Run from anywhere: python build_deck.py
Slide text and speaker notes live here, so Slide-Content.md is generated from the deck.
"""
import copy
import subprocess
import sys
from pathlib import Path

from lxml import etree
from PIL import Image
from pptx import Presentation
from pptx.chart.data import CategoryChartData
from pptx.dml.color import RGBColor
from pptx.enum.chart import XL_CHART_TYPE, XL_LABEL_POSITION, XL_LEGEND_POSITION
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Emu, Inches, Pt

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
TEMPLATE = ROOT / "organiser-materials" / "MCAIT_2026_Research_Presentation_TemplateVer2.pptx"
OUT = ROOT / "179.pptx"
ASSETS = HERE / "assets"
SCREENSHOT = Path(r"C:\Users\User\Documents\FYP DOCS\Arcana-v2\refdocs\evidence\p2-d1-17-live-q-cross-10-graph-and-path.png")
LOGO = Path(r"C:\Users\User\Documents\Coding\Hackathon\Genui\UTP Codefest Hackathon\02-submission\documentation\assets\utp-logo.png")

FONT = "Calibri"
NAVY = "071E44"
NAVY2 = "12356E"
GOLD = "DBAC48"
GOLD_TEXT = "8A6414"
GOLD_TINT = "FBF3DF"
CYAN = "1577B5"
CYAN_TINT = "E3F1FA"
TINT = "F1F4F9"
WHITE = "FFFFFF"
INK = "1B2A41"
MUTED = "566378"
RULE = "CBD3DF"
RED = "A32035"

X0, X1 = 0.55, 12.78
WIDTH = X1 - X0
TOP = 1.8
BOTTOM = 5.9


def rgb(h):
    return RGBColor.from_string(h)


def set_alt(shape, text):
    shape._element.xpath(".//p:cNvPr")[0].set("descr", text)


def fill_para(p, content, size, color, bold=False, italic=False, align=None):
    """content is a string or a list of (text, overrides) runs."""
    runs = [(content, {})] if isinstance(content, str) else content
    for item in runs:
        text, o = (item, {}) if isinstance(item, str) else item
        r = p.add_run()
        r.text = text
        f = r.font
        f.name = FONT
        f.size = Pt(o.get("size", size))
        f.bold = o.get("bold", bold)
        f.italic = o.get("italic", italic)
        f.color.rgb = rgb(o.get("color", color))
    if align:
        p.alignment = align


def text(slide, x, y, w, h, paras, size=15, color=INK, bold=False, italic=False, align=None,
         anchor=MSO_ANCHOR.TOP, after=0, bullet=False, name=None, line=None):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    if name:
        tb.name = name
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = anchor
    write_paras(tf, paras, size, color, bold, italic, align, after, bullet, line)
    return tb


def write_paras(tf, paras, size, color, bold, italic, align, after, bullet, line=None):
    paras = [paras] if isinstance(paras, str) else paras
    for i, content in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        fill_para(p, content, size, color, bold, italic, align)
        if after:
            p.space_after = Pt(after)
        if line:
            p.line_spacing = line
        if bullet:
            pPr = p._p.get_or_add_pPr()
            pPr.set("marL", str(Inches(0.2)))
            pPr.set("indent", str(-Inches(0.2)))
            bu = etree.SubElement(pPr, qn("a:buChar"))
            bu.set("char", "•")


def box(slide, x, y, w, h, paras=None, fill=TINT, line=None, size=14, color=INK, bold=False,
        align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, radius=0.08, shape=MSO_SHAPE.ROUNDED_RECTANGLE,
        margin=0.1, after=0, name=None):
    s = slide.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    if name:
        s.name = name
    if shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        s.adjustments[0] = min(radius / min(w, h), 0.5)
    s.shadow.inherit = False
    if fill:
        s.fill.solid()
        s.fill.fore_color.rgb = rgb(fill)
    else:
        s.fill.background()
    if line:
        s.line.color.rgb = rgb(line)
        s.line.width = Pt(1)
    else:
        s.line.fill.background()
    tf = s.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(margin)
    tf.margin_top = tf.margin_bottom = Inches(0.04)
    tf.vertical_anchor = anchor
    if paras is not None:
        write_paras(tf, paras, size, color, bold, False, align, after, False)
    return s


def arrow(slide, x1, y1, x2, y2, color=MUTED, width=1.5):
    c = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    c.line.color.rgb = rgb(color)
    c.line.width = Pt(width)
    ln = c.line._get_or_add_ln()
    tail = etree.SubElement(ln, qn("a:tailEnd"))
    tail.set("type", "triangle")
    return c


def line_(slide, x1, y1, x2, y2, color=MUTED, width=1.25):
    c = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    c.line.color.rgb = rgb(color)
    c.line.width = Pt(width)
    return c


def table(slide, x, y, w, rows, widths, size=14, row_h=0.36, header_fill=NAVY, styles=None, name="Table"):
    """rows[0] is the header. styles maps (row, col) or ('col', c) to dict(fill, color, bold)."""
    styles = styles or {}
    gs = slide.shapes.add_table(len(rows), len(rows[0]), Inches(x), Inches(y), Inches(w), Inches(row_h * len(rows)))
    gs.name = name
    t = gs.table
    tblPr = t._tbl.tblPr
    for a in ("firstRow", "bandRow"):
        tblPr.set(a, "0")
    sid = tblPr.find(qn("a:tableStyleId"))
    if sid is not None:
        sid.text = "{2D5ABB26-0587-4C30-8999-92F81FD0307C}"  # No Style, No Grid
    total = sum(widths)
    for i, cw in enumerate(widths):
        t.columns[i].width = Inches(w * cw / total)
    for r, row in enumerate(rows):
        t.rows[r].height = Inches(row_h)
        for c, val in enumerate(row):
            cell = t.cell(r, c)
            st = {}
            st.update(styles.get(("col", c), {}) if r else {})
            st.update(styles.get(("row", r), {}))
            st.update(styles.get((r, c), {}))
            cell.margin_left = cell.margin_right = Inches(0.1)
            cell.margin_top = cell.margin_bottom = Inches(0.03)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            tf = cell.text_frame
            tf.word_wrap = True
            head = r == 0
            fill_para(tf.paragraphs[0], val, size, WHITE if head else st.get("color", INK),
                      bold=True if head else st.get("bold", False))
            cell.fill.solid()
            cell.fill.fore_color.rgb = rgb(header_fill if head else st.get("fill", WHITE))
            tcPr = cell._tc.get_or_add_tcPr()
            ln = etree.Element(qn("a:lnB"), w="9525")
            sf = etree.SubElement(ln, qn("a:solidFill"))
            etree.SubElement(sf, qn("a:srgbClr"), val=RULE)
            tcPr.insert(0, ln)
    return gs


def bar_chart(slide, x, y, w, h, cats, series, colors, horizontal=False, maxv=None, fmt="0", alt="", gap=60, overlap=-5):
    cd = CategoryChartData()
    cd.categories = cats
    for n, vals in series:
        cd.add_series(n, vals)
    kind = XL_CHART_TYPE.BAR_CLUSTERED if horizontal else XL_CHART_TYPE.COLUMN_CLUSTERED
    gf = slide.shapes.add_chart(kind, Inches(x), Inches(y), Inches(w), Inches(h), cd)
    set_alt(gf, alt)
    ch = gf.chart
    ch.has_title = False
    ch.has_legend = True
    ch.legend.position = XL_LEGEND_POSITION.TOP
    ch.legend.include_in_layout = False
    ch.legend.font.size = Pt(13)
    ch.legend.font.name = FONT
    ch.legend.font.color.rgb = rgb(INK)
    ca, va = ch.category_axis, ch.value_axis
    ca.tick_labels.font.size = Pt(13)
    ca.tick_labels.font.name = FONT
    ca.tick_labels.font.color.rgb = rgb(INK)
    ca.format.line.color.rgb = rgb(RULE)
    ca.has_major_gridlines = False
    from pptx.enum.chart import XL_TICK_MARK
    ca.major_tick_mark = XL_TICK_MARK.NONE
    va.visible = False
    va.has_major_gridlines = False
    va.minimum_scale = 0
    if maxv:
        va.maximum_scale = maxv
    if horizontal:
        ca.reverse_order = True
    plot = ch.plots[0]
    plot.gap_width = gap
    plot.overlap = overlap
    plot.has_data_labels = True
    dl = plot.data_labels
    dl.show_value = True
    dl.number_format = fmt
    dl.number_format_is_linked = False
    dl.position = XL_LABEL_POSITION.OUTSIDE_END
    dl.font.size = Pt(13)
    dl.font.name = FONT
    dl.font.bold = True
    dl.font.color.rgb = rgb(INK)
    for s, col in zip(plot.series, colors):
        s.format.fill.solid()
        s.format.fill.fore_color.rgb = rgb(col)
        s.invert_if_negative = False
    return gf


class Deck:
    def __init__(self):
        self.prs = Presentation(str(TEMPLATE))
        self.blank = self.prs.slides[1].slide_layout
        self.bg = ASSETS / "content-bg.png"
        self.first_content_used = False
        self.n = 1

    def content(self, eyebrow, title, notes, tag=None):
        self.n += 1
        if not self.first_content_used:
            s = self.prs.slides[1]
            self.first_content_used = True
        else:
            s = self.prs.slides.add_slide(self.blank)
            pic = s.shapes.add_picture(str(self.bg), 0, 0, self.prs.slide_width, self.prs.slide_height)
            pic.name = "MCAIT background"
            set_alt(pic, "MCAIT 2026 conference header and footer")
        text(s, X0, 0.93, 9.5, 0.25, eyebrow.upper(), size=12, color=GOLD_TEXT, bold=True, name="Section label")
        text(s, X0, 1.13, WIDTH - (2.0 if tag else 0), 0.55, title, size=28, color=NAVY, bold=True, name="Title",
             anchor=MSO_ANCHOR.MIDDLE)
        if tag:
            fill, fg = (NAVY2, WHITE) if tag == "In the paper" else (CYAN, WHITE)
            box(s, X1 - 1.75, 1.2, 1.75, 0.38, tag, fill=fill, color=fg, size=13, bold=True, radius=0.19, name="Evidence tag")
        text(s, X1 - 0.6, 6.03, 0.6, 0.22, str(self.n), size=11, color=MUTED, align=PP_ALIGN.RIGHT, name="Slide number")
        s.notes_slide.notes_text_frame.text = notes
        return s


def foot(s, content):  # noqa: D103
    text(s, X0, 5.99, WIDTH - 0.8, 0.3, content, size=11, color=MUTED, name="Footnote")


def callout(s, y, h, content, size=16):
    return box(s, X0, y, WIDTH, h, content, fill=NAVY, color=WHITE, size=size, bold=True, align=PP_ALIGN.LEFT,
               margin=0.25, name="Key message")


def build():
    ASSETS.mkdir(exist_ok=True)
    d = Deck()
    prs = d.prs
    prs.core_properties.title = "Graph-Grounded Generative User Interfaces for Learning"
    prs.core_properties.author = "Fakhrul Azim Bin Ahmed Mardzukie"
    prs.core_properties.subject = "MCAIT 2026, paper 179"

    # Background images from the template itself, and the cropped product screenshot.
    tpl_s1, tpl_s2 = prs.slides[0], prs.slides[1]
    bg_pic = next(sh for sh in tpl_s2.shapes if sh.shape_type == 13)
    d.bg.write_bytes(bg_pic.image.blob)
    arch_pic = next(sh for sh in tpl_s1.shapes if sh.shape_type == 13)
    (ASSETS / "cover-bg.png").write_bytes(arch_pic.image.blob)
    shot = Image.open(SCREENSHOT).convert("RGB")
    k = shot.size[0] / 1440
    crop = shot.crop((int(300 * k), int(62 * k), int(1420 * k), int(712 * k)))
    crop.save(ASSETS / "arcana-practice.png")
    grid_shot = Image.open(SCREENSHOT.with_name("p2-d1-14-live-comparison-grid-after-fix.png")).convert("RGB")
    k = grid_shot.size[0] / 1440
    grid_shot.crop((int(322 * k), int(82 * k), int(895 * k), int(82 * k) + int(347 * k))).save(ASSETS / "arcana-grid.png")
    for fn in ("hookes", "titration", "orbit"):
        Image.open(Path(r"C:\Users\User\Documents\Coding\Hackathon\Genui\Synapse-V4\brag-output-2026-10-21-195546\ui-reference\target-v3-labs") / f"{fn}.png").convert("RGB").save(ASSETS / f"lab-{fn}.png")
    logo_path = ASSETS / "utp-logo.png"
    logo_path.write_bytes(LOGO.read_bytes())

    # ------------------------------------------------------------------ 1. Title
    by_name = {sh.name: sh for sh in tpl_s1.shapes}
    title_box = by_name["TextBox 5"]
    p = title_box.text_frame.paragraphs[0]
    p.runs[0].text = "Graph-Grounded Generative User Interfaces for Learning: Retrieval Structure Determines Interface Expressiveness"
    p.runs[0].font.size = Pt(30)
    for extra in p.runs[1:]:
        extra._r.getparent().remove(extra._r)
    who = by_name["TextBox 6"]
    who.top = Inches(3.72)
    who.width = Inches(7.6)
    lines = ["Fakhrul Azim Bin Ahmed Mardzukie  ·  Universiti Teknologi PETRONAS, Malaysia",
             "Presenter: Fakhrul Azim  ·  Parallel Session 6 (Virtual), Track 2"]
    for para, line in zip(who.text_frame.paragraphs, lines):
        para.runs[0].text = line
        para.runs[0].font.size = Pt(16)
        for extra in para.runs[1:]:
            extra._r.getparent().remove(extra._r)
    chip = box(tpl_s1, 0.77, 5.05, 2.35, 1.1, fill=WHITE, radius=0.1, name="Logo backing")
    logo = tpl_s1.shapes.add_picture(str(logo_path), Inches(0.92), Inches(5.2), width=Inches(2.05))
    logo.name = "UTP logo"
    set_alt(logo, "Universiti Teknologi PETRONAS logo")
    tpl_s1.notes_slide.notes_text_frame.text = (
        "Good afternoon. I am Fakhrul Azim from Universiti Teknologi PETRONAS. My paper asks why learners working "
        "across their own documents still get a chat box, and what it would take to give them something better.")

    # ------------------------------------------------------------------ 2. Outline
    s = d.content("Overview", "The claim of this paper",
                  "Here is the claim in one sentence. The interface components a learning system can honestly offer are "
                  "bounded by what its retrieval layer can supply. I will go through the problem, the gap in the "
                  "literature, the approach, the formal bound and the evaluation. I will also show Arcana, which is this "
                  "paper put into practice, and what we measured on it after the paper was accepted.")
    box(s, X0, TOP + 0.05, WIDTH, 1.35,
        [[("The components an interface can honestly offer are bounded by what retrieval can supply.", {"size": 24})]],
        fill=NAVY, color=WHITE, bold=True, align=PP_ALIGN.LEFT, margin=0.35, name="Claim")
    items = [("1", "Problem", "Learners get prose"), ("2", "Gap", "What the literature leaves open"),
             ("3", "Approach", "Compose, do not write"), ("4", "Bound", "Retrieval limits the catalogue"),
             ("5", "Evaluation", "Protocol and results"), ("6", "Conclusion", "Limits and next steps")]
    w = (WIDTH - 5 * 0.15) / 6
    for i, (n, h, sub) in enumerate(items):
        x = X0 + i * (w + 0.15)
        box(s, x, 3.5, w, 2.25, fill=TINT, name=f"Outline {n}")
        box(s, x + 0.15, 3.68, 0.5, 0.5, n, fill=GOLD, color=NAVY, size=16, bold=True, shape=MSO_SHAPE.OVAL, margin=0)
        text(s, x + 0.15, 4.3, w - 0.3, 0.35, h, size=18, color=NAVY, bold=True)
        text(s, x + 0.15, 4.68, w - 0.3, 0.9, sub, size=14, color=MUTED)

    # ------------------------------------------------------------------ 3. Problem
    s = d.content("Background and problem", "Learners ask relational questions and get prose",
                  "When you study across many documents, the useful questions are about relationships: which sources "
                  "agree, where they conflict, what is missing. Current tools answer with a paragraph, which hands the "
                  "work of connecting the sources back to the learner. Interactive representations can work very well: "
                  "one meta-analysis found a pooled effect of 0.83 across twenty physics studies. But that material was "
                  "authored by people. Comparison grids and concept maps are absent from corpus tools for two reasons: "
                  "someone must build them per topic, and the retrieval layer has nothing structured to fill them with.")
    text(s, X0, TOP, 5.5, 0.3, "What a learner asks across their documents", size=15, color=NAVY, bold=True)
    for i, q in enumerate(["Which of these papers agree?", "Where do they conflict?", "What does the set not cover?"]):
        box(s, X0, TOP + 0.36 + i * 0.5, 5.5, 0.43, q, fill=TINT, size=15, align=PP_ALIGN.LEFT, margin=0.18)
    arrow(s, 6.2, 2.9, 7.0, 2.9, color=NAVY, width=2.25)
    text(s, 7.2, TOP, 5.58, 0.3, "What they get back", size=15, color=NAVY, bold=True)
    box(s, 7.2, TOP + 0.36, 5.58, 1.43, fill=TINT, name="Chat answer")
    for i, frac in enumerate([1.0, 0.94, 0.98, 0.9, 0.62]):
        box(s, 7.42, TOP + 0.53 + i * 0.235, (5.58 - 0.44) * frac, 0.11, fill=RULE, shape=MSO_SHAPE.RECTANGLE, name="Line of prose")
    y = 3.75
    h = 2.05
    box(s, X0, y, 3.55, h, fill=GOLD_TINT, name="Effect size")
    text(s, X0 + 0.2, y + 0.12, 3.2, 0.7, "d = 0.83", size=34, color=GOLD_TEXT, bold=True)
    text(s, X0 + 0.2, y + 0.82, 3.2, 1.2, "pooled effect of interactive representations, 20 physics studies, human-authored [5]", size=14)
    box(s, X0 + 3.7, y, 3.9, h, fill=TINT, name="Obstacles")
    text(s, X0 + 3.9, y + 0.12, 3.5, 0.4, "Why these views are missing", size=16, color=NAVY, bold=True)
    text(s, X0 + 3.9, y + 0.56, 3.5, 1.4, ["Someone must author each one per topic", "Retrieval has nothing structured to fill it"], size=15, bullet=True, after=5)
    box(s, X0 + 7.75, y, WIDTH - 7.75, h, "A flat answer asserts relations it never retrieved, and hands the synthesis back as more text to read [4].",
        fill=NAVY, color=WHITE, size=17, bold=True, align=PP_ALIGN.LEFT, margin=0.25, name="Key message")

    # ------------------------------------------------------------------ 4. Flat vs graph
    s = d.content("Background and problem", "Flat retrieval has no way to represent a relation",
                  "The cause sits in retrieval. Standard retrieval scores every chunk independently. It finds the passage "
                  "most similar to the question, but holds no record that two passages disagree or that one concept depends "
                  "on another. A larger embedding model does not fix this, because similarity measures how alike two texts "
                  "are, not how the things inside them connect. Graph retrieval changes what is stored. Entities and "
                  "relations are extracted, so a shared entity can bring passages from different documents together.")
    for y, lab in [(TOP, "Flat retrieval"), (3.62, "Graph-hybrid retrieval")]:
        box(s, X0, y, WIDTH, 1.72, fill=TINT, name=lab + " lane")
        text(s, X0 + 0.2, y + 0.55, 1.45, 0.6, lab, size=15, color=NAVY, bold=True)
    # flat lane
    box(s, 2.3, 2.34, 1.1, 0.62, "Query", fill=NAVY, color=WHITE, bold=True)
    for i, t_ in enumerate(["Passage, scored alone", "Passage, scored alone", "Passage, scored alone"]):
        box(s, 4.25, 1.92 + i * 0.5, 3.6, 0.42, t_, fill=WHITE, line=RULE, size=14)
        arrow(s, 3.4, 2.65, 4.25, 2.13 + i * 0.5)
        arrow(s, 7.85, 2.13 + i * 0.5, 8.75, 2.65)
    box(s, 8.75, 2.2, 3.85, 0.9, ["Cited prose", [("Relations asserted, never retrieved", {"size": 14, "bold": False})]],
        fill=WHITE, line=RULE, size=16, bold=True, color=NAVY)
    # graph lane
    box(s, 2.3, 4.17, 1.1, 0.62, "Query", fill=NAVY, color=WHITE, bold=True)
    nodes = {"Temperature": (5.05, 4.26, 1.45, NAVY, WHITE),
             "Collision frequency": (3.92, 3.75, 1.85, CYAN_TINT, INK),
             "Activation energy": (6.05, 3.75, 1.75, GOLD_TINT, INK),
             "Effective collisions": (3.92, 4.82, 1.85, GOLD_TINT, INK),
             "Reaction rate": (6.05, 4.82, 1.75, CYAN_TINT, INK)}
    for (a, b) in [((5.05, 4.47), (4.85, 4.17)), ((6.5, 4.47), (6.8, 4.17)), ((5.05, 4.47), (4.85, 4.82)), ((6.5, 4.47), (6.8, 4.82))]:
        line_(s, a[0], a[1], b[0], b[1])
    for label, (x, y, w_, f, c) in nodes.items():
        box(s, x, y, w_, 0.42, label, fill=f, color=c, size=13, bold=f == NAVY, line=RULE if f != NAVY else None, margin=0.03)
    arrow(s, 3.4, 4.48, 3.92, 4.48)
    arrow(s, 7.85, 4.48, 8.75, 4.48)
    box(s, 8.75, 4.03, 3.85, 0.9, ["Relational components", [("Grid, concept map, contradiction alert", {"size": 14, "bold": False})]],
        fill=WHITE, line=RULE, size=16, bold=True, color=NAVY)
    foot(s, "Blue: from one document. Gold: from another. A shared entity brings them into one retrieved set. "
            "Similarity encodes how alike texts are, not how entities connect [3].")

    # ------------------------------------------------------------------ 5. Related work
    s = d.content("Related work", "Four literatures, and the gap between them",
                  "Four bodies of work touch this problem. Graph retrieval is evaluated as retrieval, by answer quality. "
                  "Generative interface work is evaluated by preference, and preference is not correctness in instruction. "
                  "Educational systems keep a human between generation and learner, so they are safe but limited to what an "
                  "educator anticipated. And verification work relies on oracles and executable contracts, which a learning "
                  "presentation does not have. One recent paper argues that runtime generation is unsafe because it cannot "
                  "be verified at scale. No existing mechanism answers that, and that is the gap.")
    rows = [["Area", "What it establishes", "What it leaves open"],
            ["Retrieval [1-3, 14-17]", "Hybrid and graph retrieval, schema-free extraction", "Never treats retrieved structure as a substrate for presentation"],
            ["Generative UI [6, 18-20]", "Feasible, preferred to markdown, protocols for typed intent", "None asks whether the content is supported by a source"],
            ["Generated artifacts in education [7-9, 21, 22]", "Authoring-time generation with a human reviewer", "None generates for the learner at request time from evidence"],
            ["Verification and risk [10-13, 23-25]", "Adversarial checks for code; risks of generated instruction", "Oracles do not transfer; the safety objection stands unanswered"]]
    table(s, X0, TOP, WIDTH, rows, [3.0, 4.5, 4.7], size=14, row_h=0.56, styles={("col", 0): {"bold": True, "color": NAVY}, ("col", 2): {"fill": GOLD_TINT}})
    callout(s, 4.82, 0.98, "Gap: a learning interface composed at request time, from retrieved evidence, with a stated bound on what it may assert.")

    # ------------------------------------------------------------------ Market
    s = d.content("Related work", "Generative interfaces are reaching the market",
                  "This is no longer only a research question, because products are moving the same way. Gemini Notebook, formerly "
                  "NotebookLM, answers from your sources, and the learner picks an output such as a mind map or a data table. "
                  "ChatGPT's Intelligent UI chooses the format automatically. Gemini's dynamic view writes custom code for each "
                  "prompt. I am only reporting what the vendors publish, and I have not tested these systems. The paper makes no "
                  "claim about how they work inside. What I can say is that none of these public descriptions states a rule "
                  "linking a view to the retrieved structure that justifies it. Stating that rule is what this paper does.")
    rows = [["", "Gemini Notebook (formerly NotebookLM)", "ChatGPT Intelligent UI", "Gemini dynamic view", "This paper"],
            ["Described input", "the learner's uploaded sources and instructions", "the question", "the prompt, with tools such as web search", "evidence retrieved from the learner's corpus"],
            ["How the view arises", "the learner picks an output: mind map, data table, flashcards", "the model chooses the format automatically", "the model designs and codes it per prompt", "the model selects from a typed catalogue"],
            ["Stated rule linking a view to retrieved structure", "not stated", "not stated", "not stated", "a precondition on every component"]]
    st = {("col", 0): {"bold": True, "color": NAVY}, ("col", 4): {"fill": GOLD_TINT, "bold": True}}
    table(s, X0, TOP, WIDTH, rows, [2.2, 2.75, 2.35, 2.45, 2.5], size=14, row_h=0.72, styles=st)
    callout(s, 4.95, 0.85, "This compares public descriptions only. Not stated does not mean absent, and no product was tested.")
    foot(s, "Sources, checked 1 Nov 2026: Gemini Notebook Help; OpenAI release notes, 7 Oct 2026; Google Research blog, 18 Nov 2025.")

    # ------------------------------------------------------------------ 6. Contributions
    s = d.content("This paper", "Contributions",
                  "The paper makes four contributions. First, an architecture that couples graph-native hybrid retrieval to a "
                  "typed generative interface. Second, an interface composed at request time, held to the standard developed "
                  "for verified generated artifacts. Third, a formal statement that retrieval structure bounds interface "
                  "expressiveness. Fourth, an evaluation protocol committed before any run, with a pilot reported as found. "
                  "Arcana is what these ideas look like in practice. The claims belong to the paper, and Arcana is where they "
                  "can be run and checked.")
    cards = [("Architecture", "Graph-native hybrid retrieval coupled to a typed generative interface. Evidence fills components, not prose."),
             ("Verified interface layer", "Composed at request time. One schema, fail-closed validation, registry-only rendering, provenance on every claim."),
             ("A formal bound", "A definition, with a component-by-component mapping to study activities, that retrieval bounds expressiveness."),
             ("Committed evaluation", "Ablation harness, paired test and extraction audit fixed before any run, with a pilot reported as found.")]
    cw = (WIDTH - 0.25) / 2
    for i, (h, b) in enumerate(cards):
        x = X0 + (i % 2) * (cw + 0.25)
        y = TOP + (i // 2) * 1.42
        box(s, x, y, cw, 1.27, fill=TINT, name=h)
        box(s, x + 0.18, y + 0.32, 0.6, 0.6, str(i + 1), fill=NAVY, color=WHITE, size=18, bold=True, shape=MSO_SHAPE.OVAL, margin=0)
        text(s, x + 0.95, y + 0.12, cw - 1.1, 0.34, h, size=17, color=NAVY, bold=True)
        text(s, x + 0.95, y + 0.46, cw - 1.1, 0.78, b, size=14)
    box(s, X0, 4.72, WIDTH, 1.05, [[("Arcana ", {"bold": True, "color": NAVY}), ("is this paper in practice: a learning workspace where the ideas above run, and can be measured.", {})]],
        fill=GOLD_TINT, size=16, align=PP_ALIGN.LEFT, margin=0.25, name="Arcana note")

    # ------------------------------------------------------------------ Explainer film
    s = d.content("Approach", "The method in thirty seconds",
                  "Here is the whole method in thirty seconds. A learner asks a relational question and today gets a paragraph. "
                  "Instead, documents become entities and relations, so sources can connect. Three signals are fused by rank, so "
                  "evidence from different documents arrives together. The model then composes verified components, and writes no "
                  "markup. A malformed block is rejected at the gate. And what retrieval can supply sets the limit: flat retrieval "
                  "can honestly fill three of these, and graph-hybrid retrieval can fill all six.")
    vw = 7.15
    vh = vw * 9 / 16
    vx = (13.333 - vw) / 2
    mv = s.shapes.add_movie(str(ASSETS / "arcana-explainer.mp4"), Inches(vx), Inches(TOP - 0.02), Inches(vw), Inches(vh),
                            poster_frame_image=str(ASSETS / "visual-compose.png"), mime_type="video/mp4")
    mv.name = "Explainer video"
    set_alt(mv, "Animated explainer: documents become a graph, three signals are fused, the model composes verified components, a malformed block is rejected, and retrieval bounds the catalogue")
    foot(s, "Click the video to play. An illustration of the method, using the worked example from the paper. Not captured output.")

    # ------------------------------------------------------------------ 7. Regimes
    s = d.content("Approach", "Three regimes for producing a learning interface",
                  "This table is the core of the approach. Authoring ahead is safe, but only covers what someone anticipated. "
                  "Emitting markup at runtime covers anything, but the field regards it as unverifiable at scale. We take a "
                  "third route. The model composes from a verified vocabulary, so we keep the coverage of runtime generation "
                  "and the accountability of authoring. The price is expressiveness: a question whose best answer is an "
                  "unimplemented view gets the closest available component.")
    rows = [["", "Authored ahead", "Markup emitted at runtime", "Composed at request time"],
            ["Coverage", "what was anticipated", "any question", "any question"],
            ["Produced by", "a person", "the model, as code", "the model, as typed selections"],
            ["Correctness rests on", "human review", "post-hoc verification", "retrieved evidence and schema"],
            ["Expressiveness", "fixed catalogue", "unbounded", "combinatorial over a vocabulary"],
            ["Failure mode", "no answer exists", "confident wrong artifact", "closest available component"]]
    table(s, X0, TOP, WIDTH, rows, [2.6, 2.7, 3.2, 3.7], size=15, row_h=0.5,
          styles={("col", 0): {"bold": True, "color": NAVY}, ("col", 3): {"fill": GOLD_TINT, "bold": True}, (0, 3): {}})
    foot(s, "Table I of the paper. Runtime markup: assessed as unverifiable at scale [10].")
    box(s, X0, 4.95, WIDTH, 0.82, "The components are fixed. What is generated per question is which components, and the evidence that fills them.",
        fill=NAVY, color=WHITE, size=16, bold=True, align=PP_ALIGN.LEFT, margin=0.25, name="Key message")

    # ------------------------------------------------------------------ 8. Architecture
    s = d.content("Methodology", "From document to rendered component",
                  "Here is the system design. A document is parsed, chunked and embedded. In the same pass, entities and "
                  "relations are extracted with no fixed ontology, because a learner's documents can come from any discipline. "
                  "At query time there are three signals: dense similarity, keyword matching and graph traversal. They are "
                  "fused by rank using reciprocal rank fusion, because their raw scores are not comparable. The model then "
                  "selects components and fills them from that evidence. Every request ends at this stage, so no agent can "
                  "reply to the learner directly, and everything passes validation first.")
    cols = [(X0, "Ingestion, one pass"), (X0 + 4.2, "Hybrid retrieval"), (X0 + 8.4, "Generative interface")]
    cw = 3.83
    for x, h in cols:
        box(s, x, TOP, cw, 3.3, fill=TINT, name=h)
        text(s, x + 0.15, TOP + 0.08, cw - 0.3, 0.3, h, size=15, color=NAVY, bold=True)
    ax = X0 + 0.15
    bw = (cw - 0.45) / 2
    box(s, ax, 2.25, cw - 0.3, 0.46, "Learner's documents", fill=NAVY, color=WHITE, bold=True)
    box(s, ax, 3.02, bw, 0.92, "Parse, chunk, embed", fill=WHITE, line=RULE)
    box(s, ax + bw + 0.15, 3.02, bw, 0.92, "Extract entities and relations", fill=WHITE, line=RULE, size=13)
    box(s, ax, 4.25, bw, 0.6, "Vector index", fill=CYAN_TINT, bold=True)
    box(s, ax + bw + 0.15, 4.25, bw, 0.6, "Knowledge graph", fill=CYAN_TINT, bold=True)
    for xx in (ax + bw / 2, ax + bw + 0.15 + bw / 2):
        arrow(s, xx, 2.71, xx, 3.02)
        arrow(s, xx, 3.94, xx, 4.25)
    bx = X0 + 4.35
    sig = ["Dense similarity", "Sparse keyword (BM25)", "Graph traversal, 1 hop"]
    for i, t_ in enumerate(sig):
        box(s, bx, 2.25 + i * 0.56, cw - 0.3, 0.46, t_, fill=WHITE, line=RULE)
    box(s, bx, 4.25, cw - 0.3, 0.6, "Reciprocal rank fusion", fill=CYAN_TINT, bold=True)
    arrow(s, bx + (cw - 0.3) / 2, 3.83, bx + (cw - 0.3) / 2, 4.25)
    arrow(s, X0 + cw, 3.45, X0 + 4.2 + 0.15, 3.45, color=NAVY, width=2)
    cx = X0 + 8.55
    stack = [("Task agents, one routing function", WHITE, INK, False), ("Typed component selection", WHITE, INK, False),
             ("Fail-closed validation", GOLD, NAVY, True), ("Registry-only rendering", NAVY, WHITE, True)]
    for i, (t_, f, c, b) in enumerate(stack):
        y = 2.25 + i * 0.67
        box(s, cx, y, cw - 0.3, 0.52, t_, fill=f, color=c, bold=b, line=RULE if f == WHITE else None)
        if i < 3:
            arrow(s, cx + (cw - 0.3) / 2, y + 0.52, cx + (cw - 0.3) / 2, y + 0.67)
    arrow(s, X0 + 4.2 + cw, 3.45, X0 + 8.55, 3.45, color=NAVY, width=2)
    box(s, X0, 5.2, WIDTH, 0.62, [[("RRF(d) = Σ", {"bold": True}), ("r∈R", {"size": 11, "bold": True}), ("  1 / (k + r(d)),  k = 60", {"bold": True}),
                                   ("     Fusing by rank, because cosine, keyword and traversal scores are not comparable [26].", {"size": 14})]],
        fill=GOLD_TINT, size=16, color=NAVY, align=PP_ALIGN.LEFT, margin=0.25, name="Formula")

    # ------------------------------------------------------------------ 9. Interface layer
    s = d.content("Methodology", "The model composes the interface. It does not write it.",
                  "This is what makes it defensible. The model outputs typed component selections, with payloads built from "
                  "retrieved evidence. Layout and interaction are not under its control. Each safeguard names the failure it "
                  "contains. One schema generates both sides of the wire, so a mismatch is a compile error. The validator runs "
                  "on the server and rejects on any violation. We fail closed on purpose: a visible error can be recovered "
                  "from, a confident wrong presentation cannot. The paper states the limits too. Malformed interfaces are "
                  "prevented, but one that misreads a source is still possible.", tag="In the paper")
    lw = 4.1
    for i, (h, b, f) in enumerate([("Fixed", "Components, layout, typography, interaction", TINT),
                                   ("Chosen per question", "Which components, in what order", TINT),
                                   ("From retrieved evidence", "Every payload that fills them", GOLD_TINT)]):
        y = TOP + i * 1.02
        box(s, X0, y, lw, 0.9, fill=f, name=h)
        text(s, X0 + 0.18, y + 0.1, lw - 0.3, 0.32, h, size=16, color=NAVY, bold=True)
        text(s, X0 + 0.18, y + 0.45, lw - 0.3, 0.4, b, size=14)
    rows = [["Safeguard", "Failure it contains"],
            ["One schema generates both sides of the wire", "producer and consumer drift"],
            ["Retrieval before synthesis", "assertions from outside retrieved material"],
            ["Per-claim checking [25]", "unsupported citations"],
            ["Server-side validation that fails closed", "malformed presentations"],
            ["Registry-only rendering", "unregistered presentations"]]
    table(s, X0 + lw + 0.25, TOP, WIDTH - lw - 0.25, rows, [4.3, 3.6], size=14, row_h=0.49, styles={("col", 0): {"bold": True, "color": NAVY}})
    box(s, X0, 4.9, WIDTH, 0.9,
        [[("Stated in the paper: ", {"bold": True, "color": RED}), ("claim checking fails open on a provider error, and a contradiction quote is not yet matched verbatim. "
          "Status: 24 of 24 components registered, 645 tests passing in CI.", {})]],
        fill=TINT, size=14, align=PP_ALIGN.LEFT, margin=0.25, name="Stated limits")

    # ------------------------------------------------------------------ Adaptive interface
    s = d.content("Methodology", "Adaptive interface: where expressiveness shows",
                  "This is where expressiveness becomes visible. The paper's claim is that the space of interfaces is combinatorial: an ordered choice of components from a vocabulary, "
                  "with payloads decided per question. So the interface adapts. A single-paper question gets an answer and sources. A comparison gets a dashboard. A connected path adds a concept map. "
                  "And the workspace reshapes with the task, including study. Nobody authored these layouts in advance.", tag="In the paper")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", "6", "-i", str(ASSETS / "video-adaptive.mp4"), "-frames:v", "1", str(ASSETS / "poster-video-adaptive.png")], check=True)
    mv = s.shapes.add_movie(str(ASSETS / "video-adaptive.mp4"), Inches(X0), Inches(TOP), Inches(7.15), Inches(7.15 * 9 / 16),
                            poster_frame_image=str(ASSETS / "poster-video-adaptive.png"), mime_type="video/mp4")
    mv.name = "Adaptive interface video"
    set_alt(mv, "The same components rearrange for a single-paper question, a comparison, a connected path and a study request")
    rx = X0 + 7.45
    rw = WIDTH - 7.45
    for i, (h, b, f) in enumerate([("Combinatorial", "An ordered selection of k from n components, with payload structure derived per query.", TINT),
                                   ("The workspace reshapes", "Surveying, revising, drafting and Socratic questioning need different components. Mode is inferred.", TINT),
                                   ("Bounded by retrieval", "Which layouts are honest depends on the evidence. Expressiveness is the bound's other face.", GOLD_TINT)]):
        y = TOP + i * 1.38
        box(s, rx, y, rw, 1.26, fill=f, name=h)
        text(s, rx + 0.18, y + 0.09, rw - 0.36, 0.32, h, size=16, color=NAVY, bold=True)
        text(s, rx + 0.18, y + 0.44, rw - 0.36, 0.8, b, size=14)
    foot(s, "Click to play. Section IV-A of the paper. Counts in the video are block combinations from one live run of 39 questions.")

    # ------------------------------------------------------------------ 10. Worked request
    s = d.content("Methodology", "A worked request from the paper",
                  "Here is the example from the paper. A learner revising chemistry asks why raising the temperature increases "
                  "reaction rate. Their notes attribute it to particles colliding more often. The textbook chapter attributes "
                  "it mainly to more collisions exceeding the activation energy. Both are real, and the difference in emphasis "
                  "is what a learner reproduces in an exam without noticing. The graph brings both passages into one retrieved "
                  "set. A language model then detects the disagreement. It is not read from a typed edge. The response composes "
                  "three blocks, none authored for this question. A biology question would get a comparison grid instead.", tag="In the paper")
    box(s, X0, TOP, WIDTH, 0.55, [[("Learner asks:  ", {"color": GOLD}), "Why does raising the temperature increase the rate of a reaction?"]],
        fill=NAVY, color=WHITE, size=17, bold=True, align=PP_ALIGN.LEFT, margin=0.25, name="Question")
    cw = (WIDTH - 0.4) / 3
    y0 = 2.5
    h0 = 3.35
    heads = ["Cited summary", "Contradiction alert", "Concept map"]
    for i, h in enumerate(heads):
        x = X0 + i * (cw + 0.2)
        box(s, x, y0, cw, h0, fill=TINT, name=h)
        text(s, x + 0.18, y0 + 0.1, cw - 0.36, 0.32, h, size=16, color=NAVY, bold=True)
    x = X0 + 0.18
    text(s, x, y0 + 0.5, cw - 0.36, 1.9,
         [["Higher temperature gives more frequent collisions ", ("[notes]", {"color": CYAN, "bold": True}),
           ", and a larger share of collisions above the activation energy ", ("[chapter]", {"color": GOLD_TEXT, "bold": True}), "."]], size=15)
    text(s, x, y0 + 2.45, cw - 0.36, 0.75, "Each claim carries a citation to its source.", size=13, color=MUTED)
    x = X0 + cw + 0.2 + 0.18
    box(s, x, y0 + 0.5, cw - 0.36, 0.98, ["Lecture notes", [("Particles collide more often", {"bold": False, "size": 14})]], fill=CYAN_TINT, size=14, bold=True, align=PP_ALIGN.LEFT)
    box(s, x, y0 + 1.56, cw - 0.36, 0.98, ["Textbook chapter", [("More collisions exceed the activation energy", {"bold": False, "size": 14})]], fill=GOLD_TINT, size=14, bold=True, align=PP_ALIGN.LEFT)
    text(s, x, y0 + 2.62, cw - 0.36, 0.65, "Each side shows its document and stance, side by side.", size=13, color=MUTED)
    x = X0 + 2 * (cw + 0.2) + 0.18
    cmw = cw - 0.36
    tx, ty = x + cmw / 2 - 0.65, y0 + 0.55
    pts = [("Collision frequency", x, y0 + 1.42), ("Activation energy threshold", x + cmw / 2 - 0.05, y0 + 1.42)]
    box(s, tx, ty, 1.3, 0.42, "Temperature", fill=NAVY, color=WHITE, size=13, bold=True, margin=0.02)
    for lab, px, py in pts:
        line_(s, tx + 0.65, ty + 0.42, px + cmw / 4, py)
        box(s, px, py, cmw / 2 + 0.05 - 0.1, 0.56, lab, fill=WHITE, line=RULE, size=12, margin=0.03)
    line_(s, x + cmw / 4, y0 + 1.98, x + cmw / 2, y0 + 2.28)
    line_(s, x + 3 * cmw / 4, y0 + 1.98, x + cmw / 2, y0 + 2.28)
    box(s, x + cmw / 2 - 1.05, y0 + 2.28, 2.1, 0.42, "Effective collisions", fill=WHITE, line=RULE, size=12, margin=0.03)
    text(s, x, y0 + 2.8, cmw, 0.45, "Concepts linked across the corpus.", size=13, color=MUTED)
    foot(s, "Section IV-B of the paper. An illustration of what is composed, not captured output.")

    # ------------------------------------------------------------------ 11. Bound
    s = d.content("Central claim", "Retrieval structure bounds interface expressiveness",
                  "This is the central idea. A component is a claim about the shape of an answer. A comparison grid claims that "
                  "documents line up on shared dimensions. A concept map claims that concepts stand in labelled relations. So we "
                  "define expressiveness as the set of components whose preconditions a retrieval layer can satisfy from "
                  "evidence alone. Flat retrieval can of course draw a grid. But to fill it, the model must supply a relation "
                  "retrieval never returned. A rich catalogue on flat retrieval is not richer. Its extra components are filled "
                  "by the model, in a more convincing package than prose.", tag="In the paper")
    box(s, X0, TOP, WIDTH, 0.6,
        [[("X(R) = { c ∈ C  |  P(c) satisfiable from E(R, q) }", {"bold": True, "size": 18}), ("        X(flat)  ⊂  X(graph-hybrid)", {"bold": True, "size": 18, "color": GOLD_TEXT})]],
        fill=GOLD_TINT, color=NAVY, align=PP_ALIGN.LEFT, margin=0.25, name="Formal definition")
    rows = [["Component", "Structural precondition", "Supplied by", "Study activity"],
            ["Cited summary", "ranked passages with sources", "flat retrieval", "reading, orientation"],
            ["Recall cards", "atomic facts with sources", "flat retrieval", "retrieval practice"],
            ["Comparison grid", "documents aligned on shared dimensions", "cross-document entity alignment", "comparison"],
            ["Contradiction alert", "claim pairs on one entity that disagree", "co-retrieval via the graph", "reconciling sources"],
            ["Concept map", "concept-to-concept relations", "graph traversal", "organising knowledge"]]
    st = {("col", 0): {"bold": True, "color": NAVY}}
    for r in (3, 4, 5):
        st[("row", r)] = {"fill": CYAN_TINT}
    table(s, X0, 2.52, WIDTH, rows, [2.3, 4.2, 3.3, 2.4], size=14, row_h=0.39, styles=st)
    callout(s, 5.0, 0.8, "The catalogue a generative learning interface can honestly offer is a function of the retrieval beneath it.", size=17)

    # ------------------------------------------------------------------ 12. Protocol and pilot
    s = d.content("Evaluation", "Committed protocol, and a pilot reported as found",
                  "The protocol was committed before any run: twenty questions, with signals switched off one at a time across "
                  "five arms. Extraction was interrupted by a provider quota, so the paper reports a pilot on four of sixteen "
                  "documents. The result was null. Hybrid and flat tied on eighteen of twenty questions. The reason is the "
                  "finding: traversal returned nothing on fifteen questions, because query entities needed an exact match to a "
                  "graph node. On those questions the hybrid simply was flat retrieval. So the pilot does not test the graph. "
                  "It shows that the ceiling on the graph signal is query entity resolution.", tag="In the paper")
    lw = 5.5
    box(s, X0, TOP, lw, 2.85, fill=TINT, name="Protocol")
    text(s, X0 + 0.2, TOP + 0.1, lw - 0.4, 0.3, "Protocol, fixed 9 June 2026", size=16, color=NAVY, bold=True)
    text(s, X0 + 0.2, TOP + 0.48, lw - 0.4, 2.3,
         ["20 questions: 12 cross-document, 4 single-document, 4 contradiction",
          "16 public papers, 1,570 chunks",
          "5 arms: dense, sparse, graph, flat, hybrid",
          "Metrics: distinct sources, latency",
          "Paired Wilcoxon, hybrid against flat"], size=15, bullet=True, after=4)
    rows = [["Arm", "Mean distinct sources", "Median latency (ms)"],
            ["Dense only", "2.50", "670"], ["Sparse only", "3.35", "208"], ["Graph only", "0.60", "2,500"],
            ["Flat (dense + sparse)", "3.15", "897"], ["Hybrid (all three)", "3.15", "900"]]
    table(s, X0 + lw + 0.25, TOP, WIDTH - lw - 0.25, rows, [3, 2.3, 2.1], size=14, row_h=0.47,
          styles={("row", 3): {"fill": GOLD_TINT}, ("row", 4): {"bold": True}, ("row", 5): {"bold": True}, ("col", 0): {"color": NAVY}})
    callout(s, 4.78, 1.02, [[("Null: tied on 18 of 20 questions (p = 1.0). Traversal returned nothing on 15 of 20. ", {}),
                             ("The pilot locates the ceiling in query entity resolution.", {"color": GOLD})]])
    foot(s, "Pilot index: 4 of 16 documents (796 nodes, 859 edges). Table V of the paper.")

    # ------------------------------------------------------------------ 13. VERA
    s = d.content("From paper to practice", "Where Arcana began: VERA AI",
                  "Before the results, a word on where this came from. Arcana grew out of VERA AI, an enterprise knowledge "
                  "assistant from my internship. VERA already had hybrid retrieval and a no-citation, no-answer policy. But "
                  "documents were separate silos, the layout was fixed, and the agents did not work together. Working on it "
                  "showed me the limit this paper formalises: a system with flat retrieval can cite its answers well, but it has "
                  "nothing structured to show how sources relate. This is a comparison of designs, not of results, because the "
                  "domains and corpora are different.")
    rows = [["", "VERA AI", "Arcana"],
            ["Knowledge", "Flat vector chunks, one silo per document", "Entities and relations across all documents"],
            ["Retrieval", "BM25 + vector, fused by RRF", "BM25 + vector + graph traversal, fused by RRF"],
            ["Agents", "Six fixed, independent agents", "Task agents, routed through one function"],
            ["Interface", "Static three-panel layout", "Typed components composed per question"],
            ["Domain", "Enterprise knowledge base", "Learners working across their own documents"]]
    table(s, X0, TOP, WIDTH, rows, [1.8, 5, 5.4], size=15, row_h=0.46, styles={("col", 0): {"bold": True, "color": NAVY}, ("col", 2): {"fill": GOLD_TINT}})
    callout(s, 4.78, 1.02, "VERA could cite its answers, but had nothing structured to show how sources relate. That limit is what this paper formalises.")
    foot(s, "A design comparison, not a benchmark: different domains and corpora.")

    # ------------------------------------------------------------------ 14. Practice
    s = d.content("From paper to practice", "Arcana: the paper in practice",
                  "This is Arcana on the sixteen retrieval papers. First, three questions with a real model. A relational question gets a "
                  "cited summary and a graph. A comparison gets a grid. A question the papers cannot answer gets a refusal. Nobody "
                  "designed these screens for these questions. Then the learning tools. Concept pages show the sentences behind each "
                  "link. A wrong quiz answer is corrected, and the graph recolours by mastery. And a lab appears only where a passage "
                  "states the formula.", tag="After the paper")
    pw = 7.15
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", "8", "-i", str(ASSETS / "arcana-demo.mp4"), "-frames:v", "1", str(ASSETS / "demo-poster.png")], check=True)
    mv = s.shapes.add_movie(str(ASSETS / "arcana-demo.mp4"), Inches(X0), Inches(TOP), Inches(pw), Inches(pw * 9 / 16),
                            poster_frame_image=str(ASSETS / "demo-poster.png"), mime_type="video/mp4")
    mv.name = "Arcana demo video"
    set_alt(mv, "Screen recording of Arcana: a relational question, a comparison, a refused question, concept pages, a quiz that recolours the graph, and a verified lab")
    foot(s, "Click to play. First three screens: real-model run. Learning tools: no model call. The lab's function is a test fixture, passed through the real verifier.")
    rx = X0 + pw + 0.3
    rw = WIDTH - pw - 0.3
    for i, (h, b) in enumerate([("Same corpus, different shapes", "A summary with a graph, a comparison grid, or a refusal, depending on the question."),
                                ("Grounded relations", "Each stated relation shows the sentence and page behind it."),
                                ("Beyond answers", "A quiz, mastery on the graph, and a lab verified on every slider setting.")]):
        y = TOP + i * 1.38
        box(s, rx, y, rw, 1.26, fill=TINT, name=h)
        text(s, rx + 0.18, y + 0.1, rw - 0.36, 0.32, h, size=17, color=NAVY, bold=True)
        text(s, rx + 0.18, y + 0.47, rw - 0.36, 0.75, b, size=15)

    # ------------------------------------------------------------------ Graph and grid
    s = d.content("From paper to practice", "What retrieval structure makes possible",
                  "Here is what that structure looks like. On the left is part of the real graph extracted from the sixteen papers, "
                  "showing the concepts found across the most papers. About one in nine concepts appears in two or more papers, and "
                  "those are the points where documents connect. You can also see an extraction weakness: LLM and LLMs are separate "
                  "nodes. On the right is part of a comparison grid filled from that structure. Each cell is a quote from that paper with "
                  "its page. Where a paper has nothing to say, the cell says so instead of inventing an answer.",
                  tag="After the paper")
    fw = 5.95
    fig = s.shapes.add_picture(str(ASSETS / "knowledge-graph.png"), Inches(X0), Inches(TOP), width=Inches(fw))
    fig.name = "Knowledge graph"
    set_alt(fig, "Network of the concepts found in the most papers in Arcana's knowledge graph")
    fig.line.color.rgb = rgb(RULE)
    fig.line.width = Pt(1)
    gx = X0 + fw + 0.3
    gridw = X1 - gx
    NOEV = {"color": MUTED, "fill": TINT}
    rows = [["Paper", "BM25", "Graph traversal"],
            ["RAG Survey", '"a sparse encoder (BM25) and a dense retriever" (page 9)', "No evidence in this paper"],
            ["RAG with Graphs", '"Methods like BM25 and TF-IDF primarily focus on lexical signals" (page 9)', '"GraphRAG employs graph traversal methods" (page 5)'],
            ["From Local to Global", "No evidence in this paper", "No evidence in this paper"]]
    table(s, gx, TOP, gridw, rows, [1.35, 2.4, 2.1], size=14, row_h=0.8, name="Comparison grid",
          styles={("col", 0): {"bold": True, "color": NAVY}, (1, 2): NOEV, (3, 1): NOEV, (3, 2): NOEV})
    text(s, X0, 5.52, fw, 0.3, "11,173 concepts, 13,972 edges, 11.6% of concepts in 2+ papers", size=14, color=NAVY, bold=True)
    text(s, gx, 5.52, gridw, 0.3, 'A real comparison grid: quote and page, or an honest gap', size=14, color=NAVY, bold=True)
    foot(s, "Real graph, 16 papers. Drawn: the most widely shared concepts. About a third of edges are stated in one sentence. Grid simplified from Arcana, quotes shortened.")

    # ------------------------------------------------------------------ Generated component
    s = d.content("From paper to practice", "Beyond the catalogue: generated, then verified",
                  "The paper names a cost: the catalogue is a ceiling. A question whose best answer is an interactive experiment gets the closest component. Our team's system, Synapse, explores the way past that ceiling for school science. "
                  "The model plans a lab over an audited kit, and a verifier runs it in a real browser before a student can see it. Arcana's formula labs use the same discipline. This is a different domain, so I do not compare results.", tag="After the paper")
    lv = (WIDTH - 0.4) / 3
    for i, (h, b, f, c) in enumerate([("Level 1: typed components", "Fixed, verified, filled from evidence", TINT, NAVY), ("Level 2: adaptive layout", "Arranged per question and task", TINT, NAVY),
                                      ("Level 3: generated component", "Written per question, shown only if verified", NAVY, WHITE)]):
        box(s, X0 + i * (lv + 0.2), TOP, lv, 0.85, [h, [(b, {"size": 14, "bold": False})]], fill=f, color=c, size=17, bold=True, align=PP_ALIGN.LEFT, margin=0.18, name=h)
    labs = [("hookes", "Hooke's law"), ("titration", "Acid-base titration"), ("orbit", "Newton's cannonball")]
    iw = 2.58
    for i, (fn, cap) in enumerate(labs):
        x = X0 + i * (iw + 0.12)
        pic = s.shapes.add_picture(str(ASSETS / f"lab-{fn}.png"), Inches(x), Inches(2.8), width=Inches(iw))
        pic.name = cap
        set_alt(pic, f"Interactive {cap} lab from Synapse")
        pic.line.color.rgb = rgb(RULE)
        pic.line.width = Pt(1)
        text(s, x, 4.38, iw, 0.26, cap, size=13, color=NAVY, bold=True)
    box(s, X0, 4.72, 3 * iw + 0.24, 1.1, [[("The trust path: ", {"bold": True, "color": NAVY}), "the model plans over an audited kit, a real browser moves every control, only the verifier can mint the deliverable, and it runs in a sandbox."]],
        fill=TINT, size=14, align=PP_ALIGN.LEFT, margin=0.18, name="Trust path")
    rx = X0 + 3 * iw + 0.5
    rw = X1 - rx
    for i, (n, l) in enumerate([("219 of 224", "planted defects refused, 0 of 30 false alarms"), ("20 of 20", "hostile attack shapes blocked"), ("13 of 14", "new questions built a lab, labelled model-checked")]):
        y = 2.8 + i * 1.03
        box(s, rx, y, rw, 0.96, fill=GOLD_TINT if i == 2 else TINT, name=n)
        text(s, rx + 0.15, y + 0.05, rw - 0.3, 0.45, n, size=22, color=NAVY, bold=True)
        text(s, rx + 0.15, y + 0.5, rw - 0.3, 0.42, l, size=12)
    foot(s, "Synapse, by Team EduNova (UTP), Form 4 and 5 science. Prototype screens. Planted sets written by the team. No teacher review or learner study yet.")

    # ------------------------------------------------------------------ 15. Retrieval
    s = d.content("New findings", "On the full corpus, a retrieval gain is not shown",
                  "Now the findings since the paper. We completed the study the paper called for: all sixteen papers, the "
                  "repaired entity matching, and a gold set of relevant passages. The graph signal now fires. On the original "
                  "harder, cross-document questions, the hybrid is ahead, but not significantly. On nineteen new questions, which "
                  "lean towards single papers, it falls behind. Pooled, the difference is essentially zero. So I do not claim a "
                  "retrieval gain. Not shown to help is not the same as shown not to help, but this corpus gives no support for "
                  "that claim. The metric here is nDCG, so please do not compare it with the pilot.", tag="After the paper")
    lw = 5.6
    bar_chart(s, X0, TOP - 0.05, lw, 3.15, ["Original 19", "New 19", "Pooled 38"],
              [("Flat", (0.169, 0.394, 0.281)), ("Hybrid", (0.208, 0.352, 0.280))], [RULE, NAVY], maxv=0.5, fmt="0.000",
              alt="nDCG at 10. Original 19 questions: flat 0.169, hybrid 0.208. New 19: flat 0.394, hybrid 0.352. Pooled 38: flat 0.281, hybrid 0.280.")
    rows = [["Question set", "Hybrid minus flat", "Better / tied / worse", "p"],
            ["Original 19, cross-document", "+0.039", "7 / 8 / 4", "0.15"],
            ["New 19, declared extension", "-0.042", "2 / 6 / 11", "0.068"],
            ["Pooled 38", "-0.001", "9 / 14 / 15", "0.69"]]
    table(s, X0 + lw + 0.25, TOP + 0.1, WIDTH - lw - 0.25, rows, [3.1, 1.5, 1.5, 0.7], size=14, row_h=0.57,
          styles={("row", 3): {"bold": True, "fill": GOLD_TINT}, ("col", 0): {"color": NAVY}})
    callout(s, 4.95, 0.87, "No pair reaches p < 0.05. Not shown to help is not the same as shown not to help.")
    foot(s, "nDCG@10 against gold passages, 16 papers, 1,570 passages, paired Wilcoxon. A different metric from the pilot. Not peer reviewed.")

    # ------------------------------------------------------------------ 16. Admission
    s = d.content("New findings", "The graph does extend the interface: 2 components against 5",
                  "Here is the other half of the argument. For each question, we counted which components had their preconditions "
                  "met by the evidence. Flat retrieval admits two. The hybrid layer realises all five. Please read this carefully. "
                  "That flat cannot admit the other three follows from how the preconditions are defined, so it is not a discovery. "
                  "What the measurement adds is how often the evidence exists: a connection graph on sixteen questions, and a "
                  "multi-hop path on only three, because every hop must be grounded in a stored sentence. And admitted does not "
                  "mean useful. The grid was admitted on every question, so it is not yet selective.", tag="After the paper")
    lw = 7.2
    bar_chart(s, X0, TOP - 0.05, lw, 4.15, ["Cited summary (proxy)", "Source list", "Graph view", "Comparison grid", "Concept map"],
              [("Flat", (20, 20, 0, 0, 0)), ("Hybrid", (20, 20, 16, 20, 3))], [RULE, NAVY], horizontal=True, maxv=24,
              alt="Questions admitted of 20. Flat: cited summary 20, source list 20, graph view 0, comparison grid 0, concept map 0. Hybrid: 20, 20, 16, 20, 3.", gap=45)
    rx = X0 + lw + 0.25
    rw = WIDTH - lw - 0.25
    for i, (h, b, f) in enumerate([("What is measured", "How often the evidence for each component exists, of 20 questions.", TINT),
                                   ("What is by construction", "Flat admits none of the three. The preconditions read graph structure.", TINT),
                                   ("What it does not show", "Admitted is not correct or useful. The grid is not yet selective.", GOLD_TINT)]):
        y = TOP + i * 1.38
        box(s, rx, y, rw, 1.26, fill=f, name=h)
        text(s, rx + 0.18, y + 0.1, rw - 0.36, 0.32, h, size=16, color=NAVY, bold=True)
        text(s, rx + 0.18, y + 0.45, rw - 0.36, 0.78, b, size=14)
    foot(s, "Admission over 20 questions, one graph, five components measured. Not peer reviewed.")

    # ------------------------------------------------------------------ 17. Grounding
    s = d.content("New findings", "Grounding holds with a real model, relevance is not yet shown",
                  "We also ran the whole system with a real model. All thirty-eight answerable questions were answered. The one "
                  "question the corpus cannot answer was refused. All one hundred and twenty-five citations were verbatim. And the "
                  "judge removed ten claims that had a real citation under them but were not supported by it, which is the case for "
                  "checking each claim. But look at the second row. Citation precision is about 0.21, and half the answers cite "
                  "nothing in the gold set. The gold set is incomplete, so this does not show the answers are wrong. It does show "
                  "that grounded and relevant are different things.", tag="After the paper")
    stats = [("38 of 38", "answerable questions answered"), ("1 of 1", "unanswerable control refused"),
             ("125 of 125", "quotes verbatim from the stored passage"), ("10 of 140", "claims removed as unsupported by the judge")]
    cw = (WIDTH - 0.6) / 4
    for i, (n, l) in enumerate(stats):
        x = X0 + i * (cw + 0.2)
        box(s, x, TOP, cw, 1.72, fill=TINT, name=n)
        text(s, x + 0.18, TOP + 0.14, cw - 0.3, 0.7, n, size=32, color=NAVY, bold=True)
        text(s, x + 0.18, TOP + 0.85, cw - 0.3, 0.8, l, size=15)
    cw2 = (WIDTH - 0.4) / 3
    for i, (n, l) in enumerate([("0.21", "citation precision"), ("0.21", "gold recall"), ("19 of 38", "answers cite no gold-relevant passage")]):
        x = X0 + i * (cw2 + 0.2)
        box(s, x, 3.68, cw2, 1.15, fill=GOLD_TINT, name=l)
        text(s, x + 0.18, 3.78, 1.65 if i == 2 else 1.1, 0.9, n, size=26 if i == 2 else 30, color=GOLD_TEXT, bold=True, anchor=MSO_ANCHOR.MIDDLE)
        off = 1.9 if i == 2 else 1.3
        text(s, x + off, 3.78, cw2 - off - 0.12, 0.9, l, size=15, anchor=MSO_ANCHOR.MIDDLE)
    callout(s, 4.98, 0.82, "Nothing appears without a verbatim source. Grounded and relevant are different things.")
    foot(s, "One live run, one model, no repeat. The gold set is a floor, not a full list. Not peer reviewed.")

    # ------------------------------------------------------------------ 18. Conclusion
    s = d.content("Conclusion", "What this does and does not show",
                  "To conclude. The interface guarantees hold by construction, and the bound follows from the preconditions. "
                  "The empirical picture is more modest. There is no evidence of a retrieval gain from the graph on this corpus, "
                  "and no evidence yet about learning, because no user study has been run. Next comes a human audit of the graph's "
                  "links, checking each block against its specific evidence at build time, and the interface study itself. The "
                  "point I would like you to keep is this: the components an interface can honestly offer are those whose "
                  "preconditions retrieval can satisfy.")
    cw = (WIDTH - 0.4) / 3
    cols = [("Established", TINT, NAVY, ["Interface guarantees hold by construction", "The bound follows from preconditions", "Grounding held in one live run"]),
            ("Not shown", GOLD_TINT, RED, ["A retrieval gain from the graph", "Correctness of what is admitted", "Extraction quality, by human audit", "Any learning outcome"]),
            ("Next", TINT, NAVY, ["Human audit of graph links", "Check each block against its own edges at build time", "Make components more selective", "Run the interface study"])]
    for i, (h, f, c, items_) in enumerate(cols):
        x = X0 + i * (cw + 0.2)
        box(s, x, TOP, cw, 2.92, fill=f, name=h)
        text(s, x + 0.2, TOP + 0.1, cw - 0.4, 0.35, h, size=18, color=c, bold=True)
        text(s, x + 0.2, TOP + 0.55, cw - 0.4, 2.3, items_, size=16, bullet=True, after=8)
    callout(s, 4.86, 1.0, [[("The components an interface can honestly offer are those whose preconditions retrieval can satisfy.", {"size": 19})]])

    # ------------------------------------------------------------------ 19. References
    s = d.content("References", "Selected references",
                  "These are the references cited on the slides, numbered as in the paper. The full list is in the proceedings.")
    refs_l = ["[1] Y. Gao et al., RAG for large language models: a survey, arXiv:2312.10997, 2024.",
              "[2] B. Sarmah et al., HybridRAG, arXiv:2408.04948, 2024.",
              "[3] D. Edge et al., From local to global: a graph RAG approach, arXiv:2404.16130, 2024.",
              "[4] R. E. Mayer, Cognitive theory of multimedia learning, Educ. Psychol. Rev., 2024.",
              "[5] M. A. Fadillah et al., Meta-analysis of PhET simulations, Int. J. Online Biomed. Eng., 2026.",
              "[6] Y. Leviathan et al., Generative UI, arXiv:2604.09577, 2026.",
              "[7] S. Tu et al., MAIC-UI, arXiv:2604.25806, 2026.",
              "[8] T. Calò and C. J. MacLellan, Educator-driven tutor authoring, L@S '24, 2024.",
              "[9] X. J. Wang et al., LearnMate², DIS '26, 2026.",
              "[10] S. P. Neshaei et al., The missing layer, arXiv:2606.15902, 2026.",
              "[11] J. Irigoyen et al., EduEVAL-DB, arXiv:2602.15531, 2026.",
              "[12] A. Shoufan and A. A. A. Esmaeil, AI hallucination from students' perspective, arXiv:2602.17671, 2026.",
              "[13] J. Liao et al., Code monitor red teaming, arXiv:2607.20852, 2026."]
    refs_r = ["[14] H. Han et al., RAG with graphs (GraphRAG), arXiv:2501.00309, 2024.",
              "[15] B. J. Gutiérrez et al., HippoRAG, NeurIPS, 2024.",
              "[16] Z. Guo et al., LightRAG, arXiv:2410.05779, 2024.",
              "[17] T. Zhang and H. Soh, Extract, define, canonicalize, EMNLP, 2024.",
              "[18] Y. Liu et al., AlignUI, arXiv:2601.17614, 2026.",
              "[19] Y. Liu et al., CrowdGenUI, arXiv:2411.03477, 2024.",
              "[20] Agent2UI, technical specification, 2025. Not peer reviewed.",
              "[21] Y. Ben-Zion et al., AI for rapid generation of physics simulations, arXiv:2412.07482, 2024.",
              "[22] T. N.-D. Tran et al., ChemersiveLLM, VRST '25, 2025.",
              "[23] X. Li et al., Beyond superficial tests, Findings of ACL 2026.",
              "[24] Q. Li et al., AdverMCTS, arXiv:2604.10449, 2026.",
              "[25] J. Kwok et al., LLM-as-a-verifier, arXiv:2607.05391, 2026.",
              "[26] G. V. Cormack et al., Reciprocal rank fusion, SIGIR, 2009."]
    cw = (WIDTH - 0.4) / 2
    text(s, X0, TOP, cw, 4.1, refs_l, size=12, after=3, name="References left")
    text(s, X0 + cw + 0.4, TOP, cw, 4.1, refs_r, size=12, after=3, name="References right")

    # ------------------------------------------------------------------ 20. Thank you
    d.n += 1
    s = prs.slides.add_slide(d.blank)
    pic = s.shapes.add_picture(str(ASSETS / "cover-bg.png"), 0, 0, prs.slide_width, prs.slide_height)
    pic.name = "Cover background"
    set_alt(pic, "MCAIT 2026 cover artwork")
    box(s, 0, 0, 8.7, 7.5, fill=NAVY, shape=MSO_SHAPE.RECTANGLE, name="Cover panel")
    text(s, 0.72, 0.46, 3.4, 0.4, "MCAIT 2026", size=18, color=GOLD, bold=True)
    box(s, 0.72, 1.08, 1.6, 0.035, fill=GOLD, shape=MSO_SHAPE.RECTANGLE, name="Template rule")
    text(s, 0.74, 1.45, 7.3, 0.95, "Thank you", size=54, color=WHITE, bold=True)
    text(s, 0.76, 2.5, 7.2, 0.5, "Questions are welcome.", size=24, color=GOLD)
    text(s, 0.77, 3.3, 7.2, 1.2, ["Fakhrul Azim Bin Ahmed Mardzukie", "fakhrul_22012087@utp.edu.my", "github.com/Azimlearning/Arcana"], size=18, color=WHITE, after=4)
    box(s, 0.77, 5.05, 2.35, 1.1, fill=WHITE, radius=0.1, name="Logo backing")
    lg = s.shapes.add_picture(str(logo_path), Inches(0.92), Inches(5.2), width=Inches(2.05))
    lg.name = "UTP logo"
    set_alt(lg, "Universiti Teknologi PETRONAS logo")
    text(s, 0.77, 6.75, 7.5, 0.3, "3–5 NOVEMBER 2026  ·  TAIBAH UNIVERSITY  ·  MADINAH", size=12, color=WHITE)
    s.notes_slide.notes_text_frame.text = "Thank you. The code and protocol are public, and I am happy to take questions."

    prs.save(str(OUT))
    print("saved", OUT, "slides", len(prs.slides))


if __name__ == "__main__":
    sys.exit(build())
