# Arcana — FYP1 Proposal Defence Speaking Script (FINAL)

**Presenter:** Fakhrul Azim Bin Ahmed Mardzukie (22012087)
**Target runtime:** ~15 min spoken + live demos + Q&A
**Delivery principle:** Lead with the student's pain, end on the payoff. Keep VERA AI as the pivot — every architectural choice traces back to what it proved was impossible.
**Checked against:** `PROPOSAL DEFENCE FINAL.pdf` (21 pages, exported 2026-07-09) — slide numbers, objective order, and status wording below match that exact file. See `ARCANA_CORE_NARRATIVE.md` → "Live Deck Status" for the two known slide/narrative gaps this script deliberately talks around.

> `[ ]` = delivery cue (click, gesture, pause). Say the plain prose; the slide carries the detail.

---

## Slide 1 — Title *(~20s)*

Good [morning/afternoon], Dr Mazeyanti and Dr Manoranjitham. My name is Fakhrul Azim, and today I'll be presenting my FYP1 proposal — **Arcana**, a GraphRAG-powered multi-agent research and learning intelligence platform.

`[Pause, advance]`

---

## Slide 2 — Overview *(~20s)*

Here's the roadmap for the next fifteen minutes. I'll start with the core idea and the research journey that led me here, walk through the problem, objectives, and literature, then cover the methodology, tech stack, and work plan — before closing with expected outcomes and a live demo of what's already built.

`[Advance]`

---

## Slide 3 — Introduction: What is RAG? *(~1m 30s)*

Let me start with the one concept everything rests on.

**RAG is an open-book exam for AI.** Instead of answering from memory alone, the model looks up the relevant material first, then answers using what it just read. That matters because a model trained normally only knows what it memorised during training — it can't know about a new paper you just uploaded, or a private document. RAG fixes that by retrieving the real source at query time, so the answers stay grounded.

`[Gesture to GraphRAG vs Vector RAG]`

Now, the distinction at the heart of my project. If **vector RAG** is finding matching pages in a library, **GraphRAG** is having a librarian who knows how every book connects to every other book — and can follow that trail to a complete answer.

So the takeaway is this: vector RAG finds *similar text*. GraphRAG finds *connected meaning* — and can answer questions that no single chunk of text could.

`[Advance]`

---

## Slide 4 — Research Journey / VERA AI *(~1m 30s)*

This isn't where I started — it's where a year of work led me.

`[Trace the timeline briefly]`

I began by learning the fundamentals — RAG, chunking, indexing. Then during my industrial project at PETRONAS Upstream, I built **VERA AI**, a real production RAG assistant. And VERA is exactly why I'm standing here proposing GraphRAG.

`[Point to the VERA AI box — this is the pivot]`

VERA is not a naive system. It already fuses dense vector search and BM25 keyword matching through Reciprocal Rank Fusion — a well-tuned, production-grade hybrid retriever. But here's the ceiling I hit: every chunk is still ranked on its own. VERA finds you the single most relevant passage — but it **cannot tell you that two passages contradict each other, or that one concept depends on another.** That synthesis is left entirely to the user.

Embedding similarity alone misses the relationships *between* entities across documents. VERA proved the limitation is real — and it's architectural, not a missing feature. That's the gap Arcana is built to close.

`[Advance]`

---

## Slide 5 — Problem Statement *(~1m 15s)*

That single architectural flaw cascades into three problems.

`[One, two, three]`

**One — it's reactive, not predictive.** Existing RAG tools store documents as isolated silos with no awareness of how they connect, so users are left to manually stitch ideas across sources.

**Two — no specialised task support.** Because retrieval never surfaces structured, connected knowledge, there's nothing for the system to route on. A study-plan request, a contradiction check, a citation request — all get the same generic chatbot reply.

**Three — no personalisation.** Retrieval is flat and undifferentiated, so two students uploading the same papers get identical results, regardless of where they are in their learning.

The underlying cause behind all three is the same: **flat, siloed retrieval.** Fix the retrieval layer, and the other two problems become solvable. That single point of failure is what Arcana's graph-native retrieval is designed to remove.

`[Advance]`

---

## Slide 6 — Objective *(~1m 15s)*

So Arcana has four objectives — I'll walk them in the order they're numbered on screen.

**One — GraphRAG.** Design a graph-native hybrid pipeline that extracts entities and relationships from every document into one interconnected knowledge graph, fusing graph traversal, vector search, and BM25 — and prove it beats a flat vector-RAG baseline on a quantitative benchmark. This is the foundation everything else sits on.

**Two — Generative UI, dashboard, and I/O.** An adaptive interface covering every input path — document upload, chat query — and every output path — cited summaries, knowledge-graph views, flashcards, and more — streamed through one dashboard that reshapes itself across Research, Writing, Study, Socratic, and Exploration modes.

