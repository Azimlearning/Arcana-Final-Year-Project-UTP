---
tags: [concept, superseded]
source: concept/FYP_Context_Document.md §4
supersededBy: Arcana/docs/arcana_prd.md §8 "Locked tech stack"
---

# Tech Stack — Early Planning Version (superseded)

> **This is a historical planning snapshot.** For the authoritative, current stack, see `Arcana/docs/arcana_prd.md` §8 — that file is the live source of truth and changes as the build progresses (per `Arcana/CLAUDE.md`'s order-of-authority rule). This note is kept only to show how the thinking evolved.

Early version (this planning session): Next.js 14 + Tailwind + Framer Motion (frontend), LangGraph (orchestration), Claude API primary / OpenRouter fallback (LLM), Neo4j Community / NetworkX (graph), Pinecone (vectors), OpenAI text-embedding-3-large (embeddings), FastAPI (backend), Firebase Firestore + Auth.

Largely consistent with the later PRD-locked stack, with one notable difference: this early version scoped **6 agents**; the PRD expanded this to **25 agents across 4 tiers** (P0–P2 phased) — see [[AgentSuite-Early-Superseded]].
