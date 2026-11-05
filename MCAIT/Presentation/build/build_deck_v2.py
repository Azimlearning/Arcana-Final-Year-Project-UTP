"""Builds Presentation/179-v2.pptx, the deeper alternative, from 179.pptx plus new slides.

179.pptx is only read. Reused slides keep their design and get shorter speaker notes.
"""
import json
import subprocess
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.chart import XL_CHART_TYPE, XL_LABEL_POSITION, XL_TICK_LABEL_POSITION
from pptx.chart.data import CategoryChartData
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

import build_deck as bd
from build_deck import (ASSETS, BOTTOM, CYAN, CYAN_TINT, GOLD, GOLD_TEXT, GOLD_TINT, INK, MUTED, NAVY, NAVY2, RED, RULE, TINT, TOP, WHITE, WIDTH, X0, X1,
                        arrow, bar_chart, box, callout, foot, rgb, set_alt, table, text)

ROOT = bd.ROOT
DATA = json.load(open(Path(__file__).parent / "motion" / "data.json", encoding="utf-8"))
prs = Presentation(str(ROOT / "179.pptx"))
BLANK = prs.slides[1].slide_layout
ORIGINAL = list(prs.slides)
BYTITLE = {t: s_ for s_ in ORIGINAL for t in [next((sh.text_frame.text for sh in s_.shapes if sh.name == "Title"), None)] if t}
OLD = {2: "The claim of this paper", 3: "Learners ask relational questions and get prose", 4: "Flat retrieval has no way to represent a relation", 5: "Four literatures, and the gap between them",
       6: "Generative interfaces are reaching the market", 7: "Contributions", 9: "Three regimes for producing a learning interface", 10: "From document to rendered component",
       11: "The model composes the interface. It does not write it.", 12: "A worked request from the paper", 13: "Retrieval structure bounds interface expressiveness",
       14: "Committed protocol, and a pilot reported as found", 15: "Where Arcana began: VERA AI", 17: "What retrieval structure makes possible", 18: "On the full corpus, a retrieval gain is not shown",
       19: "The graph does extend the interface: 2 components against 5", 20: "Grounding holds with a real model, relevance is not yet shown", 21: "What this does and does not show", 22: "Selected references"}
V1 = {k: BYTITLE[t] for k, t in OLD.items()}
V1[1], V1[23] = ORIGINAL[0], ORIGINAL[-1]
ADAPT = BYTITLE["Adaptive interface: where expressiveness shows"]
GENLAB = BYTITLE["Beyond the catalogue: generated, then verified"]


def new_slide(eyebrow, title, notes, tag=None):
    s = prs.slides.add_slide(BLANK)
    pic = s.shapes.add_picture(str(ASSETS / "content-bg.png"), 0, 0, prs.slide_width, prs.slide_height)
    pic.name = "MCAIT background"
    set_alt(pic, "MCAIT 2026 conference header and footer")
    text(s, X0, 0.93, 9.5, 0.25, eyebrow.upper(), size=12, color=GOLD_TEXT, bold=True, name="Section label")
    text(s, X0, 1.13, WIDTH - (2.0 if tag else 0), 0.55, title, size=28, color=NAVY, bold=True, name="Title", anchor=MSO_ANCHOR.MIDDLE)
    if tag:
        fill = NAVY2 if tag == "In the paper" else CYAN
        box(s, X1 - 1.75, 1.2, 1.75, 0.38, tag, fill=fill, color=WHITE, size=13, bold=True, radius=0.19, name="Evidence tag")
    text(s, X1 - 0.6, 6.03, 0.6, 0.22, "0", size=11, color=MUTED, align=PP_ALIGN.RIGHT, name="Slide number")
    s.notes_slide.notes_text_frame.text = notes
    return s


def poster(video, t):
    out = ASSETS / f"poster-{video}.png"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(t), "-i", str(ASSETS / f"{video}.mp4"), "-frames:v", "1", str(out)], check=True)
    return out


def video_slide(eyebrow, title, notes, video, t, cards, footer, tag=None):
    s = new_slide(eyebrow, title, notes, tag)
    w = 7.15
    mv = s.shapes.add_movie(str(ASSETS / f"{video}.mp4"), Inches(X0), Inches(TOP), Inches(w), Inches(w * 9 / 16),
                            poster_frame_image=str(poster(video, t)), mime_type="video/mp4")
    mv.name = title
    set_alt(mv, title)
    rx = X0 + w + 0.3
    rw = WIDTH - w - 0.3
    for i, (h, b) in enumerate(cards):
        y = TOP + i * 1.38
        box(s, rx, y, rw, 1.26, fill=GOLD_TINT if i == len(cards) - 1 else TINT, name=h)
        text(s, rx + 0.18, y + 0.09, rw - 0.36, 0.32, h, size=16, color=NAVY, bold=True)
        text(s, rx + 0.18, y + 0.44, rw - 0.36, 0.8, b, size=14)
    foot(s, footer)
    return s


def notes(s, value):
    s.notes_slide.notes_text_frame.text = value


