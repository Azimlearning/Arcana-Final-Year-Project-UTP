# Where each number and claim comes from

Private record for checking the decks. Not part of the slides. Arcana paths are relative to `FYP DOCS/Arcana-v2/`. Slide numbers in the first table are from the first build of `179.pptx`; find the claim by name, since slides have moved.

| Slide | Figure or claim | Source | Checked against |
|---|---|---|---|
| 3 | d = 0.83, 20 physics studies | `Paper/latex/main.tex`, Section I, ref [5] | Paper |
| 6 | Gemini Notebook: outputs from user-provided sources, Studio outputs | support.google.com/notebooklm/answer/16206563, /16212283 | Fetched 1 Nov 2026 |
| 6 | ChatGPT Intelligent UI: chooses the format automatically | OpenAI release notes, 7 Oct 2026, as recorded in `Synapse-V4/refdocs/evidence/2026-10-21-chatgpt-intelligent-ui-rea.md` | Earlier record. OpenAI's pages returned 403 on 1 Nov; press search agrees |
| 6 | Dynamic view: designs and codes per prompt, HTML/CSS/JS | research.google/blog/generative-ui-a-rich-custom-visual-interactive-user-experience-for-any-prompt | Fetched 1 Nov 2026 |
| 11 | 24 of 24 components, 645 tests | `Paper/latex/main.tex`, Section VI-E | Paper |
| 14 | Pilot table, 18 of 20, p = 1.0, 15 of 20, 4 of 16, 796 and 859 | `Paper/latex/main.tex`, Table V, Section VI-C | Paper |
| 15 | VERA design facts | `FYP DOCS/Concept-Notes/ExtendsVERA-Comparison.md`, `VERA-AI-PriorWork.md` | Azim's notes. The evaluation row and pilot figures were left off |
| 16 | Real-model screens | `refdocs/evidence/p2-d1-14`, `p2-d1-15`, `p2-d1-17` | Evidence screenshots |
| 16 | Learning tools with no model call | Scratch copy of `data/m2/atomic2-full-vault1`, fake mode, spend ledger 0 rows | Recorded 1 Nov 2026 |
| 16 | The lab's function is a test fixture | `api/labs/generator.py`, `FakeLabGenerator` | Code |
| 17 | 11,173 nodes, 13,972 edges, 1,294 in 2+ papers (11.6%) | `data/eval-live-live/graph.json` | Recomputed by `build/make_graph_figure.py` |
| 17 | About a third of edges stated in one sentence | `refdocs/STATUS.md`, verification ledger, G1.1: 34.6 percent | Status file |
| 18 | Original 19, new 19, pooled rows | `eval/results/20261014T192628Z-extension-pooled.json`, H2 nDCG pairs | Raw file |
| 19 | Admission counts | `eval/results/20261006T184643Z-bound.json`, `summary.per_layer` | Raw file |
| 20 | 38 of 38, control refused, precision 0.2088, recall 0.2146 | `eval/results/20261015T123511Z-grounding-live.json`, `summary` | Raw file |
| 20 | 125 of 125, 10 of 140, 19 of 38 | `refdocs/evidence/20261015-grounding-live.md` | Evidence record |
| Q&A | 0.86, 0.58, 30 of 100 | `refdocs/evidence/README.md`, link audit row | Evidence index |

## Added for the deeper deck and the two new slides

| Where | Figure or claim | Source | Checked against |
|---|---|---|---|
| Ingestion video | Sentences and edges: BM25 performs_best_on FEVER, BM25 captures lexical signals, HyDE outperforms BM25 | `data/eval-live-live/graph.json` and `arcana.db`, via `build/motion/extract_data.py` | Raw store |
| Traversal video | Four seeds, 74 edges, top-10 routes, 3 of 10 gold-relevant | `eval/results/20261006T093813Z-benchmark.json`, `20261007T012421Z-traversal-admission.json` | Raw files |
| Fusion video | Ranks, RRF scores, nDCG 0.242 and 0.594 | Same benchmark file; scores recomputed at k = 60 and consistent with the stored order apart from ties | Recomputed |
| Traversal card | 111 seeds, 37% approximate, 16-755 edges, 87% and 13% | `refdocs/evidence/20261007T012421Z-traversal-admission.md` | Evidence record |
| Graph statistics | 9,821, 4,830, 20.4%, 1,604, hubs | `refdocs/evidence/20261007T005311Z-graph-quality-baseline.md` | Evidence record |
| Trace slide | q-cross-01 steps, 11.08 s, $0.0199, routing 29/9/1, seven combinations | `eval/results/20261015T123511Z-grounding-live.json` | Raw file |
| Per-question chart | 38 differences, 9/14/15, category means | `data.json` from the benchmark and extension files | Raw files |
| What did not hold up | Depth, scale, re-ranker, atomic graph | `refdocs/evidence/20261015-question-set-extension.md`, `20261007T131202Z-m2-look3-scale.md`, `20261014-p3-rerank` row of the index, `20261014-m2-look5-full-corpus.md` | Evidence records |
| Checker slide | Planted-defect counts | `eval/results/mutation-factcheck.json`; `STATUS.md` ledger for 50/50 and 0/50 | Raw file |
| Lab card | 120 of 120 planted defects | `eval/results/20261007T173611Z-p4-lab-mutations.json` | Raw file |
| Cost slide | $5.81, $0.0037, 15 failures, $0.017, $0.045, 481 and 296 ms | `2026-10-06-live-ingestion-cost.json`, grounding record, benchmark summary | Raw files and record |
| Admission heat map | Per-question admission | `refdocs/evidence/20261006T184643Z-bound.md` | Evidence record |
| Personas | Aisha, Daniel, Mei | `FYP DOCS/Concept-Notes/PRD-Personas.md` | Azim's notes |
| Adaptive slide | Combinatorial in n and k, workspace reshapes, mode inferred | `Paper/latex/main.tex`, Section IV | Paper |
| Generated-lab slide | 219 of 224, 0 of 30, 20 of 20, 13 of 14 | `Synapse-V4/refdocs/changelog/CHANGELOG.md` line 117, `refdocs/evidence/2026-10-28-w16-paid-measurement.md` | Changelog and record |
| Grid on the graph slide | Quotes and pages, shortened | `refdocs/evidence/p2-d1-14-live-comparison-grid-after-fix.png` | Screenshot |
