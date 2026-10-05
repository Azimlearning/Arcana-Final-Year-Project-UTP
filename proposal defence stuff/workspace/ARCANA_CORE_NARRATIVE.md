# ARCANA — Core Project Narrative
> This document is the canonical narrative reference for the Arcana FYP project.
> All slides, reports, presentations, and agent-generated content must align with this framing.

---

## ⚠ Live Deck Status — as of `PROPOSAL DEFENCE FINAL.pdf` (exported 2026-07-09, 21 pages)

This is the actual file being presented at today's defence — lives in `proposal defence stuff/FINAL/` alongside the finalised speaking script, for easy access on the day. It was checked slide-by-slide against the "locked decisions" and "Remaining Canva Edits" recorded below (those were written against the 2 July export). Two of the previously-flagged fixes were **not** carried into this export. Given same-day timing, the decision was to present as-is and let the spoken script compensate rather than re-edit Canva:

1. **Objective slide (06) grid order is GraphRAG → GenUI → Agents → ML**, not the canonical chain order (GraphRAG → Agents → ML → GenUI) locked below. This is the superseded 2×2 grid the "Proposed Solution slide" decision said to move away from — it's back in this export. **Decision: present as-is.** The script narrates in the order actually on screen (01→02→03→04) so spoken order matches what the audience reads, rather than fighting the slide.
2. **Slide 13 (Expected Outcome) Objective 03 still reads** "In Progress — Training pipeline built; engines not yet trained" — the exact claim flagged as indefensible under ADR-017 (no training code exists yet). **Decision: present as-is.** The script does not lean on "pipeline built" when narrating this line — it says "designed and specified, implementation next" verbally, so the spoken claim stays defensible even though the slide text is more optimistic.
3. Slide 13 Objective 04 status also reads differently than any prior draft: "In Progress — Component catalog and adaptive dashboard semi built but not integrated into the app." The script now quotes this framing rather than the older "pipelines are built" phrasing.
4. The "no hard numeric targets" rule is also not fully applied — "25-agent suite" and "24-component Generative UI" still appear on the Objective and Methodology & Work Plan slides. The script still avoids stating exact counts verbally (per the rule below), even where the slide itself states them — safer to under-claim out loud than to be pinned to a number that shifts.
5. Scope & Limitations content (assumed merged into the Problem Statement slide per an earlier plan) does not appear in this export's Problem Statement slide — it may exist as a graphic not captured in text extraction, or may have been dropped. Not addressed by the script either way; flag for a post-defence check if it matters for the interim report.

If Canva gets touched again before FYP2 materials are built, apply the fixes in **Remaining Canva Edits** below for real — they were never wrong, just not carried through to this export.

---

## The One-Line Pitch

Arcana is a graph-native research and learning platform for students — built on a GraphRAG pipeline that surfaces cross-document connections no flat RAG system can find, with a multi-agent suite, trained ML engines, and an adaptive Generative UI on top.

---

## The Problem

Students working with large document sets hit a wall that no current tool solves:

- They upload 15 papers and cannot find which one contradicts another — because no tool tracks relationships between documents, only within them.
- They cannot connect concepts across subjects or sources without doing it manually — the AI only matches text, not meaning across boundaries.
- Existing AI assistants (NotebookLM, Perplexity, Elicit) treat every document as an isolated silo. Flat vector search retrieves similar chunks — it cannot traverse relationships between entities across documents.

The root cause is architectural: **flat RAG stores documents as disconnected chunks**. You can find relevant text. You cannot find connected ideas.

---

## Why GraphRAG Solves This

Flat vector RAG embeds text and retrieves by cosine similarity. It has no concept of entities, relationships, or cross-document structure.

GraphRAG changes the storage model. During ingestion, entities and relationships are extracted from every document and stored in a knowledge graph alongside the vector index. At query time, retrieval traverses the graph — following entity links across documents — rather than just matching text.

This enables:
- **Multi-hop reasoning** — answering questions that require connecting facts from 3 different sources
- **Contradiction detection** — finding where two documents make conflicting claims about the same entity
- **Hidden connection surfacing** — discovering relationships the student never explicitly searched for

This is Arcana's core technical contribution. Everything else is built on top of this foundation.

---

## The VERA AI Baseline

Before Arcana, the project built **VERA AI** — a production RAG assistant deployed at PETRONAS Upstream (BPI Unit) during a Student Industrial Project.

