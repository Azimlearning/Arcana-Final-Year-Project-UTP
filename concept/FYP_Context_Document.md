# FYP Planning Session — Full Context Document

> **Purpose:** This document contains the complete context, decisions, outputs, and research from a planning session for a Final Year Project (FYP). Use this to continue planning with any AI assistant.

---

## 1. Student Profile

| Field | Details |
|---|---|
| **Name** | Fakhrul Azim Bin Ahmed Mardzukie |
| **University** | Universiti Teknologi PETRONAS (UTP) |
| **Programme** | Bachelor of Computer Science (Hons) |
| **Graduation** | December 2025 |
| **Internship** | PETRONAS Upstream, BPI Unit — Digital Transformation & Business Performance Intern (May–December 2025) |
| **GitHub** | Azimlearning |
| **FYP Semester** | Semester 1, Academic Year 2025/2026 (starting next semester after internship) |

### Technical Background
- Frontend: Next.js 14, React, Tailwind CSS, Framer Motion, Vue.js, HTML/CSS/JS
- Backend: FastAPI (Python), Node.js, Firebase (Firestore, Auth, Cloud Functions)
- AI/ML: LangGraph, CrewAI, Claude API, OpenRouter, Pinecone, Python, PyTorch
- Other: Neo4j, NetworkX, MongoDB, MySQL, C++, Java
- CS Specialisations: AI/ML, Computer Vision

### Relevant Prior Projects
- **VERA AI** (Internship @ PETRONAS BPI) — RAG-powered enterprise knowledge assistant (see Section 2)
- **Buildora** (UMHackathon 2026) — AI construction project management using LangGraph, GLM architecture, Firebase
- **Pasar** (PutraHack 2026) — Hyperlocal farmer-to-consumer marketplace, FastAPI + sklearn
- **OnlyVolunteer** (KitaHack 2026) — Flutter Web + Firebase + Gemini volunteer-matching platform
- **Crowed-View-AI** — YOLOv8 seat occupancy tracker (computer vision)

---

## 2. Internship Project: VERA AI

### Overview
VERA AI is an enterprise-grade, RAG-powered intelligent knowledge base assistant platform developed for PETRONAS Upstream during the student's 7-month SIP at the BPI Unit.

### Key Results (14-week pilot)
- Knowledge retrieval time: reduced from 15–30 minutes to under 5 seconds (**95% efficiency gain**)
- Content creation turnaround: **90% reduction**
- Chatbot citation accuracy: **94%**
- User acceptance of AI-generated content: **82% first-pass**
- Image generation: **100% processed locally** (privacy)

### Tech Stack
| Layer | Technology |
|---|---|
| Frontend | Next.js 14 (App Router), Tailwind CSS, Framer Motion, Recharts |
| Backend | Firebase (Firestore, Storage, Cloud Functions, Auth) |
| AI (Cloud) | Google Gemini API, OpenRouter |
| AI (Local) | Python, PyTorch, Stable Diffusion v1.4 |
| Embeddings | OpenAI text-embedding-3-large (3,072 dimensions) |

### Architecture
- **Hub-and-Spoke topology** — central web interface orchestrates multiple AI services
- **Hybrid Inference Model** — cloud LLMs for text reasoning, local Stable Diffusion for image generation (data privacy)
- **"No Citation, No Answer" policy** — all chatbot responses grounded and attributed

### RAG Pipeline
1. Vector Search — cosine similarity on 3,072-dimensional embeddings
2. BM25 Keyword Search — exact term matching for technical jargon (e.g., PSC, FPSO)
3. Reciprocal Rank Fusion (RRF) — merges vector and keyword results
4. Adaptive Top-k — dynamically expands context window for complex queries

### Specialized Agents (6)
| Agent | Function |
|---|---|
| Analytics Agent | Predictive forecasting using linear regression and seasonal adjustment |
| Meetings Agent | Transcribes meeting notes into structured executive briefs |
| Podcast Agent | Converts KB topics into audio podcasts with AI-generated scripts |
| Content Agent | Drafts stories and narratives from raw submissions |
| Visual Agent | Analyzes images, auto-tags assets, generates infographics via local Stable Diffusion |
| Quiz Agent | Generates knowledge assessments from internal materials |

