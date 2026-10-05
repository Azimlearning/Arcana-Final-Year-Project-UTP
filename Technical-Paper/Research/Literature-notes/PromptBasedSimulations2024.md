# AI-Generated Simulations of Physical Phenomena (Prompt-Based Simulations)

**Authors not confirmed** · 2024 · arXiv:2412.07482 (Dec 2024)
**Domain:** LLM-generated science simulations · **Verified:** ⚠️ **title and authors not returned by
search — verify both directly on arXiv before citing**
**Priority:** ⭐ strongest motivation for the verifier

## What it does
Presents prompt templates that get ChatGPT and Claude to produce interactive HTML/JS physics
simulations — simple pendulum, 2D Ising model, random walker — with sliders, start/pause/reset
controls and live graphs, requiring no programming skill from the educator. Argues this
democratises simulation creation and adds value as a reflective, metacognitive activity for
students.

Critically, it documents the **iterative human debugging loop** required to get there. Their worked
example is a real transcript of correcting Claude 3.5 Sonnet:

> "Fix the analytical graph. There is a problem with the analytical solution shown — it displays a
> period that is exactly half of the correct time."

and they conclude that "some corrections through human supervision typically remain necessary."

## Why it matters to Synapse
This is the problem statement, in the authors' own words and with a concrete failure.

An LLM produced a physics simulation that *ran*, *rendered*, and *looked right* — and had the wrong
period. No syntax error, no crash, nothing a smoke test would catch. A student using it would have
learned incorrect physics with full confidence. This is precisely the failure mode Synapse's
adversarial verifier exists to catch, described by researchers who hit it and had to fix it by hand.

Cite this as **the problem, never the solution**. The framing writes itself: prior work establishes
that LLMs can generate educational physics simulations but requires a human expert in the loop to
catch silent conceptual errors; Synapse automates that loop.

Pair it with AdverMCTS's term **pseudo-correctness** — passing visible checks while failing the
underlying logic. The wrong-period pendulum is pseudo-correctness in a science-education setting.

## The gap it leaves
No automated verification whatsoever. Correctness depends entirely on an expert noticing. That does
not scale past a motivated physics educator, and it certainly does not survive a student asking a
question nobody has vetted.

## How to cite it
Introduction (motivation) and Method (justifying the Verifier's existence). If you use the
wrong-period example explicitly, quote it — a concrete failure is far more persuasive than a general
claim about hallucination. **Verify the citation details first.**