# ---------------------------------------------------------------- new slides
personas = new_slide("Background and problem", "Three learners hit the same wall",
    "Picture three learners. Aisha is writing a literature review across twenty papers and connects them by hand. Daniel keeps a growing thesis corpus and "
    "keeps losing context. Mei is revising, and summaries help her read but not remember. Each needs a different view of the same documents, and each gets the same chat box.")
cw = (WIDTH - 0.4) / 3
for i, (ini, n, who, need, gets) in enumerate([
        ("A", "Aisha", "Final-year undergraduate writing a literature review", "How do 15 to 20 papers relate, agree and conflict?", "Comparison grid, contradiction view"),
        ("D", "Daniel", "Master's student with a growing thesis corpus", "What does my corpus not cover yet?", "Connected knowledge base, gap view"),
        ("M", "Mei", "Undergraduate revising dense modules for exams", "Summaries help me read. How do I remember?", "Quizzes, flashcards, Socratic questions")]):
    x = X0 + i * (cw + 0.2)
    box(s := personas, x, TOP, cw, 3.95, fill=TINT, name=n)
    box(s, x + 0.2, TOP + 0.18, 0.72, 0.72, ini, fill=NAVY if i % 2 == 0 else CYAN, color=WHITE, size=22, bold=True, shape=MSO_SHAPE.OVAL, margin=0)
    text(s, x + 1.05, TOP + 0.16, cw - 1.2, 0.36, n, size=20, color=NAVY, bold=True)
    text(s, x + 1.05, TOP + 0.52, cw - 1.2, 0.7, who, size=13, color=MUTED)
    text(s, x + 0.2, TOP + 1.3, cw - 0.4, 0.3, "THEIR QUESTION", size=12, color=GOLD_TEXT, bold=True)
    text(s, x + 0.2, TOP + 1.58, cw - 0.4, 1.0, need, size=17, bold=True, color=INK)
    text(s, x + 0.2, TOP + 2.72, cw - 0.4, 0.3, "THE VIEW IT CALLS FOR", size=12, color=GOLD_TEXT, bold=True)
    text(s, x + 0.2, TOP + 3.0, cw - 0.4, 0.8, gets, size=15, color=INK)
foot(s, "Design personas from the project requirements, not study participants.")

ingest = video_slide("Methodology", "Ingestion: a sentence becomes an edge",
    "Let me follow one real question through the system, starting with ingestion. Here are real sentences from three papers in the corpus. Extraction turns each stated relation into an edge. "
    "The same concept, BM25, appears in all three, so three documents become connected. Nobody defined these relation types in advance.",
    "video-ingest", 15.4,
    [("Schema-free", "Entities and relations are extracted with no fixed ontology, so any discipline works."),
     ("One pass", "The vector index and the graph are written together, over the same passages."),
     ("One concept, three papers", "BM25 links documents that never cite each other in this example.")],
    "Click to play. Real sentences and edges from the stored graph of 16 papers. Extraction by one model, one pass per passage.", "After the paper")
# "never cite each other" is not verified, so the card is reworded below.
for sh in ingest.shapes:
    if sh.has_text_frame and "never cite each other" in sh.text_frame.text:
        sh.text_frame.paragraphs[0].runs[0].text = "BM25 is one node reached from all three passages, across document boundaries."

stats = new_slide("Methodology", "What the extracted graph really holds",
    "This is what that produces at scale: over eleven thousand concepts and nearly fourteen thousand edges. On the left, the biggest hubs. On the right, the honest part. Only about a third of edges are stated in one sentence of their passage. "
    "Only eleven point six percent of concepts appear in more than one paper, and one idea can be several nodes. So the cross-document structure is real, but thin.", "After the paper")
gf = bar_chart(stats, X0, TOP - 0.05, 5.7, 4.1, ["GraphRAG", "RAG", "Large Language Models", "Knowledge graphs", "Self-RAG", "LLMs", "LLM"],
               [("Edges", (477, 420, 299, 268, 240, 198, 177))], [NAVY], horizontal=True, maxv=560,
               alt="Largest hubs by edges: GraphRAG 477, RAG 420, Large Language Models 299, Knowledge graphs 268, Self-RAG 240, LLMs 198, LLM 177", gap=35)
gf.chart.has_legend = False
rx = X0 + 5.95
rw = WIDTH - 5.95
text(stats, rx, TOP, rw, 0.3, "From 13,972 edges to those stated in one sentence", size=15, color=NAVY, bold=True)
for i, (lab, n, c, fg) in enumerate([("All edges", 13972, NAVY, WHITE), ("Both labels in the source passage", 9821, CYAN, WHITE), ("Stated in one sentence", 4830, GOLD, NAVY)]):
    w = rw * n / 13972
    box(stats, rx, TOP + 0.36 + i * 0.5, w, 0.43, f"{n:,}", fill=c, color=fg, size=15, bold=True, align=PP_ALIGN.LEFT, radius=0.05, margin=0.12)
    text(stats, rx + (w + 0.12 if i == 2 else 1.1), TOP + 0.45 + i * 0.5, rw - (w + 0.12 if i == 2 else 1.1), 0.3, lab, size=13, color=INK if i == 2 else WHITE)