### StatsX Dashboard
- Linear Regression for baseline trend analysis
- Moving Averages for smoothing volatile data
- Seasonal Adjustment for weekly engagement patterns

### Project Lead
Fakhrul Azim Bin Ahmed Mardzukie — PETRONAS Upstream, BPI Unit — May 2026

---

## 3. FYP Project Concept

### Project Title (WIP — not finalised)
**Working titles considered:** NEXUS, GraphMind, Aether — all still under consideration. Student has not committed to a name yet.

### Subtitle
Graph-Native Multi-Agent Research and Learning Intelligence Platform

### One-Line Description
A research assistant where documents are stored not as isolated vector chunks but as an interconnected knowledge graph, queried by a hybrid graph+vector RAG pipeline, served through composable specialised agents, with a layout that adapts to how each user thinks.

### Core Inspiration
- **Google NotebookLM** — the concept of a left-panel (docs), middle-panel (chatbot), right-panel (AI/agent features) is the baseline UI pattern the student wants to extend
- **Obsidian** — the vault-style knowledge graph where information connects in a web is the storage model the student wants to implement
- Student wants to improve on NotebookLM specifically in: RAG quality, cross-document reasoning, agent specialisation, and UI adaptivity

### The Problem Being Solved
Existing RAG tools (including NotebookLM) treat documents as **isolated, flat silos**. Each document is chunked and embedded independently, so:
1. The system cannot recognise that "PSC agreement" in Doc A = "Production Sharing Contract" in Doc B
2. Relationships, contradictions, and thematic connections across sources are invisible to the retriever
3. Agents (where they exist) operate in isolation, can't delegate to each other
4. Static interfaces don't adapt to whether the user is researching, writing, or studying

### Three Core Innovations
1. **Graph-Native RAG (GraphRAG)** — Documents stored as an entity knowledge graph (Neo4j/NetworkX). Retrieval combines: graph traversal + dense vector search (3,072-dim) + BM25 keyword search, merged via Reciprocal Rank Fusion
2. **Composable Multi-Agent Pipeline** — LangGraph-based orchestration where 6 specialised agents can invoke each other as tools for complex multi-step tasks
3. **Adaptive UI** — 3-panel layout (Documents | Chat | Agents) with task-mode switching: Research Mode, Writing Mode, Study Mode. Layout memory persists across sessions.

### How It Extends VERA AI
| Dimension | VERA AI (Internship) | FYP Project |
|---|---|---|
| Knowledge Storage | Flat vector chunks per document, isolated silos | Graph-native: entity nodes + relationship edges across all documents |
| Retrieval Method | BM25 + Vector + RRF (2-way hybrid) | Graph traversal + Vector + BM25 + RRF (3-way hybrid with graph layer) |
| Agent Architecture | 6 fixed, independent agents | Composable LangGraph pipeline; agents can invoke other agents as tools |
| UI Adaptivity | Static 3-panel layout | Task-mode adaptive layout (Research / Writing / Study) |
| User Context | Session-scoped only | Persistent graph + interaction history across sessions |
| Target Domain | PETRONAS Upstream (enterprise) | Academic research and learning (student users) |
| Evaluation | Operational pilot (14 weeks) | Quantitative benchmark + structured user study |

---

## 4. Proposed Tech Stack

| Layer | Technology | Justification |
|---|---|---|
| Frontend | Next.js 14 (App Router), Tailwind CSS, Framer Motion | Proven in VERA AI; App Router enables server components |
| Agent Orchestration | LangGraph (Python) | Native multi-agent graphs with tool-calling; used in Buildora |
| LLM (Primary) | Claude API (claude-sonnet) | Superior instruction-following, long-context reasoning |
| LLM (Fallback) | OpenRouter | Model redundancy and flexibility |
| Knowledge Graph | Neo4j Community / NetworkX | Neo4j for production; NetworkX as lightweight prototype |
| Vector Store | Pinecone | High-dimensional support; used in existing FYP pipeline |
| Embeddings | OpenAI text-embedding-3-large (3,072-dim) | Same as VERA AI — enables fair comparison baseline |
| Backend API | FastAPI (Python) | Async-native; integrates with LangGraph and Python ML ecosystem |
| Database | Firebase Firestore | Managed NoSQL for metadata, user profiles, session context |
| Auth | Firebase Auth | Email/Google OAuth |

