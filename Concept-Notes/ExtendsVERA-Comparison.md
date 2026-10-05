---
tags: [concept, static]
source: concept/FYP_Context_Document.md §3 (comparison table)
---

# How Arcana Extends VERA AI

| Dimension | VERA AI (Internship) | FYP Project (Arcana) |
|---|---|---|
| Knowledge storage | Flat vector chunks per document, isolated silos | Graph-native: entity nodes + relationship edges across all documents |
| Retrieval method | BM25 + Vector + RRF (2-way hybrid) | Graph traversal + Vector + BM25 + RRF (3-way hybrid) |
| Agent architecture | 6 fixed, independent agents | Composable LangGraph pipeline; agents invoke each other as tools |
| UI adaptivity | Static 3-panel layout | Task-mode adaptive layout (Research/Writing/Study) |
| User context | Session-scoped only | Persistent graph + interaction history across sessions |
| Target domain | PETRONAS Upstream (enterprise) | Academic research and learning (student users) |
| Evaluation | Operational pilot (14 weeks) | Quantitative benchmark + structured user study |

See [[VERA-AI-PriorWork]] for the baseline this table compares against.
