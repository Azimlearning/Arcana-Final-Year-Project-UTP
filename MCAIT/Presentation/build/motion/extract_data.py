"""Reads real evaluation data for the worked-example videos and charts. Read only; no model calls.

Run with the Arcana environment from its repo root, so eval.metrics and yaml resolve:
  .venv/Scripts/python.exe <this file>
"""
import collections
import json
import re
import sqlite3
import sys
from pathlib import Path

A = Path(r"C:\Users\User\Documents\FYP DOCS\Arcana-v2")
sys.path.insert(0, str(A))
from eval.metrics import is_relevant, load_gold  # noqa: E402

OUT = Path(__file__).resolve().parent / "data.json"
R = A / "eval" / "results"
QID = "q-cross-06"
L = lambda n: json.load(open(R / n, encoding="utf-8"))

b = L("20261006T093813Z-benchmark.json")
ext = L("20261014T191800Z-ext-benchmark.json")
res = next(r for r in b["results"] if r["question_id"] == QID)
gold = load_gold(A / "eval" / "gold", QID)
db = sqlite3.connect(A / "data" / "eval-live-live" / "arcana.db")
docs = {d: t for d, t in db.execute("select id, title from documents")} if False else {}
cols = [c[1] for c in db.execute("pragma table_info(documents)")]
print("document columns", cols)
name_col = next(c for c in ("title", "filename", "name") if c in cols)
docs = {d: t for d, t in db.execute(f"select id, {name_col} from documents")}
chunks = {i: (d, p, t) for i, d, p, t in db.execute("select id, doc_id, page, text from chunks")}
all_texts = [t for _, _, t in chunks.values()]


def short(doc):
    t = docs.get(doc, doc)
    m = re.match(r"(\d{4}\.\d{5})", t)
    return (m.group(1) if m else "") + " " + re.sub(r"^\d{4}\.\d{5}(v\d)?_?", "", t).replace("_", " ")[:48]


def info(cid):
    d, p, t = chunks[cid]
    return {"id": cid, "doc": short(d), "page": p, "relevant": is_relevant(t, gold), "text": t}


arms = {k: res["arms"][k]["chunk_ids"] for k in ("dense", "sparse", "graph", "flat", "hybrid")}
RRF_K = 60
scores = collections.defaultdict(float)
parts = collections.defaultdict(dict)
for arm in ("dense", "sparse", "graph"):
    for rank, cid in enumerate(arms[arm], 1):
        scores[cid] += 1 / (RRF_K + rank)
        parts[cid][arm] = rank
mine = sorted(scores, key=lambda c: (-scores[c]))
print("stored hybrid", arms["hybrid"][:10] == mine[:10], "overlap", len(set(arms["hybrid"]) & set(mine[:10])))

fusion = []
for i, cid in enumerate(arms["hybrid"], 1):
    x = info(cid)
    fusion.append({"rank": i, "doc": x["doc"], "page": x["page"], "relevant": x["relevant"], "dense": parts[cid].get("dense"),
                   "sparse": parts[cid].get("sparse"), "graph": parts[cid].get("graph"), "score": round(scores[cid], 5), "in_flat": cid in arms["flat"]})
for f in fusion:
    print(f)

flat_rel = [info(c)["relevant"] for c in arms["flat"]]
hyb_rel = [info(c)["relevant"] for c in arms["hybrid"]]
print("flat relevant by rank", flat_rel)
print("hybrid relevant by rank", hyb_rel)

# ---- traversal
graph = json.load(open(A / "data" / "eval-live-live" / "graph.json", encoding="utf-8"))
nodes = {n["id"]: n for n in graph["nodes"]}
ents = res["arms"]["graph"]["resolution"]["entities"]
seeds = [{"id": e["node_id"], "label": nodes[e["node_id"]]["label"], "match": e["match"], "docs": len(set(nodes[e["node_id"]].get("doc_ids", []))),
          "chunks": len(nodes[e["node_id"]].get("chunk_ids", []))} for e in ents]