VERA AI achieved:
- **94% citation accuracy**
- **95% retrieval speed improvement** over the previous system

VERA AI is flat RAG. It works well for single-document Q&A and grounded responses. It cannot answer cross-document questions. It cannot detect contradictions. It cannot surface hidden connections.

VERA AI is the proof that flat RAG works in production — and the concrete baseline that motivates going further. Arcana is what VERA AI becomes when you replace flat retrieval with a knowledge graph.

> In competitive comparisons and benchmark discussions, VERA AI is the flat-RAG baseline. Arcana's GraphRAG pipeline is measured against it.

---

## The Full System — How Each Layer Follows From GraphRAG

### 1. GraphRAG Pipeline (The Core)
- Ingestion: parse → chunk → embed → entity/relation extraction
- Storage: Knowledge Graph (NetworkX prototype → Neo4j) + Pinecone vector index + Firestore metadata
- Retrieval: dense vector + BM25 + graph traversal (Louvain communities + PageRank), fused via Reciprocal Rank Fusion (RRF)
- This is the layer that makes cross-document reasoning possible.

### 2. Multi-Agent Suite + Tool Calls (Consequence of GraphRAG)
- Because retrieval now surfaces structured, connected knowledge, you need specialised agents to act on it.
- A single general-purpose chatbot cannot route a contradiction-detection task the same way it routes a study plan task.
- 25-agent target, LangGraph-orchestrated, 4-tier architecture. All agents communicate only through `route_to_agent`. 15+ confirmed built.
- Each agent has its own tool calls — tool calls are part of the agent layer, not separate.
- Key agents: Orchestrator, Research, Graph, Literature, Contradiction, Comparator, Timeline, Annotation, Learning, Writing, Socratic, Study Planner, Fact Checker, UI Agent.

### 3. Trained ML Engines (Personalisation on Top of Retrieval)
- Because retrieval is now high-quality and structured, ML models can personalise further rather than fighting noise.
- **Re-Rank Engine** — gradient-boosted trees over BM25/cosine/graph-hop-distance/RRF-rank features. Re-scores retrieval results per query.
- **Mastery Engine** — Half-Life Regression (HLR) for spaced repetition scheduling. Tracks what the student knows and surfaces gaps, not already-mastered material.
- **Document Classifier Engine** — tags chunks by document type to route them correctly through the pipeline.
- All three share one `Engine` interface (`predict()`, `is_available()`) so the pipeline degrades gracefully while training is in progress.

### 4. Generative UI — 24 Components, 5 Modes (Adaptive Output Layer)
- Because different tasks produce different output types, a static chat interface is the wrong container.
- The UI Agent selects from a 24-component catalog (22/24 confirmed built): CitedSummary, KnowledgeGraphView, FlashcardDeck, SocraticDialog, StudyPlanner, and others.
- Output is a typed `UIBlock {type, data, meta}` streamed as React Server Components over SSE.
- The frontend renders an adaptive 3-panel dashboard that reshapes across 5 task modes: Research, Study, Writing, Socratic, Exploration.

### 5. Arcana — The Vessel
- Arcana is not just a feature list. It is the platform that holds all of the above together and exposes it to students through one coherent workspace.
- Firebase Auth + Firestore for accounts and persistence.
- Obsidian import/export for interoperability.
- The name comes from the Latin *arcana* ("secrets, mysteries") — reflecting the core mandate: surfacing hidden cross-document connections that flat, siloed RAG tools leave buried.

---

## The Narrative Chain (Use This Order Every Time)

```
Student problem (manual connection, siloed documents)
        ↓
Existing tools fail because flat RAG is architecturally limited
        ↓
VERA AI proves flat RAG works — and shows exactly where it breaks
        ↓
GraphRAG fixes the architecture (knowledge graph + hybrid retrieval)
        ↓
High-quality retrieval enables specialised agents + tool calls
        ↓
Structured knowledge enables ML personalisation (Re-Rank, Mastery, Classifier)
        ↓
Rich, typed output enables Generative UI (24 components, 5 modes)
        ↓
Arcana holds it all together as one adaptive student workspace
```

This chain must be preserved in all presentations, reports, and explanations. Do not introduce agents before establishing GraphRAG. Do not introduce GenUI before establishing agents.

---

## Slide Presentation Rules

These apply to slides specifically (not to internal docs like the Current Build Status table below, which should stay exact):