sc = (rw - 0.2) / 2
for i, (n, l) in enumerate([("11.6%", "of concepts appear in 2 or more papers"), ("20.4%", "of concepts have no edge at all"),
                            ("1,604", "relation strings; authorship alone is spelled four ways"), ("3", 'nodes for one idea: "Large Language Models", "LLMs", "LLM"')]):
    x = rx + (i % 2) * (sc + 0.2)
    y = 3.75 + (i // 2) * 1.08
    box(stats, x, y, sc, 0.98, fill=TINT, name=n)
    text(stats, x + 0.12, y + 0.06, 1.05, 0.85, n, size=22, color=NAVY, bold=True, anchor=MSO_ANCHOR.MIDDLE)
    text(stats, x + 1.15, y + 0.06, sc - 1.25, 0.85, l, size=12, color=INK, anchor=MSO_ANCHOR.MIDDLE)
foot(stats, "Structure only, not correctness. 'Stated' is a strict lexical test, so the rest are not necessarily wrong. 16 papers, 1,570 passages, one extraction.")

traverse = video_slide("Methodology", "Graph traversal: one real route",
    "Now the question: how do the papers compare BM25 with dense retrieval? Its words resolve to four concepts. From those, the system follows seventy-four edges, one hop out. Passages that mention those concepts are then ranked. "
    "Three of the top ten are relevant, and they all came through BM25. The broad concept Retrieval drags in noise. That is resolution quality showing through.",
    "video-traverse", 16.4,
    [("Across 20 questions", "111 concepts resolved, 37% by approximate match. 16 to 755 edges followed per question."),
     ("How passages are reached", "87% mention a resolved concept. 13% come only through a neighbour."),
     ("Hubs are noisy", 'Broad seeds such as "Retrieval" pull in passages that are not relevant.')],
    "Click to play. Real route for question q-cross-06. Gold-relevant means covering an approved gold passage under the frozen rule.", "After the paper")

fuse = video_slide("Methodology", "Rank fusion: why a second vote matters",
    "Here is the fusion, with real numbers. The FEVER passage gets a vote from keywords and one from the graph, and rises to first. The second passage was not in the flat top ten at all, and got in only because the graph gave it a second vote. "
    "nDCG goes from point two four to point five nine. But this is one of the largest gains. Averaged over all questions, the difference is zero.",
    "video-fuse", 14.4,
    [("Comparable by rank", "Cosine, keyword and traversal scores differ in kind, so only ranks are combined [26]."),
     ("A second vote", "The rank 2 passage: dense 6, graph 7. Flat ranked it outside its top 10."),
     ("Chosen as an example", "This is one of the largest gains. The next slides show the whole distribution.")],
    "Click to play. Scores recomputed from the stored rankings at k = 60; ties keep the stored order. Question q-cross-06.", "After the paper")

compose = video_slide("Methodology", "Composition: verified components, nothing else",
    "With evidence in hand, the model composes. It picks typed components and fills them from what was retrieved. It writes no markup. A malformed block hits the validator on the server and is rejected, not repaired. "
    "We fail closed on purpose: a visible error can be recovered from, a confident wrong presentation cannot. The paper also states the gaps, shown here.",
    "video-compose", 6.6,
    [("Fails closed", "One schema generates both sides of the wire. Any violation becomes an error, not a partial render."),
     ("Registry only", "An unregistered block has no path to the screen, and omitting one fails the build."),
     ("Stated in the paper", "Claim checking fails open on a provider error. Contradiction quotes are not yet matched verbatim.")],
    "Click to play. Illustration of the method, using the paper's worked example. 24 of 24 components registered, 645 tests passing in CI.", "In the paper")

trace = new_slide("Methodology", "One request, traced end to end",
    "This is one real turn from the live run. The Orchestrator routes it, the Graph agent and Research gather evidence, and the Fact Checker removed one of six claims. Agents never call each other directly, and every path ends at composition. "
    "And across thirty-nine questions, there were seven different combinations of components. That is the interface following the question.", "After the paper")
steps = [("Orchestrator", "routes: compare", TINT, INK), ("Graph", "structure, alignment", TINT, INK), ("Research", "8 passages, 6 quotes", TINT, INK),
         ("Fact Checker", "removed 1 of 6", GOLD_TINT, INK), ("Composer", "5 blocks", NAVY, WHITE)]
bw = (WIDTH - 4 * 0.3) / 5
for i, (a, b, f, c) in enumerate(steps):
    x = X0 + i * (bw + 0.3)
    box(trace, x, TOP, bw, 0.95, [a, [(b, {"size": 13, "bold": False})]], fill=f, color=c, size=16, bold=True, name=a)
    if i < 4:
        arrow(trace, x + bw, TOP + 0.47, x + bw + 0.3, TOP + 0.47, color=NAVY, width=2)
text(trace, X0, 2.85, 5.0, 0.3, "Question q-cross-01: 11.1 seconds, about US$0.02", size=14, color=MUTED)
text(trace, X0, 3.15, 5.3, 0.3, "Routing across 39 questions", size=15, color=NAVY, bold=True)
for i, (n, l) in enumerate([("29", "compare"), ("9", "single"), ("1", "relate")]):
    x = X0 + i * 1.72
    box(trace, x, 3.5, 1.58, 1.0, fill=TINT, name=l)
    text(trace, x + 0.1, 3.53, 1.38, 0.55, n, size=28, color=NAVY, bold=True, align=PP_ALIGN.CENTER)
    text(trace, x + 0.1, 4.1, 1.38, 0.3, l, size=14, align=PP_ALIGN.CENTER)
box(trace, X0, 4.65, 5.02, 1.15, "Agents never import each other. Every hand-off goes through one routing function, within hop and token budgets.", fill=TINT, size=14, align=PP_ALIGN.LEFT, margin=0.15, name="Routing rule")
cats = ["Summary, sources, graph, route, grid", "Summary, sources", "Summary, sources, graph, grid", "Summary, sources, route, grid", "Summary, sources, grid", "All of it, with concept map", "Graph, grid, concept map"]
gf = bar_chart(trace, X0 + 5.2, 3.1, WIDTH - 5.2, 2.85, cats, [("Questions", (13, 9, 6, 5, 3, 2, 1))], [NAVY], horizontal=True, maxv=16,
               alt="Seven combinations of components across 39 questions: 13, 9, 6, 5, 3, 2 and 1 questions", gap=25)
gf.chart.has_legend = False
gf.chart.category_axis.tick_labels.font.size = Pt(11)
gf.chart.plots[0].data_labels.font.size = Pt(11)
text(trace, X0 + 5.2, 2.85, WIDTH - 5.2, 0.3, "7 combinations of components across 39 questions", size=15, color=NAVY, bold=True)
foot(trace, "One live run, real model, no repeat. Route = TraversalView. Every combination also includes a cited summary and a source list.")

boundv = video_slide("Central claim", "The bound, as a picture",
    "Here is the bound as a picture. Each retrieval layer can honestly fill only some components. Flat retrieval lights up three. Graph-hybrid lights up all six. The dark ones on the left could still be drawn, but the model would have to supply the relation itself.",
    "video-bound", 6.5,
    [("Not a rendering limit", "Any renderer can draw a grid. The question is what fills it."),
     ("A design rule", "Admit a component only once retrieval can satisfy what it asserts."),
     ("Why it matters", "A rich catalogue on flat retrieval is filled by the model, not by evidence.")],
    "Click to play. Illustration of Table III of the paper.", "In the paper")

demoq = video_slide("From paper to practice", "Demo: same corpus, different questions",
    "This is Arcana on the sixteen papers, with a real model. A relational question gets a cited summary and a graph. A comparison gets a grid, where a cell says no evidence if a paper has nothing. A question the papers cannot answer gets a refusal. Nobody designed these screens in advance.",
    "video-demo-questions", 5.5,
    [("Relational question", "A cited summary, and relations that each cite their sentence."),
     ("Comparison", 'A grid. Each cell quotes its source, or says "No evidence in this paper".'),
     ("Unanswerable", "It says so, instead of inventing an answer.")],
    "Click to play. Real-model run on 16 papers.", "After the paper")

demot = video_slide("From paper to practice", "Demo: from answers to learning",
    "And the learning side. Concept pages are built from the graph, and each stated link shows its sentence and page. The quiz comes from the learner's own documents. A wrong answer is corrected, and the graph recolours by mastery. And a lab is offered only where a stored passage states the formula, verified across every slider setting.",
    "video-demo-tools", 12.0,
    [("Concept pages", "Built from the graph. Every stated link shows its sentence and page."),
     ("Quiz and mastery", "A wrong answer is corrected with its source, and the graph recolours."),
     ("Verified lab", "Offered only where a passage states the formula. 120 of 120 planted defects refused.")],
    "Click to play. No model call in these tools. The lab's function is a test fixture, passed through the real verifier. Planted set written by the project.", "After the paper")

perq = new_slide("New findings", "Every question: the graph helps some and hurts others",
    "Here is every question, sorted. Nine improve with the graph, fourteen tie, fifteen get worse. So the average hides large swings in both directions. The table shows where. On the original cross-document questions the hybrid is ahead. On single-document questions, it is behind. A good system would know when to use the graph, and that is a direction this suggests.", "After the paper")
pq = sorted(DATA["per_question"], key=lambda p: p["hybrid"] - p["flat"])
assert len(pq) == 38
cd = CategoryChartData()
cd.categories = [p["q"] for p in pq]
cd.add_series("Hybrid minus flat", [round(p["hybrid"] - p["flat"], 3) for p in pq])
gf = perq.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(X0), Inches(TOP + 0.25), Inches(6.5), Inches(3.75), cd)
set_alt(gf, "Hybrid minus flat nDCG for 38 questions, sorted, from minus 0.343 to plus 0.420. 15 worse, 14 tied, 9 better.")
ch = gf.chart
ch.has_legend = False
ch.has_title = False
ca, va = ch.category_axis, ch.value_axis
ca.tick_label_position = XL_TICK_LABEL_POSITION.NONE
ca.format.line.color.rgb = rgb(MUTED)
va.has_major_gridlines = False
va.minimum_scale, va.maximum_scale, va.major_unit = -0.4, 0.5, 0.2
va.tick_labels.font.size = Pt(12)
va.tick_labels.font.name = bd.FONT
va.tick_labels.font.color.rgb = rgb(INK)
va.tick_labels.number_format = "+0.0;-0.0;0"
va.tick_labels.number_format_is_linked = False
va.format.line.fill.background()
plot = ch.plots[0]
plot.gap_width = 25
ser = plot.series[0]
ser.invert_if_negative = False
for i, p in enumerate(pq):
    d = p["hybrid"] - p["flat"]
    pt = ser.points[i]
    pt.format.fill.solid()
    pt.format.fill.fore_color.rgb = rgb(GOLD if d > 0 else (RED if d < 0 else RULE))
    dpt = pt.format._element if False else ser._element.xpath(f'c:dPt[c:idx/@val="{i}"]')[0]
    inv = dpt.makeelement("{http://schemas.openxmlformats.org/drawingml/2006/chart}invertIfNegative", {"val": "0"})
    dpt.insert(1, inv)