---

## 5. Specialised Agent Suite

| Agent | Primary Function | Key Outputs |
|---|---|---|
| Graph Agent | Traverses knowledge graph to surface hidden cross-document connections | Concept maps, entity chains, relationship summaries |
| Research Agent | Synthesises answers from multiple documents with cross-source citations | Cited research summaries, comparative analyses |
| Learning Agent | Identifies user knowledge gaps and generates adaptive study materials | Flashcards, quizzes, concept summaries |
| Writing Agent | Drafts structured documents grounded in the knowledge base | Literature reviews, outlines, technical reports |
| Annotation Agent | Ingests user highlights and notes back into the knowledge graph | Enriched graph nodes, personalised context |
| Insight Agent | Surfaces unexpected connections and detects contradictions across sources | Contradiction alerts, discovery cards |

---

## 6. Project Objectives

### Primary Objectives
1. Design and implement a graph-native hybrid RAG pipeline that outperforms standard vector-only RAG in cross-document retrieval accuracy
2. Develop a composable multi-agent orchestration system using LangGraph, enabling autonomous task decomposition across specialised agents
3. Build an adaptive UI with task-mode switching that dynamically reconfigures based on the user's current research or learning context

### Secondary Objectives
1. Evaluate retrieval quality against a standard flat RAG baseline and informally compare against Google NotebookLM
2. Implement persistent user context management (graph + interaction history across sessions)
3. Demonstrate applicability through a structured user study with student participants

---

## 7. Scope

### In Scope
- Text-based document ingestion: PDF, DOCX, web URLs
- Knowledge graph construction from extracted entities and relationships
- Hybrid RAG pipeline (Graph + Vector + BM25 + RRF)
- Minimum 3 fully functional agents with agent-to-agent tool invocation (for FYP 2 submission)
- Adaptive UI with minimum 2 task modes (Research and Study)
- Quantitative evaluation benchmarking retrieval quality vs flat RAG baseline
- User study: minimum 10–15 student participants

### Out of Scope
- Video/audio ingestion and transcription
- Real-time collaborative multi-user knowledge bases
- Mobile application development
- Local/offline LLM inference
- Integration with external academic databases (Semantic Scholar, arXiv API)

---

## 8. Preliminary Timeline

### FYP 1
| Weeks | Milestone |
|---|---|
| 1–3 | Literature review: GraphRAG, multi-agent LLMs, adaptive UI |
| 4–6 | System design, knowledge graph schema, architecture diagrams |
| 7–9 | Proof of concept: ingestion pipeline + graph construction + retrieval comparison demo |
| 10–12 | FYP 1 report writing and submission |

### FYP 2
| Weeks | Milestone |
|---|---|
| 1–4 | Full hybrid RAG pipeline (Graph + Vector + BM25 + RRF) |
| 5–8 | Agent suite (minimum 3 agents with composable tool-calling) |
| 9–11 | Adaptive UI + integration testing |
| 12–14 | User study execution, benchmark evaluation, results analysis |
| 15–16 | FYP 2 report finalisation and defence preparation |

---

## 9. LLM Council Assessment Summary

The project was run through a 5-advisor LLM council (Contrarian, First Principles, Expansionist, Outsider, Executor) with peer review. Key findings:

### Where All Advisors Agreed
- GraphRAG core is genuinely novel and academically defensible
- Scope is too wide as originally stated for a solo 2-semester developer
- Evaluation design is underdeveloped — needs to be first-class concern from day 1
- Entity extraction quality is the load-bearing technical risk

