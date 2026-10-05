# AlignUI: A Method for Designing LLM-Generated UIs Aligned with User Preferences

**Liu, Sra & Xiao** · 2026 · arXiv:2601.17614 (24 Jan 2026), cs.HC
**Domain:** Generative UI — alignment · **Verified:** ✅ arXiv abstract page confirmed
**Priority:** supporting

## What it does
Aligns LLM-generated interfaces with user tasks and preferences using a crowdsourced preference
dataset — 50 general users, 720 UI-control preferences across eight image-editing tasks. Generation
is multi-stage: the LLM finds dataset tasks similar to the user's task, matches the user's stated
preference, then reasons out UI controls that fit both. Evaluated by generating UIs for six unseen
tasks and running a study with 72 additional users.

## Why it matters to Synapse
Two uses, both secondary.

First, it shows the generative-UI field is already past "can we do it" and into "can we make it fit
the person" — useful for establishing that this is an active research area with real methodological
standards, not a novelty.

Second, the evaluation design is worth copying in structure: build on a fixed task set, hold out
unseen tasks, evaluate with non-expert raters. That is a realistic shape for a small study.

The preference-alignment angle itself is *not* Synapse's contribution and should not be oversold —
Synapse aligns to correctness, not taste.

## The gap it leaves
Alignment to preference says nothing about correctness. A UI can match a user's stated preferences
perfectly and still be wrong. In an image-editing task that is a usability issue; in a science
lesson it is a misconception. The paper's domain (image editing) has no ground truth to violate,
which is exactly what makes education different.

## How to cite it
Related Work, generative-UI paragraph — one clause alongside CrowdGenUI, establishing the alignment
line of work, then the pivot: *this line optimises for preference, not correctness.*
