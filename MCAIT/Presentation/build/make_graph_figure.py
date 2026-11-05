"""Draws assets/knowledge-graph.png from the stored Arcana graph over the 16 evaluation papers.

Only real nodes and edges are drawn. It shows the concepts found in the most papers and the edges
among them, which is where documents connect. Prints the figures quoted on the slide.
"""
import collections
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx

GRAPH = Path(r"C:\Users\User\Documents\FYP DOCS\Arcana-v2\data\eval-live-live\graph.json")
OUT = Path(__file__).resolve().parent / "assets" / "knowledge-graph.png"
NAVY, GOLD, CYAN, RULE, INK = "#071E44", "#DBAC48", "#1577B5", "#CBD3DF", "#1B2A41"
TOP_NODES = 70
LABELS = 9

def close(a, b):
    return abs(a[0] - b[0]) < 0.42 and abs(a[1] - b[1]) < 0.16


data = json.load(open(GRAPH, encoding="utf-8"))
nodes = {n["id"]: n for n in data["nodes"]}
docs = {d for n in nodes.values() for d in n.get("doc_ids", [])}
multi = sum(1 for n in nodes.values() if len(set(n.get("doc_ids", []))) >= 2)
print(f"nodes {len(nodes)} edges {len(data['edges'])} papers {len(docs)} in-2+-papers {multi} ({multi / len(nodes):.1%})")

top = sorted(nodes, key=lambda k: (len(set(nodes[k].get("doc_ids", []))), len(nodes[k].get("chunk_ids", []))), reverse=True)[:TOP_NODES]
keep = set(top)
g = nx.Graph()
g.add_nodes_from(top)
weights = collections.Counter()
for e in data["edges"]:
    a, b = e["source"], e["target"]
    if a in keep and b in keep and a != b:
        weights[tuple(sorted((a, b)))] += 1
g.add_edges_from(weights)
g = g.subgraph(max(nx.connected_components(g), key=len)).copy()
print("drawn nodes", g.number_of_nodes(), "drawn edges", g.number_of_edges())

pos = nx.kamada_kawai_layout(g)
span = {n: len(set(nodes[n].get("doc_ids", []))) for n in g.nodes}
fig, ax = plt.subplots(figsize=(6.0, 3.65), dpi=300)
nx.draw_networkx_edges(g, pos, ax=ax, edge_color=RULE, width=0.8)
colors = [NAVY if span[n] >= 12 else (CYAN if span[n] >= 8 else GOLD) for n in g.nodes]
sizes = [18 + span[n] ** 2 * 0.9 for n in g.nodes]
nx.draw_networkx_nodes(g, pos, ax=ax, node_color=colors, node_size=sizes, linewidths=0.6, edgecolors="white")
chosen = []
for n in sorted(g.nodes, key=lambda n: (span[n], g.degree(n)), reverse=True):
    if not any(close(pos[n], pos[m]) for m in chosen) and len(chosen) < LABELS:
        chosen.append(n)
for n in chosen:
    x, y = pos[n]
    ax.annotate(nodes[n]["label"], (x, y), xytext=(0, 7 + span[n] * 0.35), textcoords="offset points", ha="center",
                fontsize=7.5, color=INK, fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.85))
for label, c in [("in 12+ papers", NAVY), ("in 8 to 11 papers", CYAN), ("in fewer", GOLD)]:
    ax.scatter([], [], c=c, s=60, label=label)
ax.legend(loc="lower left", frameon=False, fontsize=8, labelcolor=INK)
ax.margins(0.08)
ax.axis("off")
fig.tight_layout(pad=0.2)
OUT.parent.mkdir(exist_ok=True)
fig.savefig(OUT, facecolor="white")
print("spans", collections.Counter(span.values()).most_common(8))
print("labels", [nodes[n]["label"] for n in chosen])