### Key Clashes & Resolutions
- **Scope (cut hard vs build all):** Resolution — build the tight version for the grade (3 agents, 2 UI modes, NetworkX for PoC); open-source as full vision post-graduation
- **Adaptive UI (contribution or distraction):** Resolution — keep it as implementation vehicle for user study, not a standalone research contribution
- **NotebookLM as benchmark:** Resolution — use self-built flat RAG as primary benchmark; NotebookLM as informal secondary comparison only

### Blind Spots Identified
- **Gold-standard evaluation dataset problem** — need 20 multi-document questions with known correct answers requiring cross-document reasoning. Must be designed in FYP 1, not after system is built
- **Supervisor expertise dependency** — framing of thesis contribution needs calibration to supervisor's background (NLP/AI vs Systems)
- **VERA AI baseline is underused** — not starting from zero; proven RAG frontend, deployment patterns, and 14-week enterprise pilot data already exist
- **NetworkX vs Neo4j trade-off** — use NetworkX for FYP 1 PoC; decide at FYP 2 start based on scale requirements

### Final Verdict
**Commit to the project, but restructure around one falsifiable claim:**
> *"Graph-augmented hybrid retrieval produces measurably superior cross-document reasoning compared to flat vector RAG in an academic research context."*

**The one thing to do first:** Draft 20 multi-document questions with known correct answers before writing a single line of code. This defines what "better" means and shapes every architecture decision.

---

## 10. FORM 01A Content (UTP Final Year Project Title Proposal)

The student confirmed they have the UTP Form 01A template (Doc Ref: UTP-ACA-PROG-FYP-01.01a, Version 7.0, Jan 2025). The following content was prepared for manual entry:

### Project Title
GraphRAG-Powered Multi-Agent Research and Learning Intelligence Platform

### Proposer's Name
Fakhrul Azim Bin Ahmed Mardzukie

### Area / Specialization
Bachelor of Computer Science (Hons)

### Problem Statement
Current Retrieval-Augmented Generation (RAG) systems used in research and learning tools — including commercial platforms such as Google NotebookLM — treat documents as isolated, independently indexed chunks. This flat storage model prevents the system from recognising relationships between concepts across different documents, forcing users to manually cross-reference and synthesise information. Additionally, existing AI research assistants offer single general-purpose chat interfaces with no specialised task support, and their static layouts do not adapt to the user's current workflow — whether researching, writing, or studying. These limitations result in inefficient knowledge retrieval, fragmented research workflows, and poor support for personalised learning.

### Objectives
1. To design and implement a graph-native hybrid RAG pipeline combining knowledge graph traversal, dense vector search, and BM25 keyword retrieval with Reciprocal Rank Fusion, and to evaluate its retrieval accuracy against a standard flat vector RAG baseline.
2. To develop a composable multi-agent orchestration system using LangGraph, enabling specialised agents (Research, Learning, Writing, Graph, Annotation, and Insight) to autonomously decompose and delegate complex research tasks through agent-to-agent tool invocation.
3. To build and evaluate an adaptive user interface with task-mode switching (Research, Writing, and Study modes) that dynamically reconfigures available tools and layout based on the user's current activity.

### Pre-requisite
Retrieval-Augmented Generation (RAG), Large Language Model (LLM) API integration, graph database concepts, Python (FastAPI, LangGraph), Next.js 14 (React), vector embeddings and similarity search.

### Short Summary
This project proposes the design and development of a graph-native multi-agent research and learning intelligence platform — an AI-powered knowledge assistant that addresses the contextual isolation problem in existing RAG-based document tools. Unlike conventional systems that store documents as flat, disconnected vector chunks, this platform extracts entities and relationships from ingested documents and constructs a structured knowledge graph (using Neo4j or NetworkX). Retrieval is performed via a three-way hybrid pipeline combining graph traversal, dense vector search (3,072-dimensional embeddings via OpenAI text-embedding-3-large), and BM25 keyword matching, merged using Reciprocal Rank Fusion. The system is orchestrated by a LangGraph multi-agent pipeline where six specialised agents — Research, Learning, Writing, Graph, Annotation, and Insight — can invoke each other as tools to handle complex, multi-step tasks. The platform features an adaptive three-panel interface that reconfigures based on the user's current task mode. The project extends VERA AI, a RAG-powered enterprise knowledge assistant developed by the same author during a Student Industrial Project at PETRONAS Upstream (BPI Unit), which achieved 94% citation accuracy and a 95% reduction in knowledge retrieval time. The system will be evaluated through a quantitative retrieval benchmark against a flat RAG baseline and a structured user study with student participants.