**Three — agents and tools.** Because retrieval is now high-quality and structured, a composable, LangGraph-orchestrated agent suite, each agent with its own tools, communicating through a single routing function, demonstrated end-to-end on at least one complete multi-agent research task.

**Four — trained models.** ML Engines behind one shared interface, personalising ranking, spaced repetition, and document handling — beyond what fixed rules can do.

`[Gesture to the name origin, lightly]`

Structurally they still build on each other in that order — GraphRAG is what makes the agents' retrieval worth routing on, what the ML engines personalise on top of, and what the interface ultimately renders. And the name — *Arcana*, Latin for "secrets, mysteries" — reflects the mandate: surfacing the hidden cross-document connections that flat RAG leaves buried.

`[Advance]`

---

## Slide 7 — Literature Review *(~1m)*

I reviewed twenty papers across eight domains. I won't read the table — but here's the shape of it.

`[Sweep hand down the domains]`

Foundational RAG confirms plain retrieval isn't enough. The GraphRAG line — Edge and colleagues, 2024 — pioneered the entity-graph paradigm, but only for enterprise summarisation, never an interactive research tool. The KG-construction and multi-agent work gives me the building blocks, and the ML and evaluation papers ground my engines and my benchmark.

Out of that review, I isolated **seven concrete research gaps** — from "no graph signal in retrieval" to "no graph-versus-flat evaluation gate." Each one maps directly to a component I'm building. Arcana isn't feature accumulation — every piece answers a specific documented gap.

`[Advance]`

---

## Slide 8 — Competitive Analysis *(~50s)*

Here's how that lands against what already exists.

`[Point to the comparison columns]`

NotebookLM, Elicit, Perplexity — and my own VERA AI — all fail on the capabilities that matter most: cross-document graph traversal, multi-hop reasoning, contradiction detection, specialised routing. Arcana is the only column that's a full set of checkmarks.

And the bottom table makes the *why* concrete: vector RAG retrieves isolated chunks and reasons one hop at a time. GraphRAG retrieves entities and relationships, traverses across documents, and answers corpus-wide questions directly. The cost is higher indexing — which leaner designs like LightRAG largely recover.

`[Advance]`

---

## Slide 9 — Methodology & Work Plan *(~1m 15s)*

The methodology is agile and iterative, structured in three priority phases across roughly thirty weeks.

`[P0, P1, P2]`

**P0 — the foundation:** ingestion, knowledge-graph construction, hybrid retrieval, and the first three agents, end to end. **P1 — scale up:** the full agent suite across every tier, the GenUI component catalog, all task modes, and the adaptive dashboard. **P2 — prove it:** train the Re-Rank Engine, run the RAGAS-gated benchmark against flat RAG, run the user study, and write the dissertation.

The evaluation is gated — nothing ships as "proven" until it passes a RAGAS comparison against the flat-vector baseline. That baseline, again, is VERA.

`[Advance]`

---

## Slide 10 — Architecture Diagram *(~1m 15s)*

This is the whole system on one slide. Let me trace the flow.

`[Follow the arrows: A → B → C → D]`

**A — ingestion.** A document comes in, gets parsed, chunked, embedded, and then — the key step — entities and relationships are extracted schema-free and written simultaneously to the vector store and the knowledge graph.

**B — agentic reasoning.** A user query hits the LangGraph orchestrator, which routes through a single routing function to a composable suite of twenty-five agents, backed by hybrid retrieval and session memory.

**C — the adaptive GenUI.** The result isn't plain text — the system selects from a typed catalog of components and streams them to a dashboard that reshapes itself per task mode.

**D — the ML engines.** The Re-Rank, Mastery, and Classifier engines sit on top, personalising the whole pipeline.

Everything writes back to one unified data tier — Firestore, Pinecone, and Neo4j.

`[Advance]`

---

## Slide 11 — Tech Stack *(~40s)*

Quickly on the stack. `[Sweep across cards]` FastAPI and Python for the backend; LangGraph orchestrating the agent suite; Pinecone plus Neo4j behind a GraphStore abstraction for hybrid retrieval; TensorFlow on Colab for the ML engines; Claude as the primary LLM with OpenRouter fallback; and a Next.js 14 frontend streaming the Generative UI through the Vercel AI SDK. All production-grade, all already wired up.

`[Advance]`

---

## Slide 12 — Work Plan Gantt Chart *(~30s)*

And here's the timeline mapped to the official FYP milestones — FYP1 across the current fourteen weeks, FYP2 through to hard-bound submission. The milestones you'd expect — proposal defence, interim report, dissertation — are all placed against the build phases I just described.

