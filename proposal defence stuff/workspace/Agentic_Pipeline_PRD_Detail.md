# Arcana — PRD-Grounded Detail for the Agentic Pipeline / Architecture Slide Cluster

Everything below is pulled directly from `Arcana/docs/arcana_prd.md` §8, §11-14 (no invented facts).
Section 0 is a correction you need to see before anything else. Section 1-4 is the exhaustive
reference. Section 5 is the actual slide content recommendation, condensed from that reference.

---

## 0. Correction needed on the already-confirmed "Agents & Tools" slide

The currently-confirmed Agents & Tools slide content says:

> "Checklist-confirmed built: 15+ agents, including learning, writing, socratic, discovery, graph,
> **literature, contradiction, comparator, timeline**, and annotation agents."

The PRD's actual 25-agent roster (§12) has **no** Literature Agent, Contradiction Agent, Comparator
Agent, or Timeline Agent. Those are *tool methods* belonging to other agents:
- `cross_document_compare` and `detect_contradictions` → tools on the **Research Agent**
- `build_literature_review` → a tool on the **Writing Agent**
- `render_timeline` → a tool on the **Visual Agent**

This needs fixing before it's cascaded — naming them as standalone agents isn't accurate to your own
PRD. The corrected slide content is in §5.2 below.

---

## 1. The Full 25-Agent Roster (PRD §12)

**Phase tags:** P0 = FYP1 PoC · P1 = FYP2 MVP (target 15+ built) · P2 = post-FYP roadmap to the full 25.

### TIER 1 — Orchestration (1 agent)

| Agent | Phase | Role | Key tools |
| --- | --- | --- | --- |
| **Orchestrator** | P0 | Single entry point; classifies intent/mode, decomposes into a plan, dispatches specialists, never answers itself | `detect_mode`, `route_to_agent`, `sequence_agents`, `assemble_response` |

### TIER 2 — Core Intelligence (8 agents)

| Agent | Phase | Role | Key tools |
| --- | --- | --- | --- |
| **Research** | P0 | Flagship cross-document reasoner: synthesis, comparison, contradiction detection, gap analysis, always grounded and cited | `hybrid_retrieve`, `cross_document_compare`, `detect_contradictions`, `find_research_gaps`, `summarise_with_grounding`, `cite_sources` |
| **Graph** | P0 | Knowledge-graph specialist: traversal and the four graph algorithms; usually called *by* other agents | `graph_expand`, `find_shortest_path`, `detect_communities` (Louvain), `find_bridge_concepts` (betweenness, P2), `pagerank_concepts`, `detect_entity_contradictions` |
| **Learning** | P1 | Turns corpus material into study artifacts and schedules their review; engine behind Study mode | `generate_flashcards`, `generate_quiz`, `feynman_explain`, `cornell_notes`, `assess_knowledge_gap`, `schedule_spaced_review`, `generate_blurting_prompt`, `create_interleaving_set` (P2) |
| **Writing** | P1 | Produces grounded written work and checks it against the user's corpus; engine behind Writing mode | `draft_section`, `generate_outline`, `build_literature_review`, `check_consistency`, `generate_annotated_bibliography`, `get_document_outline` |
| **Socratic Tutor** | P1 | Teaches by asking, never telling; guides via probing questions and misconception detection | `generate_probing_question`, `assess_understanding`, `build_bloom_assessment`, `scaffold_hint`, `evaluate_misconception` |
| **Discovery** | P1 | Surfaces non-obvious, serendipitous cross-document connections; engine behind Exploration mode | `surface_cross_document_link`, `generate_insight_card`, `detect_serendipitous_connection`, `rank_novelty` |
| **Methodology** | P2 | Advises on research design, methodology comparison, sample size, evaluation metrics | `recommend_research_design`, `compare_methodologies`, `estimate_sample_size`, `suggest_evaluation_metrics`, `generate_methodology_template` |
| **Debate** | P2 | Stress-tests arguments: counterarguments, steelmanning, counter-evidence, simulated peer review | `generate_counterargument`, `build_steelman`, `find_counter_evidence`, `simulate_peer_review` |

### TIER 3 — Output Generation (5 agents)

