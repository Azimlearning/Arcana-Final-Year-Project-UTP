# LearnMate²: Design and Evaluation of an LLM-powered Personalized and Adaptive Support System for Online Learning

**Authors per DIS '26 listing (confirm names)** · 2026 · **ACM DIS 2026** · arXiv:2605.06257
**Domain:** LLM systems in education — evaluation design · **Verified:** 🟡 DIS programme entry +
arXiv abstract confirmed; author list not captured
**Priority:** supporting — methodological template

## What it does
Three coordinated components forming a closed learning loop: **PlanMate** (personalised study plans
across goals, time, pace, path), **StudyMate** (real-time contextual assistance with progressive
disclosure and adaptive quizzes), **AdaptMate** (adjusts plans from quiz performance and
interaction patterns). Evaluated in two rounds — a preliminary study (n=24) that drove refinements,
then an evaluation (n=16) against a combined baseline of a state-of-the-art online learning platform
plus an LLM. Reports gains in both learning outcomes and user experience.

## Why it matters to Synapse
Almost entirely methodological, and valuable for that reason.

It is a **peer-reviewed ACM venue** publishing a system evaluation with n=16 in the main study.
That is the single most useful fact in this note: it establishes that a small-n system evaluation
against a sensible baseline is publishable at a good venue, which is directly relevant given the
5-day timeline and no user study in hand.

The baseline design is worth copying too — not "our system vs nothing," but **our system vs the
realistic alternative the student would otherwise use**. For Synapse that means: generated
interactive artifact vs a plain LLM text explanation of the same question. That baseline is free,
honest, and exactly the comparison a reviewer will want.

## The gap it leaves
Personalisation and scheduling, not content generation. LearnMate² adapts *around* fixed course
material; it never generates the instructional artifact itself, so questions of generated-content
correctness never arise.

## How to cite it
Evaluation section, when justifying study design and n. Optionally one clause in Related Work as an
example of LLM-driven adaptive learning support that stops short of generating the material.
