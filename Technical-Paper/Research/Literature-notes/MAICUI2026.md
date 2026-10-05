# MAIC-UI: Making Interactive Courseware with Generative UI

**THU-MAIC group** · 2026 · arXiv:2604.25806 · github.com/THU-MAIC/MAIC-UI
**Domain:** Generative UI in education · **Verified:** 🟡 abstract + body confirmed, authors not
individually confirmed
**Priority:** ⭐⭐ closest prior art — must cite and differentiate

## What it does
A zero-code authoring system letting educators build interactive STEM courseware from textbooks,
PPTs and PDFs. Three technical contributions:

1. Structured knowledge analysis with multi-modal understanding (documents up to 50 pages) for
   pedagogical rigour.
2. A **two-stage generate-verify-optimize pipeline** — stage 1 produces content-aligned interactive
   simulations, stage 2 applies visual polish, layout verification, theming.
3. Click-to-Locate editing with unified-diff incremental generation, cutting edit cycles from
   200–600s to under 10s.

Evaluated with a controlled lab study (n=40: 4.9 vs 7.0 editing iterations, better learnability and
controllability than direct text-to-HTML) and a **three-month classroom deployment** (n=53 high
school students; pilot class +9.21 points in STEM vs −2.32 in control).

## Why it matters to Synapse
This is the uncomfortable one. A published 2026 system that generates interactive science
simulations through a *generate-verify* pipeline, with a real classroom deployment and real learning
gains. If a reviewer knows this paper and it is not in your Related Work, the paper is rejected —
not for overlap, but for apparent unawareness of the field.

Cited properly it becomes an asset rather than a threat, because the differentiation is genuine:

| | MAIC-UI | Synapse |
|---|---|---|
| Who triggers generation | Teacher, authoring time | Learner, request time |
| Input | Textbook / PPT / PDF | A natural-language science question |
| Verification | Quality and layout optimisation stage | Adversarial verifier with revision retries |
| Safety property | Human review before delivery | **Structural** — delivery requires a type only the verifier can mint |
| Coverage | What the teacher authored | Arbitrary student question |

The deployment numbers are also the honest benchmark for what a *strong* evaluation looks like here.
You will not match a three-month classroom study before 20 August, and should not pretend to.

## The gap it leaves
MAIC-UI keeps the human in the loop by design — the teacher reviews before students see anything.
It therefore never answers whether generation can be safe **without** that review, which is the only
way to cover a question the teacher did not anticipate. Coverage is bounded by authoring effort.

## How to cite it
Related Work, the education-GenUI paragraph — as the closest system, followed explicitly by the
authoring-time vs request-time distinction. Also in Evaluation, as context for why your n is
smaller.