| Agent | Phase | Role | Key tools |
| --- | --- | --- | --- |
| **UI Agent** | P1 | Terminal node; the *only* agent that chooses presentation/layout | `select_output_components`, `determine_layout`, `get_user_preferences`, `adapt_complexity_level` (P2), `stream_component_block` |
| **Citation** | P1 | Formats and exports citations/bibliographies in academic styles | `format_citation`, `export_bibtex`, `export_ris`, `sync_zotero` (P2), `detect_citation_style` |
| **Visual** | P1 | Produces typed data structures for visual components (maps, charts, timelines, tables, graph views) | `render_concept_map`, `render_comparison_chart`, `render_timeline`, `render_data_table`, `render_knowledge_graph_view` |
| **Document** | P1 | Generates downloadable file artifacts with provenance preserved | `generate_pdf_report`, `generate_docx`, `generate_slide_deck` (P2), `export_literature_matrix`, `export_obsidian_vault` |
| **Audio** | P2 | Audio overviews, TTS, podcast scripts, spoken flashcards (roadmap-only, out of graded scope) | `generate_audio_summary`, `text_to_speech`, `generate_podcast_script`, `generate_spoken_flashcards` |

### TIER 4 — Quality & Meta (11 agents)

| Agent | Phase | Role | Key tools |
| --- | --- | --- | --- |
| **Fact Checker** | P1 | The guardrail: verifies generated claims are grounded before reaching the user | `verify_claim`, `check_citation_accuracy`, `flag_hallucination`, `cross_reference_sources` |
| **Annotation** | P1 | Captures user highlights/notes and folds them back into the knowledge graph | `add_user_annotation`, `enrich_graph_node`, `link_user_note_to_entity`, `capture_highlight` |
| **Memory** | P1 | Continuity layer: loads/saves profile, history, session context, learning progress; runs first every turn | `get_user_profile`, `retrieve_session_context`, `update_interaction_history`, `track_learning_progress`, `store_user_preference` |
| **Ingestion** | P0 | Agent-facing wrapper around the ingestion pipeline; lets sources be added mid-conversation | `parse_document`, `extract_entities_relationships`, `chunk_and_embed`, `ocr_scan`, `parse_youtube_transcript` |
| **Web Search** | P1 | Academic paper discovery only, **not** general web search | `search_semantic_scholar`, `search_arxiv`, `search_google_scholar`, `fetch_citation_network`, `recommend_related_papers` |
| **Study Planner** | P1 | Schedules study time, manages Pomodoro, tracks deadlines, sends review reminders | `generate_study_schedule`, `create_pomodoro_session`, `track_deadline`, `forecast_workload`, `send_review_reminder` |
| **Analytics** | P1 | Measures what the FYP is graded on; produces evaluation evidence + user-facing progress dashboard | `measure_retrieval_quality`, `track_study_effectiveness`, `generate_progress_dashboard`, `compute_retention_rate` |
| **Plagiarism** | P2 | Originality + AI-content checks, uncited-passage flagging | `check_originality`, `detect_ai_content`, `flag_uncited_passage`, `suggest_citation` |
| **Grammar & Style** | P2 | Grammar, readability, journal-readiness, style suggestions | `check_grammar`, `score_readability`, `assess_journal_readiness`, `suggest_style_improvement` |
| **Paraphrase** | P2 | Rewrites for complexity/length/register/audience without losing meaning or provenance | `rewrite_complexity`, `reduce_word_count`, `academify_text`, `simplify_for_audience` |
| **Export** | P2 | Bulk import/export and third-party sync (Drive, Anki, Obsidian) | `bulk_import`, `sync_google_drive`, `export_anki_deck`, `export_obsidian`, `batch_export` |

**Composability matrix (PRD §12.6):** Writing → Research, Fact Checker, Citation · Research → Graph,
Fact Checker · Learning → Research, Graph · Socratic Tutor → Graph, Learning · Discovery → Graph ·
Orchestrator → any agent · UI Agent → terminal, calls no one.

---

## 2. GraphRAG / Hybrid Retrieval Core (PRD §8, §10, §12 Graph Agent)

- **Ingestion:** parse → chunk → embed (OpenAI `text-embedding-3-large`, 3072-dim) → extract
  entities/relationships into the knowledge graph.
- **Storage:** `GraphStore` abstraction — NetworkX (P0 prototype, in-process) / Neo4j Community (P1
  production target) — so swapping backend is a one-line config change.
- **Four graph algorithms (all behind the same `GraphStore` ABC):**
  - `detect_communities()` — Louvain community detection (FR-KG-04)
  - `pagerank_concepts()` — node importance (FR-KG-05)
  - `find_bridge_concepts()` — betweenness centrality (FR-KG-06, deferred to P2)
  - `find_shortest_path()` — the "how are X and Y related" answer
