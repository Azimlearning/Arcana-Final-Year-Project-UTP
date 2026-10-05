---
tags: [concept, decision, static]
source: concept/FYP_Context_Document.md §9
---

# LLM Council Assessment Summary

Project run through a 5-advisor LLM council (Contrarian, First Principles, Expansionist, Outsider, Executor) with peer review.

**All advisors agreed:** GraphRAG core is genuinely novel and academically defensible; scope is too wide as originally stated for a solo 2-semester developer; evaluation design was underdeveloped (fixed as first-class from day 1 — see [[KeyDecisions]]); entity extraction quality is the load-bearing technical risk.

**Key clashes & resolutions:**
- Scope (cut hard vs. build all) → build the tight version for the grade (3 agents, 2 UI modes, NetworkX for PoC); open-source the full vision post-graduation.
- Adaptive UI (contribution vs. distraction) → kept as the implementation vehicle for the user study, not a standalone research contribution.
- NotebookLM as benchmark → self-built flat RAG is the primary benchmark; NotebookLM is an informal secondary comparison only.

**Blind spots identified:** gold-standard evaluation dataset problem (need 20 cross-document Qs with known answers, designed in FYP1 before building); supervisor-expertise dependency (framing needs calibration to supervisor's NLP/AI vs Systems background); VERA AI baseline was underused; NetworkX-vs-Neo4j tradeoff (NetworkX for PoC, decide at FYP2 start based on scale).

**Final verdict — commit to the project, restructure around one falsifiable claim:**
> "Graph-augmented hybrid retrieval produces measurably superior cross-document reasoning compared to flat vector RAG in an academic research context."

**The one thing to do first:** draft 20 multi-document questions with known correct answers before writing a single line of code.
