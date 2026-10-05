"""Render the paper's figures as column-width, greyscale-safe PNGs.

Designed for a 3.4 in IEEE column at 400 dpi. No colour is load-bearing:
emphasis is carried by fill shade and border weight only.
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Times New Roman", "DejaVu Serif"]

COL_W = 3.4
DPI = 600

BOX = dict(boxstyle="round,pad=0.30,rounding_size=0.06", linewidth=0.8,
           edgecolor="black", facecolor="white")
GATE = dict(boxstyle="round,pad=0.32,rounding_size=0.06", linewidth=1.9,
            edgecolor="black", facecolor="0.86")
STORE = dict(boxstyle="round,pad=0.30,rounding_size=0.06", linewidth=0.8,
             edgecolor="black", facecolor="0.93")
OUT = dict(boxstyle="round,pad=0.30,rounding_size=0.06", linewidth=0.8,
           edgecolor="black", facecolor="white", linestyle="--")


def box(ax, x, y, text, style=BOX, fs=6.4):
    ax.text(x, y, text, ha="center", va="center", fontsize=fs, bbox=style,
            zorder=3, linespacing=1.25)


def arrow(ax, x1, y1, x2, y2, style="-|>", rad=0.0, lw=0.8):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
                                 mutation_scale=7, linewidth=lw, color="black",
                                 connectionstyle=f"arc3,rad={rad}", zorder=2,
                                 shrinkA=1, shrinkB=1))


def lane(ax, y, label, x0=0.3, x1=9.7):
    ax.plot([x0, x1], [y, y], color="0.6", lw=0.6, ls=":")
    ax.text(x0 - 0.15, y - 0.36, label, fontsize=9.6, style="italic",
            weight="bold", ha="left")


# ----------------------------------------------------------------------
# Fig. 1 - pipeline: dual-write ingestion, fused retrieval, typed
# component selection, fail-closed validation, registry render
# ----------------------------------------------------------------------
def fig_arch(path: str) -> None:
    fig, ax = plt.subplots(figsize=(COL_W, 4.15))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 13.6)
    ax.axis("off")

    ax.text(0.15, 13.25, "ingestion", fontsize=9.6, style="italic",
            weight="bold", ha="left")
    box(ax, 5.0, 12.5, "learner's documents (any discipline)", fs=6.2)
    box(ax, 2.55, 11.0, "parse, chunk,\nembed", fs=6.2)
    box(ax, 7.45, 11.0, "schema-free entity\nand relation extraction", fs=6.0)
    arrow(ax, 4.2, 12.15, 2.75, 11.6)
    arrow(ax, 5.8, 12.15, 7.25, 11.6)
    box(ax, 2.55, 9.35, "vector index", STORE, fs=6.2)
    box(ax, 7.45, 9.35, "knowledge graph", STORE, fs=6.2)
    arrow(ax, 2.55, 10.45, 2.55, 9.85)
    arrow(ax, 7.45, 10.45, 7.45, 9.85)
    ax.text(5.0, 10.1, "dual write", fontsize=8.1, style="italic", ha="center")

    lane(ax, 8.5, "retrieval")

    box(ax, 1.5, 7.0, "dense\nvector", fs=6.0)
    box(ax, 5.0, 7.0, "BM25", fs=6.0)
    box(ax, 8.5, 7.0, "graph\ntraversal", fs=6.0)
    arrow(ax, 2.4, 8.85, 1.6, 7.7, lw=0.7)
    arrow(ax, 7.6, 8.85, 8.4, 7.7, lw=0.7)
    box(ax, 5.0, 5.4, "reciprocal rank fusion", fs=6.2)
    for x in (1.5, 5.0, 8.5):
        arrow(ax, x, 6.4, 5.0, 5.95)

    lane(ax, 4.6, "generative interface")

    box(ax, 5.0, 3.2, "component selection and\ntyped payload from evidence",
        fs=6.0)
    arrow(ax, 5.0, 4.9, 5.0, 3.85)
    box(ax, 5.0, 1.75, "schema validation,\nfail closed", GATE, fs=6.2)
    arrow(ax, 5.0, 2.6, 5.0, 2.35)
    box(ax, 5.0, 0.45, "component registry", fs=6.2)
    arrow(ax, 5.0, 1.15, 5.0, 0.9)

    ax.text(9.75, 3.2, "no markup\nis emitted", fontsize=7.8, style="italic",
            ha="right", va="center", linespacing=1.2)
    ax.text(9.75, 1.75, "unregistered or\ninvalid block\nnever renders",
            fontsize=7.8, style="italic", ha="right", va="center",
            linespacing=1.2)

    fig.tight_layout(pad=0.15)
    fig.savefig(path, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)


# ----------------------------------------------------------------------
# Fig. 2 - retrieval structure bounds interface expressiveness
# ----------------------------------------------------------------------
def fig_bound(path: str) -> None:
    fig, ax = plt.subplots(figsize=(COL_W, 2.55))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.4)
    ax.axis("off")

    ax.text(0.1, 7.1, "flat retrieval", fontsize=9.9, style="italic",
            weight="bold", ha="left")
    box(ax, 1.2, 5.6, "query", fs=6.2)
    for y in (6.5, 5.6, 4.7):
        box(ax, 4.3, y, "passage", fs=6.2)
        arrow(ax, 1.95, 5.6, 3.62, y)
    box(ax, 8.0, 5.6, "prose with\ncitations", OUT, fs=6.2)
    for y, ty in ((6.5, 5.9), (5.6, 5.6), (4.7, 5.3)):
        arrow(ax, 5.0, y, 7.02, ty)
    ax.text(5.0, 3.85, "scored independently: no relation is representable",
            ha="center", fontsize=8.3, style="italic")

    ax.plot([0.2, 9.8], [3.3, 3.3], color="0.6", linewidth=0.6, linestyle=":")

    ax.text(0.1, 2.95, "graph-native retrieval", fontsize=9.9, style="italic",
            weight="bold", ha="left")
    box(ax, 1.2, 1.6, "query", fs=6.2)
    circ = dict(boxstyle="circle,pad=0.28", linewidth=0.8, edgecolor="black",
                facecolor="white")
    ax.text(3.9, 2.35, "A", fontsize=9.3, ha="center", va="center", zorder=3,
            bbox=circ)
    ax.text(5.6, 2.55, "B", fontsize=9.3, ha="center", va="center", zorder=3,
            bbox=circ)
    ax.text(4.6, 1.15, "C", fontsize=9.3, ha="center", va="center", zorder=3,
            bbox=circ)
    arrow(ax, 1.95, 1.7, 3.55, 2.25)
    ax.plot([4.25, 5.25], [2.42, 2.52], color="black", linewidth=0.8, zorder=1)
    ax.plot([3.85, 4.5], [2.0, 1.5], color="black", linewidth=0.8, zorder=1)
    ax.text(4.95, 2.86, "cites", fontsize=7.8, style="italic", ha="center")
    ax.text(4.12, 1.72, "contradicts", fontsize=7.8, style="italic",
            ha="right", va="center")
    box(ax, 8.0, 1.9, "structured\ncomponents", OUT, fs=6.2)
    arrow(ax, 6.05, 2.5, 7.0, 2.05)
    arrow(ax, 5.05, 1.2, 7.0, 1.7)
    ax.text(5.0, 0.25,
            "entities and labelled relations across documents:\n"
            "a component's precondition can be satisfied",
            ha="center", fontsize=8.3, style="italic", linespacing=1.25)

    fig.tight_layout(pad=0.15)
    fig.savefig(path, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)


# ----------------------------------------------------------------------
# Fig. 3 - the life of one block: what must hold before a learner sees it
# ----------------------------------------------------------------------
def fig_block(path: str) -> None:
    fig, ax = plt.subplots(figsize=(COL_W, 2.4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6.6)
    ax.axis("off")

    xs = [1.15, 3.35, 5.55, 7.75]
    labels = ["evidence\nretrieved", "component\nchosen", "payload\nbuilt",
              "claims\nchecked"]
    for x, t in zip(xs, labels):
        box(ax, x, 5.15, t, fs=5.9)
    for i in range(len(xs) - 1):
        arrow(ax, xs[i] + 0.75, 5.15, xs[i + 1] - 0.75, 5.15)

    box(ax, 9.35, 5.15, "schema\nvalidation", GATE, fs=5.9)
    arrow(ax, 8.5, 5.15, 8.85, 5.15)

    ax.text(5.0, 3.55, "one shared schema generates both sides of the wire",
            ha="center", fontsize=8.4, style="italic")
    ax.text(5.0, 2.95, "rendered through the registry as one of:", ha="center",
            fontsize=8.4, style="italic")

    for x, t in zip([1.5, 3.83, 6.17, 8.5],
                    ["empty", "loading", "partial", "error"]):
        box(ax, x, 2.0, t, OUT, fs=5.9)
    ax.text(5.0, 0.75, "every component implements all four states, so a\n"
                       "failing or streaming block degrades visibly",
            ha="center", fontsize=8.3, style="italic", linespacing=1.25)

    fig.tight_layout(pad=0.15)
    fig.savefig(path, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig_arch("fig1_arch.png")
    fig_bound("fig2_bound.png")
    fig_block("fig3_block.png")
    print("wrote fig1_arch.png, fig2_bound.png, fig3_block.png")
