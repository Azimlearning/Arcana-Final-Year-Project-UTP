# Beyond Superficial Tests: Adversarial Refinement for Reliable Property-Based Testing

**Xiao Li, Runlin Liu, Zhe Zhang, Xiang Gao & Hailong Sun** · 2026 · **Findings of ACL 2026**,
pp. 13957–13974, San Diego
**DOI:** 10.18653/v1/2026.findings-acl.683 · ACL Anthology: 2026.findings-acl.683
**Domain:** Adversarial verification of generated code · **Verified:** ✅ full bibliographic record
confirmed — venue, pages, DOI, complete author list
**Priority:** ⭐ peer-reviewed anchor for the adversarial-verification claim

## What it does
Names the **"superficiality gap"**: LLMs readily generate syntactically valid tests, but struggle to
bridge implementation and intended invariant logic, producing weak properties that give a false
sense of security.

PROBE treats test generation as a **game of semantic asymmetry**. A Validator agent actively
generates **counter-implementations** — deliberately incorrect code that nonetheless satisfies the
generated property — to expose loopholes in the specification itself. It also builds a
cross-functional semantic graph to catch dependencies local analysis misses.

Results: +9.79% mutation score over baselines, and 45 previously unknown bugs found in top-tier
libraries, confirmed by maintainers.

## Why it matters to Synapse
This is the citation that should carry the adversarial-verification argument, for one decisive
reason: **it is peer-reviewed at ACL**, while most of the adversarial-verification literature from
2026 is arXiv-only preprints with no citation history. Reviewers weigh that. Lead with PROBE and use
AdverMCTS and the red-teaming work as supporting evidence rather than the other way round.

Substantively, the counter-implementation idea is the sharpest available articulation of why a
passive checker is insufficient. A verifier that only asks "does this look right?" will approve
plausible-but-wrong output. A verifier that actively tries to construct a way for the output to be
wrong while still passing is doing something categorically different. That is the design principle
behind Synapse's Verifier, and PROBE gives it a name and an empirical result.

The "false sense of security" phrase transfers directly to the education setting — a generated
simulation that renders smoothly conveys exactly that false confidence to a student.

## The gap it leaves
Software correctness against specifications and invariants, not **pedagogical** correctness. A
physics simulation can be free of software defects and still teach the wrong model — there is no
unit test for "this misrepresents the Doppler effect." Extending adversarial verification from code
properties to domain/conceptual correctness is genuinely open, and is where Synapse's Verifier
prompt design sits.

That gap is worth stating explicitly in the paper: it is the honest boundary of the contribution,
and stating it preempts the obvious reviewer objection.

## How to cite it
Related Work (verification paragraph) and Method (justifying the adversarial design over a passive
checker). The strongest venue in the verification group — treat it as the primary citation there.