`[Advance]`

---

## Slide 13 — Expected Outcome & Conclusion *(~1m)*

So where does that leave me today?

`[Point to the status pills — be honest and precise about what's done vs. in progress]`

Objectives one and two — **knowledge and retrieval, and the agent suite — are done and working.** The graph-hybrid pipeline is built; the quantitative benchmark against the flat-RAG baseline is what's left to run. The agent suite is complete end-to-end — I've demonstrated a full multi-agent task on it.

Objectives three and four are in progress, and I want to be precise about where. The ML Engines are designed and specified behind one shared interface — training and integration is the next build phase, nothing's been trained yet. The Generative UI component catalog and adaptive dashboard are partially built but not yet wired into the live app — that integration is next too.

What Arcana delivers is three replacements: graph-native retrieval instead of flat silos, a composable agent suite instead of one chatbot, and an adaptive UI instead of a static chat window.

And the contribution is both academic and practical — **a reproducible comparison of graph-hybrid versus flat vector-RAG, built directly on the VERA AI baseline**, plus a working platform demonstrated end-to-end on real documents.

`[Advance — transition to demo]`

Rather than just tell you — let me show you.

---

## Slide 14 — Dashboard Demo *(live — ~intro 15s)*

`[Switch to the app]` This is the Arcana dashboard. Let me walk you through the adaptive interface and how it reshapes per task mode.

> **Demo notes:** [keep it to 2–3 clicks — show the mode switch and one component render. Have a fallback screenshot ready in case of network.]

---

## Slide 15 — Live Demo *(live — ~intro 15s)*

`[Run the query]` And here's the retrieval working live — I'll upload a document, and run a cross-document query that flat RAG couldn't answer, so you can see the graph traversal and cited output in action.

> **Demo notes:** [pick one query that clearly shows a multi-hop or contradiction result — the thing VERA can't do. That's the money shot.]

---

## Slide 16 — Future Work / Evaluation *(~1m)*

Coming out of the demo — this is how I'll rigorously prove it in FYP2. Two evaluations.

**One — the retrieval benchmark.** The claim: graph-hybrid retrieval outperforms flat vector-RAG on cross-document queries. Same embedding model, same documents, no graph traversal — that's the baseline. Measured through a RAGAS gate: faithfulness, relevance, context precision and recall. Smoke benchmarks are already done; the full comparison runs next phase.

**Two — a user study.** The claim: the adaptive GenUI is coherent and usable across all adaptive task modes. Structured tasks per mode, a representative student sample, measuring completion rate, mode-switch friction, and perceived usefulness. Study design is complete; recruitment is finalised with my supervisor.

`[Advance]`

---

## Slide 17–19 — References *(~10s, only if flipped)*

`[If you land here, don't read them]` These are the twenty papers underpinning the design, grouped by domain — I'm happy to point to any specific citation during questions.

`[Advance]`

---

## Slide 20 — Thank You *(~10s)*

That's Arcana — turning scattered documents into one living knowledge graph. Thank you for your time, and I'd be glad to take your questions.

---

## Slide 21 — Q&A

`[Stay on this slide. Breathe. Listen to the whole question before answering.]`

---

### Likely questions — quick anchors

- **"Isn't this just a lot of features?"** → No — every component answers one of the seven documented gaps, and all of it traces back to the single flaw VERA proved: flat retrieval can't see cross-document relationships.
- **"Why not just improve VERA?"** → VERA already does hybrid vector+BM25 with RRF. The ceiling is architectural — embeddings can't represent relationships between entities. You can't tune your way past it; you need a graph.
- **"GraphRAG is expensive — is it worth it?"** → That's exactly what my benchmark tests. LightRAG shows the cost is largely recoverable, and my evaluation quantifies the accuracy gain against that cost.
- **"Is the scope realistic for FYP2?"** → Two of four objectives are already done end-to-end. What remains is training the ML Engines and finishing GenUI integration — both are designed and scoped, with implementation as the immediate next phase.
- **"How do you know it's better, not just different?"** → The RAGAS-gated benchmark against the flat baseline, on a held-out multi-hop question set finalised with my supervisor.
- **"Is the ML Engine training pipeline actually built?"** → The design is locked — one shared `Engine` interface all three engines implement — but no training run has completed yet. That's explicitly the next build phase, not a claim I'm making today.
- **"Your Objective slide lists GenUI before Agents — doesn't that break your own logic where GraphRAG enables agents, which enables the UI?"** → The numbering there is presentation order, not dependency order. Architecturally GraphRAG is the foundation both sit on: agents produce the typed output the UI renders, so the build sequence is GraphRAG → Agents → ML → GenUI regardless of the slide layout.