### Tools / Equipment Required
Next.js 14 (Frontend Framework), Tailwind CSS, Framer Motion, FastAPI (Python Backend), LangGraph (Multi-Agent Orchestration), Claude API / OpenRouter (LLM), OpenAI text-embedding-3-large (Embeddings), Pinecone (Vector Store), Neo4j Community / NetworkX (Knowledge Graph), Firebase Firestore + Auth (Database & Authentication), GitHub (Version Control), VS Code / Cursor (Development Environment)

---

## 11. Advisor Presentation Slides — Content Outline

### Slide 1 — Title
- GraphRAG-Powered Multi-Agent Research and Learning Intelligence Platform
- Fakhrul Azim Bin Ahmed Mardzukie | FYP Title Proposal | [Semester & Year]
- Supervisor: [TBD]

### Slide 2 — The Problem
- Existing RAG tools (e.g. NotebookLM) store documents as isolated silos — no awareness of cross-document relationships
- Users must manually connect ideas across sources; the AI cannot do it for them
- No specialised task support — one chatbot handles everything, poorly
- Static interfaces that don't adapt to whether the user is researching, writing, or studying
- Result: fragmented workflows, slow synthesis, and high cognitive load for the user

### Slide 3 — Proposed Solution (Three Core Innovations)
**Innovation 1 — Graph-Native RAG:** Documents stored as interconnected knowledge graph. Retrieval = graph traversal + vector search + BM25, merged via RRF.
**Innovation 2 — Composable Multi-Agent Pipeline:** 6 specialised agents on LangGraph — agents can invoke each other as tools for complex multi-step tasks.
**Innovation 3 — Adaptive Interface:** 3-panel layout (Documents | Chat | Agents) with task-mode switching between Research, Writing, and Study modes.

### Slide 4 — Built on VERA AI (Prior Work)
Comparison table: VERA AI vs This FYP (see Section 3 table above)
Key message: VERA AI proved the RAG foundation works. This FYP upgrades the intelligence layer.

### Slide 5 — Tech Stack
- Frontend: Next.js 14, Tailwind CSS, Framer Motion
- Backend: FastAPI (Python)
- Agent Orchestration: LangGraph
- LLM: Claude API (primary), OpenRouter (fallback)
- Embeddings: OpenAI text-embedding-3-large (3,072-dim)
- Vector Store: Pinecone
- Knowledge Graph: Neo4j / NetworkX
- Database & Auth: Firebase Firestore + Auth

### Slide 6 — Objectives & Scope
3 primary objectives (see Section 6). In-scope and out-of-scope items (see Section 7).

### Slide 7 — Evaluation Plan
- Retrieval benchmark: 20 multi-document questions with known correct answers — compare graph hybrid RAG vs flat vector RAG on accuracy and relevance
- User study: 15 student participants, two conditions (with graph vs without graph), measuring task completion time and answer quality
- Secondary: informal qualitative comparison against Google NotebookLM

### Slide 8 — Timeline
FYP 1 (Weeks 1–12) and FYP 2 (Weeks 1–16) milestones — see Section 8.

---

## 12. Related Literature (13 Papers, All ≤5 Years)

### Cluster 1: Foundational RAG

**[1] Gao et al. (2024). Retrieval-Augmented Generation for Large Language Models: A Survey.**
- arXiv:2312.10997 | https://arxiv.org/abs/2312.10997
- Covers Naive RAG → Advanced RAG → Modular RAG progression. Essential baseline citation. Use to establish why plain RAG is insufficient and why GraphRAG is the next step.

