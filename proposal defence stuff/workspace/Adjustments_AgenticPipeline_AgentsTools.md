# Adjustments — Agentic Pipeline & Agents and Tools Slides

Two slides changed this round, both grounded directly in `Arcana/docs/arcana_prd.md` §12.
Full backing reference (all 25 agents, GenUI catalog, GraphRAG mechanics) is in
`Agentic_Pipeline_PRD_Detail.md` — this file is just the two finalized, copy-paste-ready slides.

---

## 1. AGENTIC PIPELINE — rewritten with PRD-level detail

**What changed:** the original 4 bullets covered only the composability mechanism. Now expanded to
also cover the full agent roster, GraphRAG, and GenUI, per your request. Recommended as a **2x2 grid
layout** (4 labelled quadrants), not a flat bullet list, since each quadrant is dense on its own.

**Title:** AGENTIC PIPELINE

**Quadrant 1 — Mechanism:**
AgentState is the single shared ledger, every agent appends its contribution and nothing overwrites another agent's output; agents compose only through route_to_agent, which enforces a hop budget and a per-turn token budget, never direct module imports; intent-scoped tool injection caps every agent at max_tools_per_prompt = 12.

**Quadrant 2 — Agent Roster (25 agents, 4 tiers):**
Orchestration (Orchestrator) → Core Intelligence (Research, Graph, Learning, Writing, Socratic Tutor, Discovery, Methodology, Debate) → Output Generation (UI Agent, Citation, Visual, Document, Audio) → Quality & Meta (Fact Checker, Annotation, Memory, Ingestion, Web Search, Study Planner, Analytics, Plagiarism, Grammar & Style, Paraphrase, Export). 15+ confirmed built across P0/P1; the remainder scoped P2.

**Quadrant 3 — GraphRAG at the core:**
Every Research/Learning/Socratic/Discovery task routes through the Graph Agent (Louvain community detection, PageRank, shortest path) and the hybrid retrieval pipeline (dense vector + BM25 + graph traversal, fused via Reciprocal Rank Fusion); this is what makes the suite graph-native rather than a flat-RAG wrapper.

**Quadrant 4 — GenUI termination:**
Every path ends at the UI Agent, the only agent that selects from the 24-component catalog and emits a typed UIBlock {type, data, meta}, streamed over SSE and rendered via the component registry into the adaptive 3-panel dashboard.

**Footer:** 2026 | Universiti Teknologi PETRONAS

---

## 2. AGENTS & TOOLS — corrected

**What changed:** the previous version named "literature, contradiction, comparator, timeline" as
standalone agents. None of those exist in the PRD's 25-agent roster — they're tool *methods* on other
agents (`cross_document_compare` / `detect_contradictions` on Research, `build_literature_review` on
Writing, `render_timeline` on Visual). Replaced with the actual confirmed-built agents.

**Title:** AGENTS & TOOLS

**Body (5 bullets):**
1. Target suite: 25 agents across 4 tiers (Orchestration 1, Core Intelligence 8, Output Generation 5, Quality & Meta 11).
2. Checklist-confirmed built (P0/P1): Orchestrator, Research, Graph, Learning, Writing, Socratic Tutor, Discovery, Ingestion.
3. Also confirmed built: UI Agent, Citation, Visual, Document (Output tier); Fact Checker, Annotation, Memory, Web Search, Study Planner, Analytics (Quality & Meta tier).
4. Deferred to P2: Methodology, Debate, Audio, Plagiarism, Grammar & Style, Paraphrase, Export.
5. Every agent follows one template: subclass BaseAgent, expose tools via @tool, read AgentState without mutating upstream slots, and never emit raw HTML or pick UI components.

**Footer:** 2026 | Universiti Teknologi PETRONAS