sid = {s["id"] for s in seeds}
followed = [e for e in graph["edges"] if e["source"] in sid or e["target"] in sid]
print("seeds", seeds, "\nedges followed", len(followed), "resolution", {k: res["arms"]["graph"]["resolution"][k] for k in ("hit_rate", "n_exact", "n_approx")})
ta = next(r for r in L("20261007T012421Z-traversal-admission.json")["results"] if r["question_id"] == QID)
print("admission record", {k: ta[k] for k in ("seeds", "steps_followed", "steps_shown", "reached", "reached_via")})
SENT = re.compile(r"(?<=[.!?])\s+")
reach = []
for rank, cid in enumerate(arms["graph"], 1):
    x = info(cid)
    via = [s["label"] for s in seeds if cid in nodes[s["id"]].get("chunk_ids", [])]
    reach.append({"rank": rank, "doc": x["doc"], "page": x["page"], "relevant": x["relevant"], "via": via})
    print(reach[-1])

# stated edges among seeds and neighbours on the reached chunks
def stated(e):
    t = chunks.get(e["chunk_id"], (None, None, ""))[2]
    a, b_ = nodes[e["source"]]["label"].lower(), nodes[e["target"]]["label"].lower()
    for s in SENT.split(t):
        low = s.lower()
        if a in low and b_ in low and 30 < len(s) < 260:
            return " ".join(s.split())
    return None


GENERIC = {"authored", "author", "authored by", "author of", "related to", "mentions", "cites", "published in"}
samples = []
for e in followed:
    if e["relation"].lower() in GENERIC:
        continue
    sent = stated(e)
    if sent:
        d, p, _ = chunks[e["chunk_id"]]
        samples.append({"source": nodes[e["source"]]["label"], "relation": e["relation"], "target": nodes[e["target"]]["label"],
                        "doc": short(d), "page": p, "sentence": sent, "reached": e["chunk_id"] in arms["graph"], "chunk": e["chunk_id"]})
print("stated samples", len(samples))
for s in sorted(samples, key=lambda s: (not s["reached"], len(s["sentence"])))[:24]:
    print(s["source"], "--", s["relation"], "->", s["target"], "|", s["doc"], s["page"], "|", s["reached"], "|", s["sentence"][:170])

# ---- per-question and per-category
pq = []
for src, tag in ((b, "original"), (ext, "new")):
    for r in src["results"]:
        if "flat" in r["arms"] and r["arms"]["flat"]["ndcg_at_10"] is not None:
            pq.append({"q": r["question_id"], "set": tag, "cat": r["category"], "flat": r["arms"]["flat"]["ndcg_at_10"], "hybrid": r["arms"]["hybrid"]["ndcg_at_10"],
                       "dense": r["arms"]["dense"]["ndcg_at_10"], "sparse": r["arms"]["sparse"]["ndcg_at_10"], "graph": r["arms"]["graph"]["ndcg_at_10"]})
print("per question", len(pq))
cats = collections.defaultdict(lambda: collections.defaultdict(list))
for p in pq:
    for a in ("dense", "sparse", "graph", "flat", "hybrid"):
        cats[(p["set"], p["cat"])][a].append(p[a])
cat_means = {f"{k[0]}|{k[1]}": {a: round(sum(v) / len(v), 3) for a, v in d.items()} | {"n": len(d["flat"])} for k, d in cats.items()}
print(json.dumps(cat_means, indent=0))

top = {}
for f, cid in zip(fusion, arms["hybrid"]):
    if f["relevant"]:
        top[f["rank"]] = " ".join(chunks[cid][2].split())
        print("RELEVANT rank", f["rank"], f["doc"], "p", f["page"], top[f["rank"]][:700])
json.dump({"question": "How do the papers compare BM25 with dense vector retrieval in terms of complementarity? What does each method capture that the other misses?", "relevant_text": top, "qid": QID, "fusion": fusion, "seeds": seeds, "followed": len(followed), "reach": reach,
           "samples": samples[:200], "per_question": pq, "cat_means": cat_means, "flat_rel": flat_rel, "hyb_rel": hyb_rel,
           "summary": b["summary"]["per_arm"], "ext_summary": ext["summary"]["per_arm"]}, open(OUT, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("written", OUT)