- **Hybrid retrieval:** dense vector (Pinecone) + BM25 (sparse keyword) + graph traversal, fused via
  Reciprocal Rank Fusion (`rrf_k = 60`).
- **Re-Rank Engine:** optional trained post-RRF step (gradient-boosted trees over BM25/cosine/
  graph-hop-distance/RRF-rank features); designed, not yet trained [PLACEHOLDER].
- **Why it matters most:** this is the core technical premise the whole FYP is graded on — Objective 1
  and the primary success metric (PRD §4.3) are both "does graph-augmented retrieval beat flat
  vector-RAG on cross-document questions."

---

## 3. GenUI Protocol & 24-Component Catalog (PRD §13-14)

- **UIBlock protocol:** a tagged union `{ type, data, meta }` — `type` names a catalog component,
  `data` matches its typed schema, `meta` carries panel/ordering/complexity hints. Defined once in
  `packages/schema`, shared by backend and frontend. Modelled in the spirit of Google's A2UI protocol,
  delivered via the Vercel AI SDK's streaming of React Server Components.
- **Streaming lifecycle (5 steps):** agent emits block → server validates (fail closed) → server
  streams as SSE event → client resolves `type` via the registry, mounts a skeleton → client hydrates
  as data arrives.
- **Security property (NFR-SEC-04):** agents never emit executable code, only data conforming to a
  known schema — a model can never inject markup or script.

### The 24-Component Catalog

| Component | Purpose | Produced by |
| --- | --- | --- |
| `CitedSummary` | Grounded answer with inline source citations | Research |
| `LiteratureMatrix` | Papers × dimensions comparison grid | Research |
| `ContradictionAlert` | Flags where sources disagree on a concept | Research / Graph |
| `GapAnalysis` | What the corpus does not cover | Research |
| `InsightCard` | A surfaced serendipitous cross-document link | Discovery |
| `KnowledgeGraphView` | Interactive graph of entities and edges | Graph / Visual |
| `ConceptMap` | Concept-relationship map for reasoning | Visual / Socratic |
| `ComparisonChart` | Chart of structured comparative data | Visual |
| `Timeline` | Chronological event view | Visual |
| `DataTable` | Sortable structured table | Visual |
| `FlashcardDeck` | Active-recall cards with SR scheduling | Learning |
| `QuizCard` | MCQ / short-answer question item | Learning |
| `BlurtingPrompt` | Free-recall prompt + comparison to source | Learning |
| `FeynmanExplainer` | Simplified explanation + flagged gaps | Learning |
| `CornellNotes` | Cue / notes / summary structured note | Learning |
| `SocraticDialog` | Guided questioning that withholds answers | Socratic Tutor |
| `StudyPlanner` | Schedule, Pomodoro and review queue | Study Planner |
| `DraftEditor` | Editable grounded draft with citations | Writing |
| `CitationPreview` | Formatted citation in chosen style | Citation |
| `PlagiarismReport` | Originality and AI-content flags | Plagiarism |
| `BibliographyExport` | BibTeX / RIS export panel | Citation |
| `SourceList` | The notebook's ingested sources | Ingestion |
| `ProgressDashboard` | Learning-progress and retention metrics (the "dashboard") | Analytics |
| `AudioSummary` | Player for an audio overview (P2) | Audio |

- **UI Agent's decision:** the only agent that selects components, assigns panels, computes panel
  widths. Layout is computed at runtime, so the interface space is effectively unbounded, the 5
  modes are samples, not a fixed menu.
- **5 demonstrated modes** (Sources / Chat / Studio panel split + streamed components):
  - **Research** (~20/45/35): `CitedSummary`, `LiteratureMatrix`, `ContradictionAlert`
  - **Study** (collapsed/~45/expanded): `FlashcardDeck`, `QuizCard`, `BlurtingPrompt`
  - **Writing** (sources/maximised/hidden): `DraftEditor`, `CitationPreview`, `PlagiarismReport`
  - **Socratic** (sources/dialog/concept graph): `SocraticDialog`, `FeynmanExplainer`, `ConceptMap`
  - **Exploration** (hidden/narrow/full-canvas graph): `InsightCard`, `GapAnalysis`
- **4 required states per component:** Empty (clear call-to-act), Loading (skeleton), Partial
  (streaming in), Error (plain-language cause + retry).
