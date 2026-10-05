---
tags: [concept, prd-static]
source: Arcana/docs/arcana_prd.md §4
---

# PRD — Goals, Non-Goals, Success Metrics (stable)

**Product goals:** make cross-document relationships retrievable; enable autonomous multi-step task completion via agent-to-agent invocation; adapt the interface to the current task; help users learn/retain, not just find, information; empirically demonstrate graph-augmented retrieval beats flat vector RAG for cross-document questions.

**Non-goals (this release):** real-time multi-user collaboration; native mobile app; local/offline LLM inference; video generation/animated explainers; general-purpose web search (limited to academic paper discovery).

**Success metrics:**

| Metric | Target |
|---|---|
| Cross-document retrieval accuracy (PRIMARY) | Statistically significant improvement over flat-vector baseline |
| Citation accuracy | ≥ 90% |
| Task completion rate | ≥ 80% without facilitator intervention |
| Usability (SUS) | ≥ 70 (good) |
| Time-to-insight | Meaningful reduction vs manual/NotebookLM |
| Activation | ≥ 90% reach first grounded answer in session one |
| Retrieval latency | < 3s to first streamed token |

The primary metric is deliberately academic: the FYP is graded on a defensible contribution, and a rigorous retrieval benchmark is the strongest evidence available.