text(perq, X0, TOP, 6.5, 0.3, "Hybrid minus flat, nDCG@10, 38 questions sorted", size=15, color=NAVY, bold=True)
rx = X0 + 6.75
rw = WIDTH - 6.75
for i, (n, l, c) in enumerate([("9", "better", GOLD_TEXT), ("14", "tied", MUTED), ("15", "worse", RED)]):
    x = rx + i * (rw / 3)
    box(perq, x, TOP, rw / 3 - 0.12, 0.95, fill=TINT, name=l)
    text(perq, x + 0.05, TOP + 0.04, rw / 3 - 0.22, 0.55, n, size=28, color=c, bold=True, align=PP_ALIGN.CENTER)
    text(perq, x + 0.05, TOP + 0.6, rw / 3 - 0.22, 0.3, l, size=14, align=PP_ALIGN.CENTER)
cm = DATA["cat_means"]
rows = [["Set, category", "n", "Flat", "Hybrid"]]
for key, lab in [("original|cross_document", "Original, cross-document"), ("original|single_document", "Original, single-document"), ("original|contradiction", "Original, contradiction"),
                 ("new|cross_document", "New, cross-document"), ("new|single_document", "New, single-document")]:
    rows.append([lab, str(cm[key]["n"]), f"{cm[key]['flat']:.3f}", f"{cm[key]['hybrid']:.3f}"])