- **No hard numeric targets in slides.** Don't say "25 agents," "15+ built," "24-component catalog," "22/24 confirmed." Describe these as general capabilities (a multi-agent suite, a component catalog). Exact counts are a moving, easily-attacked target during defence — state the capability, not the count.
- **"Adaptive task modes," not "5 task modes."** 5 is the current build target, not a ceiling — the mode list (Research, Study, Writing, Socratic, Exploration) can still be named, just without the number framing it as fixed.
- **No phase/sprint labels outside the timeline slide.** Don't reference FYP1, FYP2, Phase P2, SIT, SIP, or TTP on any slide except the explicit roadmap/timeline slide. Elsewhere, describe deferred scope in plain terms (e.g. "scoped for continued development beyond this milestone") instead of naming the phase.
- **`route_to_agent` stays in code, not slide prose.** On slides outside a dedicated architecture deep-dive, describe it as "a single routing function/mechanism" rather than the literal identifier — keeps the slide readable without losing the architectural point (no direct agent-to-agent imports).

**Locked decision (Objectives slide, finalised):** Knowledge & Retrieval / Agents & Tools / Trained ML Models / Generative UI, Dashboard & I/O — order corrected to match the canonical chain (GraphRAG → Agents → ML Engines → GenUI), superseding the earlier 2×2 grid draft which had GenUI before ML. Each block de-numbered per the rules above. This is the reference style for every subsequent slide in this deck (Scope & Limitations, Proposed Solution, etc.): no counts, no phase labels, mechanisms described in prose, and the four-pillar order kept identical everywhere it appears.

**Locked decision (Proposed Solution slide, finalised):** Merged with the old "Ecosystem" summary block — that content was redundant with Objectives and now lives only in the conclusion slide as delivered-status. Final structure: a chain strip (GraphRAG → Agents & Tools → ML Engines → Generative UI → Arcana), a left panel of 4 one-sentence blocks (one per pillar, no elaboration — verbal delivery carries the why/how), and a right panel with just the headline tagline and the Arcana name-origin line. Proposed Solution = what it is; Conclusion = what was delivered against each objective. Don't re-add detail here — that's the point of the split.

**Locked decision (Competitive Analysis slide, new):** Inserted between Proposed Solution and System Architecture, using the Competitive Positioning table below as-is. Answers "why does this project need to exist" before the technical deep-dive begins — VERA AI sits in the table as the flat-RAG baseline, scoring identically to other flat tools on every graph-dependent row, visually proving GraphRAG (not just more engineering) is what unlocks the right side of the table.

**Locked decision (technical diagram slides, finalised):** Consolidated 10 candidate diagram slides down to 5 — System Architecture, Knowledge Graph, ML Engines, Output Formats, Tech Stack. Cut Ingestion Pipeline, Orchestration, and Generative UI as standalone slides because System Architecture's three lanes (Input/Reasoning/Output) already contain compressed versions of all three — their depth is narrated verbally during that one walkthrough instead of shown twice. Cut one duplicate Output Formats slide (was pixel-identical). Cut Dashboard (was empty — treat as a live demo moment, not a static slide). Each surviving slide gets a one-line caption stating what it proves, not just what it shows. Outstanding diagram-art fix (not a text edit): ML Engines slide has "Phase P1/P2" badges baked into the graphic — needs re-editing in Canva to match the no-phase-label rule.

---

## Final Deck Structure (as exported — `PROPOSAL DEFENCE FINAL.pdf`, dated 9 July 2026, 21 pages)

