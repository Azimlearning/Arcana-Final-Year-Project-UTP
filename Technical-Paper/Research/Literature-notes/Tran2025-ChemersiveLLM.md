# ChemersiveLLM: Prompt-to-VR Simulation of Chemistry Experiments Using Generative AI

**Tran, Huynh, Poor, Tran & Nguyen** · 2025 · **ACM VRST '25** (31st ACM Symposium on Virtual
Reality Software and Technology), Montreal, 12–14 Nov 2025
**DOI:** 10.1145/3756884.3770535
**Domain:** LLM-generated science simulations · **Verified:** ✅ ACM DOI and venue confirmed

> ⚠️ Naming collision: the FYP review already contains a `Tran2025` (AdaptOrch, arXiv:2602.16873).
> Different authors, different paper. Keep the identifiers distinct in the bibliography.

## What it does
A VR chemistry-lab platform where the learner supplies only a lesson title and target language, and
an LLM generates the full experiment specification as structured JSON — chemicals, tube positions,
volumes, procedural steps — constrained by predefined rules (valid quantity ranges, maximum tube
counts, banned terms). A semantic action-mapping framework binds that JSON to interactive Unity/Meta
Quest 2 objects.

Within-subjects study, n=20, three conditions: traditional materials, ChatGPT chatbot learning, and
ChemersiveLLM. Cronbach's α > 0.94; repeated-measures ANOVA p < 0.001, with ChemersiveLLM
consistently outperforming both baselines on engagement, comprehension and satisfaction.

## Why it matters to Synapse
Two contributions, one methodological and one rhetorical.

**Methodological:** the three-condition design — *traditional / chatbot / generated-interactive* —
is the right comparison structure for Synapse, and it comes with a published precedent at an ACM
venue. The middle condition is what makes it good: comparing against a plain LLM chatbot isolates
the contribution of the generated interactive artifact rather than of the LLM in general.

**Rhetorical:** their stated limitation is your contribution.

> "the system still has limits, especially in controlling AI outputs and avoiding hallucinations, so
> **expert review remains essential**."

That is the third independent paper in this set (with the prompt-based simulations work and the
Missing Layer position paper) whose conclusion is that generated educational content needs a human
to check it. Three separate 2024–2026 papers naming the same unsolved problem is a far stronger
motivation than any single citation.

Their constrained-JSON approach is also a useful contrast: they achieve safety by narrowing the
output space to a rigid schema, which caps what can be expressed. Synapse keeps the output space
open (arbitrary HTML/JS) and moves safety to verification instead. That is a real architectural
trade-off worth one sentence.

## The gap it leaves
Safety by schema restriction, so expressiveness is bounded by what the JSON spec anticipates — the
same coverage ceiling MAIC-UI has, reached by a different route. Hallucination control is
acknowledged as unsolved. Requires a Meta Quest 2, which limits deployability in exactly the
under-resourced contexts a Malaysian education framing cares about.

## How to cite it
Related Work (generated science simulations), Evaluation (three-condition design), and Introduction
(the "expert review remains essential" quote, as part of the stacked motivation).