table(perq, rx, TOP + 1.1, rw - 0.05, rows, [3.2, 0.6, 1, 1.1], size=14, row_h=0.41, styles={("row", 1): {"fill": GOLD_TINT, "bold": True}, ("col", 0): {"color": NAVY}})
foot(perq, "Range: -0.343 to +0.420. Mean nDCG@10 per set. No pair reaches p < 0.05. Questions were not randomly sampled. Not peer reviewed.")

tried = new_slide("New findings", "What we tried, and what did not hold up",
    "Evaluation also killed some of our own ideas. On the original questions, deeper retrieval looked like a real gain, but a rule fixed in advance reversed it when it failed on new questions. The graph seemed to help more as the corpus grew, and that did not replicate either. A trained re-ranker did not help. A cleaner graph with forty percent of the edges did about as well. I report these because negative results are part of the evidence.", "After the paper")
rows = [["Change", "Looked like", "When tested", "Verdict"],
        ["30 candidates per signal", "Recall@10 +0.093, 19 questions (p = 0.094)", "-0.007 on 19 new questions (p = 1.0)", "Reversed, by a rule fixed in advance"],
        ["Graph signal at larger scale", "-0.022 at 285 passages, +0.039 at 1,570", "-0.042 on new questions, -0.001 pooled", "Did not replicate"],
        ["Pretrained cross-encoder re-ranker", "Standard next step", "-0.007 nDCG@10 (p = 0.90), about 5 s per query", "Left off"],
        ["Cleaner atomic-note graph", "61% of the nodes, 40% of the edges", "+0.010 fused, pooled (p = 0.86)", "About level from a smaller graph"]]
table(tried, X0, TOP, WIDTH, rows, [3, 3.6, 3.5, 2.6], size=14, row_h=0.6, styles={("col", 0): {"bold": True, "color": NAVY}, ("col", 3): {"fill": GOLD_TINT, "bold": True}})
callout(tried, 4.95, 0.85, "The rule for the new questions was fixed before they ran, so a result could not be quietly kept.")
foot(tried, "Descriptive, 38 questions in two differently drawn sets, one corpus. Not peer reviewed.")

checker = new_slide("New findings", "We tested the checkers too",
    "A checker you have not tested is just a claim, so we planted defects. Fake quotes and wrong citations were caught every time. Invented claims nearly always. But a negated claim, zero out of fifty. A word-overlap rule cannot see the word not. That is why claim checking needs a model judge, and in the live run the judge removed ten claims that a real quote did not support. These defects were written by the project, so they show known shapes, not a general rate.", "After the paper")