This is the confirmed slide order in the deck actually being presented today. Supersedes the 2 July structure previously recorded here (that export had a different page count and an assumed Scope & Limitations merge that isn't present in this one). Use this as the reference for the speaking script and any future Canva edits.

| # | Slide title (on-screen) | Notes |
|---|---|---|
| 1 | Title | "GraphRAG-Powered Multi-Agent Research & Learning Intelligence Platform · FYP 1 Proposal Defence" |
| 2 | Overview | Numbered section list, two columns |
| 3 | Introduction | Single slide: What is RAG, Why It Matters, GraphRAG vs Vector RAG, takeaway line |
| 4 | Research Journey | Timeline SIT→SIP→TTP→FYP1→FYP2→Future, VERA AI baseline proof panel |
| 5 | Problem Statement | Three root-cause problems (Reactive/No Specialised Support/No Personalisation) + underlying-cause line. No Scope & Limitations content visible in this export. |
| 6 | Objective | Four objective blocks in a 2×2 grid — **order is GraphRAG → GenUI → Agents & Tools → Trained Models (⚠ not the canonical chain order — see Live Deck Status above)**; The Single Workspace / The Ecosystem / Name Origin blocks below |
| 7 | Literature Review | 20 papers grouped by domain (table extraction was too garbled to confirm exact domain count with certainty — script says "eight," inherited from the original draft), 7 research gaps G1–G7 |
| 8 | Competitive Analysis | Feature matrix vs NotebookLM / Elicit / Perplexity / VERA AI; Vector RAG vs GraphRAG comparison table |
| 9 | Methodology & Work Plan | Agile/RAGAS-gated, phase-labelled blocks, agent/component counts still present (⚠ see Live Deck Status) |
| 10 | System Architecture | A/B/C/D lanes: Ingestion, Agentic Reasoning, Adaptive GenUI, Personalised ML Engines |
| 11 | Tech Stack | ML Training & Data, LLM & Generative APIs, Retrieval & Knowledge Stores, Backend & Orchestration, DB & Auth, Frontend & GenUI panels |
| 12 | Work Plan Gantt Chart | FYP1 weeks −1→14 and FYP2 weeks 1→15 |
| 13 | Expected Outcome & Conclusion | Objectives status table (⚠ Obj 03/04 wording — see Live Deck Status) + WHAT ARCANA DELIVERS + CONTRIBUTIONS |
| 14 | Dashboard Demo | Live demo placeholder |
| 15 | Live Demo | Live demo placeholder |
| 16 | Future Work | Evaluation 1 (Retrieval Benchmark) + Evaluation 2 (User Study) |
| 17–19 | References | 20 papers across Foundational RAG / GraphRAG / Multi-Agent / Adaptive UI / ML / Evaluation |
| 20 | Thank You | |
| 21 | QNA | |

---

## Remaining Canva Edits (still not applied as of the 9 July live export)

These were confirmed from the 2 July 2026 PDF export and checked again against the 9 July export used for today's defence — **none of them were carried through**. Fixes must be applied manually in Canva — they are not copy-paste-ready drafts, they are specific string replacements. Not blocking for today (see Live Deck Status above for how the script compensates verbally); apply for real before any future re-export.

### Slide 6 — Proposed Solution + Objectives

**Ecosystem block (right panel):**
> *Current:* "Operates a modular ecosystem of a 25-agent LangGraph suite (15+ confirmed built), a 24-component Generative UI catalog, and three trained ML Engines…"
> *Fix:* "Operates a modular ecosystem of a multi-agent LangGraph suite, a Generative UI component catalog, and three trained ML Engines…"

**Objective 02 — Agents & Tools:**
> *Current:* "…a composable, LangGraph-orchestrated 25-agent suite each agent equipped with…"
> *Fix:* "…a composable, LangGraph-orchestrated multi-agent suite, each agent equipped with…"

**Objective 04 — GenUI:**
> *Current:* "Build and demonstrate an adaptive 24-component Generative UI…"
> *Fix:* "Build and demonstrate an adaptive Generative UI component catalog…"

### Slide 9 — Methodology & Work Plan

**Phase labels** (P0 → P1 → P2 notation and P0/P1/P2 as section headers):
> These violate the no-phase-labels rule (only the timeline/Gantt slide may use phase labels). Replace with plain headings such as "Research & Foundation → Core Build → Full Platform → Evaluation & Submission" or similar descriptive terms.

**Agent and component counts in the P1 block:**
> *Current:* "15+ agents across 4 tiers, 22/24 GenUI components, UIBlock streaming protocol…"
> *Fix:* "Multi-agent suite across all tiers, full GenUI component catalog, UIBlock streaming protocol…"

**Placeholder text** — confirmed resolved in this PDF:
- ✓ "[PLACEHOLDER: size TBC]" → "size finalised with supervisor"
- ✓ "[PLACEHOLDER: sample size and recruitment TBC]" → "recruitment finalised with supervisor"

### Slide 13 — Expected Outcome & Conclusion (⚠ factual correction)

**Objective 03 status line:**
> *Current:* "03 — Trained ML Models: In Progress — training pipeline built; engines not yet trained"
> *Fix:* "03 — Trained ML Models: In Progress — Engines designed and specified; implementation is the next build phase"
> *Why:* No ML training code exists yet (checklist §1.14, ADR-017). Claiming a "training pipeline built" is not defensible if an examiner asks to see it. The honest framing — designed, implementation next — still supports Objective 03 as a live graded deliverable.

---

## ML Engines — scope decision (2026-07-03)

The ML Engines (Re-Rank, Mastery, Document Classifier) are **graded FYP2 scope**, matching Objective 03 in the deck. The codebase docs were pulled into line on 2026-07-03 (Arcana `DECISIONS.md` **ADR-017**, supersedes ADR-013; PRD §12A/§17.10/§24; checklist §1.14). Defence-relevant framing:

- **Graded core is the Re-Rank Engine** (gradient-boosted, post-RRF) behind a shared `Engine` interface. Mastery + Document Classifier are lower-priority and may ship as pretrained priors.
- **The Engines are strictly additive.** They never replace RRF fusion — the graph-vs-flat retrieval benchmark (the project's primary empirical claim) stands alone with or without any Engine attached. If asked "does the ML model prop up your main result?", the answer is no: it's a separate, additional benchmark arm.
- **Current honest status:** designed and specified, not yet built — implementation is the immediate next development phase.

---

## Competitive Positioning

| Feature | NotebookLM | Elicit | Perplexity | VERA AI (flat RAG) | **Arcana** |
|---|---|---|---|---|---|
| Cross-document graph traversal | ✗ | ✗ | ✗ | ✗ | ✓ |
| Multi-hop reasoning | ✗ | Partial | ✗ | ✗ | ✓ |
| Contradiction detection | ✗ | ✗ | ✗ | ✗ | ✓ |
| Specialised multi-agent routing | ✗ | ✗ | ✗ | ✗ | ✓ |
| Adaptive UI per task mode | ✗ | ✗ | ✗ | ✗ | ✓ |
| Trained ML personalisation | ✗ | ✗ | ✗ | ✗ | ✓ |
| Grounded citations | ✓ | ✓ | Partial | ✓ | ✓ |
| Works on private/local corpus | ✓ | ✗ | ✗ | ✓ | ✓ |

---

## Academic Contributions

1. **A reproducible graph-hybrid vs. flat vector-RAG retrieval benchmark** — measured via RAGAS (faithfulness, answer relevance, context precision, context recall) on a held-out multi-hop cross-document question set.
2. **A working multi-agent research and learning platform** — demonstrated end-to-end across all 5 task modes on real student documents.

---

## Current Build Status (as of FYP1 close / FYP2 start)

| Component | Status |
|---|---|
| Ingestion pipeline | ✓ Complete |
| Knowledge graph (NetworkX) | ✓ Complete |
| Hybrid retrieval (vector + BM25 + graph + RRF) | ✓ Complete |
| Orchestrator + Research + Graph agents | ✓ Complete |
| 15+ agent suite | ✓ Confirmed built |
| 22/24 GenUI components | ✓ Confirmed built |
| Firebase Auth + Firestore | ✓ Complete |
| Re-Rank Engine | ✗ Designed (PRD §12A); implementation is the next build phase — nothing coded yet |
| Mastery Engine | ✗ Designed (PRD §12A); not yet built |
| Document Classifier Engine | ✗ Designed (PRD §12A); not yet built |
| Neo4j migration (from NetworkX) | ✗ In progress |
| Full RAGAS benchmark | ✗ Scheduled P1 remainder |
| User study | ✗ Design ready, recruitment TBC |

---

## What This Project Is NOT

- Not a general-purpose web search tool (Arcana reasons over the student's curated corpus only)
- Not a real-time multi-user collaboration platform
- Not an audio/video generation tool
- Not a replacement for a search engine

These are deliberate scope decisions, not limitations. The research boundary is: **can a graph-native multi-agent system measurably outperform flat RAG for student research and learning tasks?**

---

*Last updated: 9 July 2026 — cross-checked against `PROPOSAL DEFENCE FINAL.pdf` (live defence deck) and the finalised speaking script*
*Student: Fakhrul Azim bin Ahmed Mardzukie (22012087)*
*Supervisor: Dr Mazeyanti Bt M Ariffin*
*Co-supervisor: AP Dr Noreen Izza Bt Arshad*
*Universiti Teknologi PETRONAS*
