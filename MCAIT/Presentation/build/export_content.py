"""Writes Presentation/Slide-Content.md from 179.pptx, so the review copy always matches the deck."""
import sys
from pathlib import Path

from pptx import Presentation

ROOT = Path(__file__).resolve().parent.parent
QA = (Path(__file__).parent / "qa.md").read_text(encoding="utf-8")
DECK = sys.argv[1] if len(sys.argv) > 1 else "179.pptx"
prs = Presentation(str(ROOT / DECK))
out = ["# MCAIT 2026 slide content\n", "Generated from the deck file. Refer to slide numbers when asking for changes.\n"]
words = 0
HIDDEN = {"MCAIT background", "Cover background", "Picture 1", "Picture 2", "UTP logo"}
SKIP = {"Title", "Section label", "Slide number", "Line of prose"}


def shape_text(sh):
    lines = []
    if sh.has_text_frame:
        lines += [p.text.strip() for p in sh.text_frame.paragraphs if p.text.strip()]
    if getattr(sh, "has_table", False) and sh.has_table:
        for r, row in enumerate(sh.table.rows):
            cells = [c.text.strip().replace("\n", " ") or " " for c in row.cells]
            lines.append("| " + " | ".join(cells) + " |")
            if r == 0:
                lines.append("|" + "---|" * len(cells))
    return lines


for i, s in enumerate(prs.slides, 1):
    title = next((sh.text_frame.text for sh in s.shapes if sh.name == "Title"), None) or {1: "Title slide"}.get(i, "Thank you")
    out.append(f"\n## Slide {i}. {title}\n")
    for sh in s.shapes:
        if sh.name in SKIP:
            continue
        if sh.shape_type == 13 and sh.name not in HIDDEN:
            out.append(f"*[Image: {sh.name}]*\n")
        if getattr(sh, "has_chart", False) and sh.has_chart:
            out.append(f"*[Chart: {sh._element.xpath('.//p:cNvPr')[0].get('descr')}]*\n")
        lines = shape_text(sh)
        if lines:
            out.append("\n".join(lines) + "\n")
    note = s.notes_slide.notes_text_frame.text
    words += len(note.split())
    out.append(f"**Say:** {note}\n")
out.append(f"\n---\n\nSpoken length: {words} words, about {words / 130:.1f} minutes at 130 words a minute.\n\n")
out.append(QA)
(ROOT / ("Slide-Content.md" if DECK == "179.pptx" else "Slide-Content-v2.md")).write_text("\n".join(out), encoding="utf-8")
print("words", words)