gf = bar_chart(checker, X0, TOP + 0.2, 7.2, 3.9, ["Quote not verbatim", "Cites the wrong passage", "Cites the wrong document", "Invented, other document", "Invented, same document", "Negated claim"],
               [("Detected of 50", (50, 50, 50, 49, 48, 0))], [NAVY], horizontal=True, maxv=58,
               alt="Planted defects detected of 50: quote not verbatim 50, wrong passage 50, wrong document 50, invented other document 49, invented same document 48, negated claim 0", gap=35)
gf.chart.has_legend = False
text(checker, X0, TOP, 7.2, 0.3, "Fact-check defects detected, of 50 each, word-overlap rule only", size=15, color=NAVY, bold=True)
rx = X0 + 7.45
rw = WIDTH - 7.45
for i, (h, b, f) in enumerate([("The blind spot", "Word overlap cannot see a negated or altered claim: 0 of 50.", GOLD_TINT),
                               ("Why a judge is needed", "In the live run the model judge removed 10 of 140 claims under valid quotes.", TINT),
                               ("Clean answers", "50 of 50 clean answers were kept, so the rule did not over-refuse.", TINT)]):
    y = TOP + i * 1.38
    box(checker, rx, y, rw, 1.26, fill=f, name=h)
    text(checker, rx + 0.18, y + 0.1, rw - 0.36, 0.32, h, size=16, color=NAVY, bold=True)
    text(checker, rx + 0.18, y + 0.45, rw - 0.36, 0.78, b, size=14)
foot(checker, "A planted set written by the project: known shapes, not an unbiased rate. The judge's own accuracy is not yet measured.")

# ---------------------------------------------------------------- backup
divider = new_slide("Backup", "Backup slides, for questions", "Backup only. Use these if a question calls for them.")
text(divider, X0, 2.2, WIDTH, 3, ["Rank fusion: the full top 10 for the worked example", "Admission by question: which components each question could support",
                                  "The wire contract, and how a component is added", "Cost and latency", "The real graph and a comparison grid", "Safeguards, and what each contains"], size=20, bullet=True, after=10)

ffull = new_slide("Backup", "Rank fusion: the full top 10", "Backup. The full fused list for the worked question.", "After the paper")
rows = [["#", "Passage", "Dense", "Sparse", "Graph", "RRF", "Gold", "In flat top 10"]]
NM = {"2005.11401": "RAG for Knowledge-Intensive NLP", "2312.10997": "RAG Survey", "2212.10496": "Precise Zero-Shot Dense Retrieval", "2404.16130": "From Local to Global"}
LIGHT = "LightRAG"
for f in DATA["fusion"]:
    doc = f["doc"].strip()
    label = next((v for k, v in NM.items() if doc.startswith(k)), doc[11:] if doc[:4].isdigit() else doc)
    if "LightRAG" in doc:
        label = LIGHT
    rows.append([str(f["rank"]), f"{label}, p{f['page']}", str(f["dense"] or "-"), str(f["sparse"] or "-"), str(f["graph"] or "-"), f"{f['score']:.5f}", "yes" if f["relevant"] else "no", "yes" if f["in_flat"] else "no"])
st = {("col", 1): {"color": NAVY}}
for i, f in enumerate(DATA["fusion"], 1):
    if f["relevant"]:
        st[("row", i)] = {"fill": GOLD_TINT, "bold": True}
table(ffull, X0, TOP, WIDTH, rows, [0.5, 5, 0.9, 0.9, 0.9, 1.1, 0.8, 1.4], size=13, row_h=0.355, styles=st)
foot(ffull, "Question q-cross-06, k = 60. Scores recomputed from stored rankings; ties keep the stored order.")

heat = new_slide("Backup", "Admission by question", "Backup. Each question and which graph components its evidence could support.", "After the paper")
QS = ["cross-01", "cross-02", "cross-03", "cross-04", "cross-05", "cross-06", "cross-07", "cross-08", "cross-09", "cross-10", "cross-11", "cross-12", "single-01", "single-02", "single-03", "single-04", "contra-01", "contra-02", "contra-03", "contra-04"]
NOGRAPH = {"cross-06", "cross-12", "single-03", "contra-04"}
MAP = {"cross-07", "cross-10", "single-01"}
grid = [[0 if q in NOGRAPH else 1 for q in QS], [1] * 20, [1 if q in MAP else 0 for q in QS]]
assert sum(grid[0]) == 16 and sum(grid[2]) == 3
fig, ax = plt.subplots(figsize=(12.2, 3.1), dpi=220)
ax.imshow(grid, cmap=ListedColormap(["#EEF1F6", "#071E44"]), aspect="auto", vmin=0, vmax=1)
ax.set_xticks(range(20), QS, rotation=55, ha="right", fontsize=11, color="#1B2A41")
ax.set_yticks(range(3), ["Graph view  (16)", "Comparison grid  (20)", "Concept map  (3)"], fontsize=13, color="#1B2A41")
ax.set_xticks([x - .5 for x in range(21)], minor=True)
ax.set_yticks([y - .5 for y in range(4)], minor=True)
ax.grid(which="minor", color="white", linewidth=2.5)
ax.tick_params(which="both", length=0)
for sp in ax.spines.values():
    sp.set_visible(False)
