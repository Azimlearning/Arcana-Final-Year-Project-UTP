# The Missing Layer: Why EdTech Needs Design-Time Generative UI, Not Just Runtime Personalization

**Neshaei, Shibu & Güreş** · 2026 · arXiv:2606.15902 (Jun 2026)
**Domain:** Generative UI in education — position paper · **Verified:** 🟡 abstract + full body text
confirmed
**Priority:** ⭐⭐ the objection the paper answers

## What it does
A position paper arguing that the dominant runtime-GenUI paradigm in EdTech is wrong. Their case:
runtime adaptation operates on content already locked into a modality, pushes per-learner inference
costs onto low-resource deployments, and — the load-bearing claim —

> "might lead to inaccurate learning content due to the **inability to conduct verification at
> scale**"

and at runtime "errors may be exposed directly to learners," because the domain-knowledgeable
instructor is no longer in the loop at the moment generation happens.

Their alternative: a **card-based authoring-time paradigm**. Content is encoded as
modality-agnostic semantic units; GenAI produces several interface representations (interactive,
audio-first, simplified text, low-bandwidth) at design time; the instructor verifies before anything
reaches a learner. They cite MAIC-UI as the encouraging early example.

## Why it matters to Synapse
This is the single most useful paper in the set, because it is a **named, published, 2026 argument
that what Synapse does is unsafe** — and Synapse's architecture is a direct answer to it.

Their claim is that runtime generation cannot be verified at scale. Synapse's adversarial verifier
plus structural delivery gate is precisely a mechanism for verifying at scale at runtime. So the
disagreement is not vague positioning; it is a concrete architectural dispute with a testable
resolution.

That gives the paper a thesis instead of a system description:

> Prior work argues runtime generative UI is pedagogically unsafe because generated content cannot
> be verified at scale before reaching learners. We show this is an architectural limitation rather
> than a fundamental one: by making verification a structural precondition of delivery rather than a
> review step, request-time generation retains the safety property that authoring-time review
> provides.

Handle it with respect, not dismissal. Their cost argument (per-learner inference) is correct and
you should concede it in Limitations — Synapse *is* more expensive per learner than a cached
authored artifact. Your counter is coverage: authoring time cannot anticipate every question.

## The gap it leaves
It treats verification-at-scale as impossible rather than as an open engineering problem, and
offers no mechanism that would make runtime verification safe. It is a position paper — no system,
no evaluation. That is the opening.

## How to cite it
Introduction (as the stated objection), Related Work (as the counterposition), and Limitations
(conceding the cost argument). Arguably the most important single citation for framing the
contribution.