- **Frontend:** Next.js 14 App Router, TypeScript, Tailwind CSS; 3-panel adaptive shell
  (Sources/Chat/Studio); component registry (`type → component` map, one-line additions); Zustand
  stores (`uiStore`, `sessionStore`, `blockStore`); layout is agent-suggested but user-overridable
  (FR-UI-07).

---

## 4. ML Engines (recap, already established elsewhere in the deck)

- **Re-Rank Engine** (P1): gradient-boosted trees over BM25/cosine/graph-hop-distance/RRF-rank
  features, optional post-RRF step. Not yet trained [PLACEHOLDER].
- **Mastery Engine** (P2): Half-Life Regression for recall-probability, swappable vs SM-2. Not yet
  trained [PLACEHOLDER].
- **Document Classifier Engine** (P2): lightweight TF-IDF/linear classifier over existing embeddings.
  Not yet trained [PLACEHOLDER].
- All three share one `Engine` interface (`predict()`, `is_available()`) for graceful degradation.

---

## 5. Recommended slide content (condensed from the reference above)

### 5.1 AGENTIC PIPELINE (the slide you asked about)

**Title:** AGENTIC PIPELINE

**Body:**
1. **Mechanism:** AgentState is the single shared ledger, every agent appends its contribution and nothing overwrites another agent's output; agents compose only through route_to_agent, which enforces a hop budget and a per-turn token budget, never direct module imports; intent-scoped tool injection caps every agent at max_tools_per_prompt = 12.
2. **The 25-agent suite, 4 tiers:** Orchestration (Orchestrator) → Core Intelligence (Research, Graph, Learning, Writing, Socratic Tutor, Discovery, Methodology, Debate) → Output Generation (UI Agent, Citation, Visual, Document, Audio) → Quality & Meta (Fact Checker, Annotation, Memory, Ingestion, Web Search, Study Planner, Analytics, Plagiarism, Grammar & Style, Paraphrase, Export). 15+ confirmed built across P0/P1; the remainder are scoped P2.
3. **GraphRAG at the core:** every Research/Learning/Socratic/Discovery task routes through the Graph Agent for knowledge-graph traversal (Louvain communities, PageRank, shortest path) and the hybrid retrieval pipeline (dense vector + BM25 + graph traversal, fused via Reciprocal Rank Fusion), this is what makes the agents "graph-native" rather than flat-RAG wrappers.
4. **GenUI termination:** every path ends at the UI Agent, the only agent that selects from the 24-component catalog and emits a typed UIBlock {type, data, meta}, streamed over SSE and rendered via the component registry into the adaptive 3-panel dashboard.

**Footer:** 2026 | Universiti Teknologi PETRONAS

*(This is denser than a normal bullet slide. Given the volume, consider a 2x2 grid layout: Mechanism / Agent Roster / GraphRAG / GenUI as four quadrants, rather than 4 long bullets.)*

### 5.2 AGENTS & TOOLS (corrected)

**Title:** AGENTS & TOOLS

**Body:**
1. Target suite: 25 agents across 4 tiers (Orchestration 1, Core Intelligence 8, Output Generation 5, Quality & Meta 11).
2. Checklist-confirmed built (15+): Orchestrator, Research, Graph, Learning, Writing, Socratic Tutor, Discovery, Ingestion (P0/P1 tagged in the PRD).
3. Also confirmed: UI Agent, Citation, Visual, Document (Output tier); Fact Checker, Annotation, Memory, Web Search, Study Planner, Analytics (Quality & Meta tier).
4. Deferred to P2: Methodology, Debate, Audio, Plagiarism, Grammar & Style, Paraphrase, Export.
5. Every agent follows one template: subclass BaseAgent, expose tools via @tool, read AgentState without mutating upstream slots, never emit raw HTML or pick UI components.

*(Replaces the old bullet 2 that incorrectly named "literature, contradiction, comparator, timeline" as standalone agents — those are tool methods on Research/Writing/Visual, not agents.)*

### 5.3 GENERATIVE UI (expanded)

Keep existing 4 bullets, optionally add the full mode table (5.3 above) as a visual table if the slide layout allows, since the PRD treats this table as central to explaining "what GenUI actually means."

---

*Source: `Arcana/docs/arcana_prd.md` §8, §11-14, §12.6. No facts invented; anything not explicitly in the PRD (e.g. exact training data sizes for ML Engines) remains flagged [PLACEHOLDER] per your standing no-fabrication rule.*