fig.tight_layout()
fig.savefig(ASSETS / "admission-heatmap.png", facecolor="white")
plt.close(fig)
pic = heat.shapes.add_picture(str(ASSETS / "admission-heatmap.png"), Inches(X0), Inches(TOP), width=Inches(WIDTH))
set_alt(pic, "Heat map of 20 questions by 3 components. Graph view admitted on 16, comparison grid on 20, concept map on 3.")
pic.name = "Admission heat map"
foot(heat, "Dark = admitted. Availability, not quality. The worked example q-cross-06 has no graph view here: none of the edges returned by the Graph agent had a quote naming both ends.")

wire = new_slide("Backup", "The wire contract", "Backup. The block type as declared in the shared schema, and the three steps to add a component.", "After the paper")
box(wire, X0, TOP, 6.3, 3.95, fill=NAVY, name="Code panel")
text(wire, X0 + 0.25, TOP + 0.15, 5.9, 3.7, ["export interface ComparisonGrid {", '  type: "ComparisonGrid";', "  id: string;", "  meta: BlockMeta;", "  data: ComparisonGridData;", "}", "", "export type UIBlock =", "  | CitedSummary", "  | SourceList", "  | GraphView", "  | ComparisonGrid", "  | ..."], size=15, color=WHITE)
for shp in wire.shapes:
    if shp.has_text_frame and "export interface" in shp.text_frame.text:
        for para in shp.text_frame.paragraphs:
            for r in para.runs:
                r.font.name = "Courier New"
rx = X0 + 6.55
rw = WIDTH - 6.55
text(wire, rx, TOP, rw, 0.3, "Adding a component is three steps", size=16, color=NAVY, bold=True)
for i, t_ in enumerate(["Add the schema variant, and regenerate the server models", "Implement the component, with its four states", "Add one line to the registry"]):
    box(wire, rx, TOP + 0.42 + i * 0.72, 0.52, 0.52, str(i + 1), fill=NAVY, color=WHITE, size=15, bold=True, shape=MSO_SHAPE.OVAL, margin=0)
    text(wire, rx + 0.68, TOP + 0.42 + i * 0.72, rw - 0.7, 0.55, t_, size=15, anchor=MSO_ANCHOR.MIDDLE)
box(wire, rx, TOP + 2.7, rw, 1.25, "A payload change not reflected on both sides is a compile error. Generated models are strict and forbid unknown fields, so they fail closed.", fill=GOLD_TINT, size=15, align=PP_ALIGN.LEFT, margin=0.18, name="Why")
foot(wire, "From the shared schema package. Four states: empty, loading, partial, error.")

cost = new_slide("Backup", "Cost and latency", "Backup. What it costs to build and run.", "After the paper")
cards = [("US$5.81", "to ingest 16 papers, 1,570 passages"), ("US$0.0037", "per passage: extraction plus embedding"), ("15 of 1,570", "passages failed extraction (0.95%)"),
         ("US$0.017", "mean per question, real model"), ("US$0.045", "mean per writing turn"), ("481 ms", "mean hybrid retrieval, against 296 ms flat")]
