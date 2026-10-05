---
tags: [concept, admin, static]
source: concept/FYP_Context_Document.md §10
---

# FORM 01A Content (UTP FYP Title Proposal)

Doc ref: UTP-ACA-PROG-FYP-01.01a, Version 7.0, Jan 2025.

**Project title:** GraphRAG-Powered Multi-Agent Research and Learning Intelligence Platform
**Proposer:** Fakhrul Azim Bin Ahmed Mardzukie · Bachelor of Computer Science (Hons)

**Problem statement:** Current RAG systems (incl. NotebookLM) treat documents as isolated, independently indexed chunks, preventing recognition of cross-document concept relationships and forcing manual cross-referencing. Static, general-purpose interfaces don't adapt to research/writing/study workflows — resulting in inefficient retrieval, fragmented workflows, and poor personalised-learning support.

**Objectives:** (1) graph-native hybrid RAG pipeline (KG traversal + dense vector + BM25 + RRF) evaluated against a flat vector RAG baseline; (2) composable multi-agent orchestration (LangGraph) with A2A invocation across Research/Learning/Writing/Graph/Annotation/Insight agents; (3) adaptive UI with task-mode switching (Research/Writing/Study).

**Pre-requisites:** RAG, LLM API integration, graph database concepts, Python (FastAPI, LangGraph), Next.js 14, vector embeddings/similarity search.

**Tools/equipment:** Next.js 14, Tailwind, Framer Motion, FastAPI, LangGraph, Claude API/OpenRouter, OpenAI text-embedding-3-large, Pinecone, Neo4j/NetworkX, Firebase Firestore+Auth, GitHub, VS Code/Cursor.
