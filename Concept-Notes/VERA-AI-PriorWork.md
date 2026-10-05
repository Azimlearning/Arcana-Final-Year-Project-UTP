---
tags: [concept, static]
source: concept/FYP_Context_Document.md §2
---

# VERA AI — Prior Work (Internship Baseline)

Enterprise-grade RAG-powered knowledge base assistant built for PETRONAS Upstream (BPI Unit) during a 7-month SIP. Arcana explicitly extends this baseline — see [[ExtendsVERA-Comparison]].

**Key results (14-week pilot):** retrieval time 15–30 min → <5s (95% gain); content creation turnaround −90%; citation accuracy 94%; AI-content acceptance 82% first-pass; local image generation (privacy).

**Architecture:** Hub-and-spoke topology; hybrid inference (cloud LLM for text, local Stable Diffusion for images); "No Citation, No Answer" policy.

**RAG pipeline:** vector search (cosine, 3072-dim) → BM25 keyword search → Reciprocal Rank Fusion → adaptive top-k.

**6 specialised agents:** Analytics (forecasting), Meetings (transcription→briefs), Podcast (audio scripts), Content (drafting), Visual (image tagging/infographics via local Stable Diffusion), Quiz (assessments).

Repo: `https://github.com/Azimlearning/VERA-AI` (see [[ContinuityNotes]]).