**[2] Sarmah et al. (2024). Hybrid RAG: Improving RAG Accuracy with Semantic Search and Hybrid Query-Based Retrievers.**
- arXiv:2404.07220 | https://arxiv.org/abs/2404.07220
- Directly validates the hybrid BM25 + vector retrieval strategy. Provides empirical benchmarks showing hybrid outperforms pure vector or pure keyword. Use as mid-baseline between plain RAG and full GraphRAG.

### Cluster 2: GraphRAG & Knowledge Graph Retrieval

**[3] Edge, D., Trinh, H., et al. (2024). From Local to Global: A Graph RAG Approach to Query-Focused Summarization. (Microsoft Research)**
- arXiv:2404.16130 | https://arxiv.org/abs/2404.16130
- THE primary GraphRAG foundation paper. Standard RAG fails on global corpus-level questions; GraphRAG solves this via LLM-built entity knowledge graph + community summaries. Your project extends this from enterprise summarization to interactive multi-agent research tools.

**[4] Han, H., Wang, Y., et al. (2024). Retrieval-Augmented Generation with Graphs (GraphRAG). arXiv:2501.00309.**
- https://arxiv.org/abs/2501.00309
- First comprehensive GraphRAG survey. Formalises Graph-Based Indexing → Graph-Guided Retrieval → Graph-Enhanced Generation workflow. Use to position your system within the GraphRAG taxonomy.

**[5] Gutiérrez, B.J., Shu, Y., Gu, Y., Yasunaga, M., & Su, Y. (2024). HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models. NeurIPS 2024.**
- arXiv:2405.14831 | https://arxiv.org/abs/2405.14831
- Closest existing system to your approach. Uses LLM to build schemaless knowledge graph + Personalised PageRank for retrieval, mimicking hippocampal memory indexing. Key comparison point. Your project extends the concept with composable multi-agent system + adaptive UI for students/researchers.

**[6] Guo, Z., Xia, L., et al. (2024). LightRAG: Simple and Fast Retrieval-Augmented Generation.**
- arXiv:2410.05779 | https://arxiv.org/abs/2410.05779
- Leaner, more computationally efficient GraphRAG alternative. Achieves comparable accuracy at ~10x lower token cost via dual-level (local + global) retrieval. Use when justifying design trade-offs between Neo4j and NetworkX, and to reference the efficiency vs depth debate.

**[7] Zhang, B., & Soh, H. (2024). Extract, Define, Canonicalize: An LLM-based Framework for Knowledge Graph Construction. EMNLP 2024.**
- https://aclanthology.org/2024.emnlp-main.548/
- Proposes the EDC framework for building knowledge graphs from arbitrary text without a pre-defined ontology — exactly what your ingestion pipeline needs since users upload diverse, arbitrary documents. Use for the document ingestion methodology section.

### Cluster 3: Multi-Agent LLM Systems

**[8] Zhuge, M., Hong, S., et al. (2024). MetaGPT: Meta Programming for Multi-Agent Collaborative Framework. ICLR 2024.**
- arXiv:2308.00352 | https://arxiv.org/abs/2308.00352
- Foundational work on role-specialisation in multi-agent LLM systems. Theoretical basis for your 6-agent specialised pipeline. Each of your agents (Research, Writing, Learning) embodies this role-specialisation principle.

**[9] Zheng, C., et al. (2024). Exploration of LLM Multi-Agent Application Implementation Based on LangGraph + CrewAI. arXiv:2411.18241.**
- https://arxiv.org/abs/2411.18241
- One of the few academic papers directly evaluating LangGraph as an orchestration framework — the exact tool you are using. Validates your tech stack choice and gives citable justification for choosing LangGraph over AutoGen or plain LangChain.

**[10] Tran, A., et al. (2025). AdaptOrch: Task-Adaptive Multi-Agent Orchestration in the Era of LLM Performance Convergence. arXiv:2602.16873.**
- https://arxiv.org/abs/2602.16873
- 2025 cutting-edge paper identifying that static LangGraph pipelines have a "topology selection problem" — exactly the limitation your composable, task-adaptive agent pipeline is designed to address. Positions your work at the frontier of the field.

