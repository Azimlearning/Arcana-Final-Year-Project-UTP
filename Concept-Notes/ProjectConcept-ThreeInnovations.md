---
tags: [concept, static]
source: concept/FYP_Context_Document.md §3
---

# Project Concept — The Three Core Innovations

**One-line description:** A research assistant where documents are stored not as isolated vector chunks but as an interconnected knowledge graph, queried by a hybrid graph+vector RAG pipeline, served through composable specialised agents, with a layout that adapts to how each user thinks.

**Core inspiration:** Google NotebookLM (3-panel docs/chat/agent UI pattern — extend it) + Obsidian (vault-style knowledge graph — the storage model to implement).

**The problem:** existing RAG tools treat documents as isolated flat silos — can't recognise cross-document entity equivalence, relationships/contradictions are invisible to the retriever, agents can't delegate to each other, static interfaces don't adapt to task.

**Three core innovations:**
1. **Graph-Native RAG** — entity KG (Neo4j/NetworkX); retrieval = graph traversal + dense vector (3072-dim) + BM25, merged via RRF.
2. **Composable Multi-Agent Pipeline** — LangGraph orchestration, agents invoke each other as tools (this early version: 6 agents; superseded by the 25-agent suite in the PRD — see [[AgentSuite-Early-Superseded]]).
3. **Adaptive UI** — 3-panel layout with task-mode switching (Research/Writing/Study), layout memory persists across sessions.
