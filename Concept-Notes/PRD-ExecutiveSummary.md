---
tags: [concept, prd-static]
source: Arcana/docs/arcana_prd.md §2
---

# PRD — Executive Summary (stable)

Arcana is a graph-native, multi-agent research and learning platform for students and academic researchers. Ingests documents (papers, reports, notes, web pages) into a single connected knowledge base that can be queried, studied from, and written against.

**The problem:** current RAG assistants (incl. NotebookLM) treat each document as an isolated silo; can't answer cross-source questions; agents can't collaborate; interface doesn't adapt to task.

**The product bet — three things, used together:**
1. A knowledge graph makes cross-document relationships (agreement, contradiction, influence) first-class and retrievable.
2. A composable multi-agent system lets specialised agents invoke one another for autonomous task decomposition.
3. A Generative UI assembles the interface per request from typed components.

**Why credible:** extends [[VERA-AI-PriorWork|VERA AI]] (94% citation accuracy, 95% retrieval-time cut over a 7-month industrial placement).

This is the stable "why" — for current phase/build status see `Arcana/docs/checklist.md` (not duplicated here; it changes too often).