cw = (WIDTH - 0.4) / 3
for i, (n, l) in enumerate(cards):
    x = X0 + (i % 3) * (cw + 0.2)
    y = TOP + (i // 3) * 1.95
    box(cost, x, y, cw, 1.78, fill=TINT, name=n)
    text(cost, x + 0.2, y + 0.2, cw - 0.4, 0.7, n, size=32, color=NAVY, bold=True)
    text(cost, x + 0.2, y + 0.98, cw - 0.4, 0.7, l, size=16)
foot(cost, "One ingestion, one live run, original 19 questions for latency. Embedding price is an assumption until reconciled with the provider.")

# ---------------------------------------------------------------- notes for reused slides
notes(V1[1], "Good afternoon. I am Fakhrul Azim from Universiti Teknologi PETRONAS. My paper asks why learners working across their own documents still get a chat box, and what it would take to give them something better.")
notes(V1[2], "Here is the claim in one sentence. The components a learning interface can honestly offer are bounded by what its retrieval can supply. I will take you through the problem, the method with one real worked question, the bound, and what we measured.")
notes(V1[3], "When you study across documents, the useful questions are about relationships: which sources agree, where they conflict, what is missing. Current tools answer with a paragraph. Interactive views can work very well, with a pooled effect of 0.83 in physics, but someone has to author them, and retrieval has nothing structured to fill them with.")
notes(V1[4], "The cause sits in retrieval. Standard retrieval scores every passage on its own. It holds no record that two passages disagree or that one concept depends on another. Graph retrieval changes what is stored, so a shared entity can bring passages from different documents together.")
notes(V1[5], "Four literatures touch this. Graph retrieval is evaluated as retrieval. Generative interfaces are evaluated by preference. Educational systems keep a human reviewer. Verification relies on oracles a learning view does not have. One recent paper argues runtime generation is unsafe because it cannot be verified at scale, and that objection stands unanswered.")
notes(V1[6], "Products are moving the same way. Gemini Notebook answers from your sources. ChatGPT chooses a format automatically. Gemini's dynamic view writes code per prompt. I report only what vendors publish, and I did not test them. None of these public descriptions states a rule linking a view to the retrieved structure behind it. Stating that rule is this paper's work.")
notes(V1[7], "The paper makes four contributions: the architecture, a verified interface layer, the formal bound, and a committed evaluation. Arcana is these ideas in practice. The claims belong to the paper, and Arcana is where they can be run and checked.")
notes(V1[9], "Authoring ahead is safe, but covers only what someone anticipated. Emitting markup at runtime covers anything, but is hard to verify. We take a third route: the model composes from a verified vocabulary. The price is expressiveness, because a question gets the closest available component.")
notes(V1[10], "Here is the design. Ingestion writes a vector index and a graph in one pass. Three signals are fused by rank. Task agents hand off through one routing function, and every path ends at validated components. Let me now walk one real question through this.")
notes(V1[12], "Here is the paper's teaching example. A chemistry learner asks why temperature raises reaction rate. Their notes stress collision frequency, and the chapter stresses activation energy. That difference is what a learner reproduces in an exam. The response composes three blocks, none authored for this question. A language model detects the disagreement, not a typed edge.")
notes(V1[13], "Formally: a component is a claim about the shape of an answer, and its precondition is what must hold in the evidence. Expressiveness is the set of components a retrieval layer can satisfy. So the catalogue you can honestly offer is a function of the retrieval beneath it.")
notes(V1[14], "The protocol was committed before any run. A provider quota stopped extraction, so the paper reports a pilot on four of sixteen documents. The result was null, and traversal returned nothing on fifteen questions, because entities needed an exact match. So the pilot located the ceiling: query entity resolution.")
notes(V1[15], "A word on where this began. Arcana grew out of VERA AI, an enterprise assistant from my internship, which already cited its answers. But documents were silos and the layout was fixed. It could cite well, yet had nothing structured to show how sources relate. This compares designs, not results.")
notes(V1[18], "After the paper we completed the study: all sixteen papers, repaired matching, and a gold set. On the harder original questions the hybrid is ahead, not significantly. On new questions it falls behind. Pooled, the difference is zero. So I claim no retrieval gain. Not shown to help is not the same as shown not to help.")
notes(V1[19], "The other half. Flat retrieval admits two of five measured components, and the hybrid all five. That flat cannot admit the other three follows from the definitions. What we measured is how often the evidence exists: sixteen questions for a graph, three for a multi-hop path. Admitted does not mean useful.")
notes(V1[20], "With a real model, all answerable questions were answered, the unanswerable one was refused, and every quote was verbatim. But citation precision is about 0.21. The gold set is incomplete, so this does not show the answers are wrong. It does show that grounded and relevant are different things.")
notes(V1[21], "To conclude. The guarantees hold by construction, and the bound follows from the preconditions. The empirical picture is more modest: no retrieval gain shown, and no learning outcome, because no user study has run. The point to keep: the components an interface can honestly offer are those whose preconditions retrieval can satisfy.")
notes(V1[17], "Backup. Part of the real graph, and a comparison grid filled from it.")
notes(V1[11], "Backup. The safeguards and the failure each contains.")

# ---------------------------------------------------------------- order
ORDER = [V1[1], V1[2], V1[3], personas, V1[4], V1[5], V1[6], V1[7], V1[9], V1[10], ingest, stats, traverse, fuse, compose, ADAPT, trace, V1[12], V1[13], boundv, V1[14], V1[15], demoq, demot, GENLAB,
         V1[18], perq, tried, V1[19], V1[20], checker, V1[21], V1[22], V1[23], divider, ffull, heat, wire, cost, V1[17], V1[11]]
lst = prs.slides._sldIdLst
by_part = {prs.part.related_part(x.rId): x for x in list(lst)}
for x in list(lst):
    lst.remove(x)
for s in ORDER:
    lst.append(by_part[s.part])
for x in by_part.values():  # slides left out: drop them and their media
    if x not in list(lst):
        prs.part.drop_rel(x.rId)
for i, s in enumerate(ORDER, 1):
    for sh in s.shapes:
        if sh.name == "Slide number":
            sh.text_frame.paragraphs[0].runs[0].text = str(i)
for sh in V1[23].shapes:
    pass
OUT = ROOT / "179-v2.pptx"
prs.save(str(OUT))
print("saved", OUT, len(ORDER))
talk = ORDER[:ORDER.index(V1[23]) + 1]
w = sum(len(s.notes_slide.notes_text_frame.text.split()) for s in talk)
print("main slides", len(talk), "words", w, "minutes", round(w / 130, 1))
print({ORDER.index(s) + 1: len(s.notes_slide.notes_text_frame.text.split()) for s in talk})
