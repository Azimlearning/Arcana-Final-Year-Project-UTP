---
tags: [concept, decision, static]
source: concept/FYP_Context_Document.md §14
---

# Key Decisions Made (Proposal Stage)

1. Project name still WIP at this stage — NEXUS / GraphMind / Aether were working titles only (superseded — see [[ContinuityNotes]] for current naming status).
2. Student chose to proceed with the **full project scope** despite the [[LLMCouncilAssessment|LLM council's]] scope-down warning.
3. Primary benchmark = self-built flat RAG baseline (not NotebookLM as a controlled experiment); NotebookLM is informal secondary comparison only.
4. Evaluation dataset = 20 multi-document questions with known correct answers requiring cross-document reasoning, to be designed in FYP1.
5. NetworkX for the FYP1 PoC; decide on Neo4j for FYP2 based on scale (later resolved — Neo4j migration deferred to P2, per `checklist.md` §2.2).
6. Minimum FYP2 deliverable at proposal time: 3 agents (Research, Learning, Writing) + 2 UI modes (Research, Study) + graph-hybrid RAG benchmark — since expanded substantially (PRD targets 15+ agents, 5 modes).
7. VERA AI treated as the FYP's own prior-work baseline — reuse frontend architecture, embedding model, deployment patterns rather than starting from zero.