### Cluster 4: Adaptive Learning & Personalised Interfaces

**[11] Essa, S.G., Celik, T., & Human-Hendricks, N.E. (2023). Personalized Adaptive Learning Technologies Based on Machine Learning Techniques to Identify Learning Styles. IEEE Access, 11, 48392–48409.**
- https://doi.org/10.1109/ACCESS.2023.3276284
- Systematic literature review covering adaptive learning technologies for identifying learning styles. Academic grounding for your adaptive UI's Learning Mode. Use to justify why one-size-fits-all interfaces (NotebookLM) are insufficient for learning contexts.

**[12] Dascalu, S.M., & Harris Jr., F.C. (2025). AI-Powered Adaptive Learning Interfaces: A User Experience Study in Education Platforms. Frontiers in Computer Science, 7.**
- https://doi.org/10.3389/fcomp.2025.1672081
- Evaluates 3 AI learning platforms with 23 participants, measuring task completion time, user satisfaction, engagement, and task accuracy. Your closest methodological reference for your own user study design. Draw from this explicitly when designing your user study protocol.

**[13] Strielkowski, W., et al. (2025). AI-Driven Adaptive Learning for Sustainable Educational Transformation. Sustainable Development. Wiley.**
- https://doi.org/10.1002/sd.3221
- Bibliometric overview showing publications on adaptive learning in education grew from 1 (1990) to 636 (2023). Macro-level motivation for your entire project — demonstrates this is a rapidly scaling field. Use in the introduction to establish relevance and timeliness.

---

## 13. Documents Produced During This Session

| Document | Description | Status |
|---|---|---|
| `FYP_Project_Concept_Document.docx` | Full 11-section formal concept document | ✅ Generated |
| `FYP_Context_Document.md` (this file) | Full session context for continuity | ✅ Generated |
| FORM 01A content | Plain text fill-in content for UTP Form 01A | ✅ In Section 10 above |
| Advisor slides content | 8-slide content outline for supervisor pitch | ✅ In Section 11 above |
| 13 related papers | Annotated literature with citations and relevance notes | ✅ In Section 12 above |

---

## 14. Key Decisions Made

1. **Project name is still WIP** — NEXUS / GraphMind / Aether are working titles only. Not finalised.
2. **Student decided to proceed with the full project scope** despite council warnings about width — the council recommendation to scope down was noted but not adopted.
3. **Primary benchmark** = self-built flat RAG baseline (NOT NotebookLM as controlled experiment). NotebookLM = informal secondary comparison only.
4. **Evaluation dataset** = 20 multi-document questions with known correct answers requiring cross-document reasoning — to be designed in FYP 1.
5. **NetworkX for PoC** (FYP 1), then decide on Neo4j for FYP 2 based on scale.
6. **Minimum deliverable for FYP 2:** 3 agents (Research, Learning, Writing) + 2 UI modes (Research, Study) + graph hybrid RAG benchmark.
7. **VERA AI = FYP's own prior work baseline** — not starting from zero; reuse frontend architecture, embedding model, deployment patterns.

---

## 15. Important Context Notes for Continuing AI

- The student is **not** asking for help with FYP planning timelines or academic administration. The project concept is **decided**.
- The project title is **not finalised** — do not suggest locking it in until the student is ready.
- The student's supervisor has **not yet been assigned** — that field is blank in all documents.
- VERA AI GitHub repo: https://github.com/Azimlearning/VERA-AI
- The three-panel NotebookLM UI layout (left = docs, middle = chat, right = agent features) is the **confirmed UI pattern** to base the design on.
- The Obsidian-vault style knowledge web is the **confirmed storage model** the student wants.
- The student has **strong prior experience** with LangGraph (Buildora hackathon), Next.js 14 (VERA AI + multiple projects), FastAPI (Pasar, multiple projects), and Firebase (multiple projects).
- All documents produced use **Times New Roman** where applicable, detailed non-simplified notes, and plain academic styling (no table of contents unless specified).

---

*End of context document. Generated from FYP planning session, May 2026.*
