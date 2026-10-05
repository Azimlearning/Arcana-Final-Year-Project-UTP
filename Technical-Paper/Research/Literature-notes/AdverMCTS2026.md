# AdverMCTS: Combating Pseudo-Correctness in Code Generation via Adversarial Monte Carlo Tree Search

**Authors not confirmed** · 2026 · arXiv:2604.10449v1
**Domain:** Adversarial verification of generated code · **Verified:** 🟡 abstract and method
confirmed; authors not established
**Priority:** supporting — but the terminology is valuable

## What it does
Frames robust code generation as a **minimax game** between a Solver agent that synthesises
candidates and an Attacker agent that evolves targeted corner-case tests exposing logical
divergence among them. Discovered tests accumulate into a progressively hostile global filter;
candidates must pass the whole accumulated suite to enter the code pool. An LLM-based Output Arbiter
adjudicates when candidates disagree and no ground truth exists.

The core diagnosis:

> "the bottleneck is not the Solver's capacity to generate correct solutions, but the **environment's
> capacity to discriminate them** at inference time."

## Why it matters to Synapse
Primarily for the vocabulary. **"Pseudo-correctness"** — output that overfits the visible checks
while failing the underlying logic — is the exact term for what a Synapse artifact does when it
renders beautifully and teaches the wrong physics. Borrowing an established term from the code-
generation literature and applying it to generated instruction is a small but genuine framing
contribution, and it costs one sentence.

The diagnosis quoted above also reframes the whole problem usefully. The argument is not "LLMs
cannot generate good science simulations" — evidently they can. It is that **without a discriminating
environment you cannot tell which generations are the good ones**. That is a much stronger and more
defensible motivation for the Verifier than any claim about model capability, and it survives model
improvements: better generators do not remove the need for discrimination.

Also useful: their Attacker *co-evolves* with the Solver, so the verification environment gets
harder as generation improves. That maps to a real future-work direction for Synapse's Verifier.

## The gap it leaves
Competitive-programming and benchmark settings with divergence-based signals — it works by finding
inputs on which candidate programs disagree, which presumes multiple candidates and a well-defined
input/output contract. A single generated science artifact has neither. Transferring the adversarial
principle to a domain with no test oracle is the open problem.

## How to cite it
Related Work (verification paragraph) and wherever "pseudo-correctness" is introduced. Prefer PROBE
as the primary adversarial-verification citation given the venue difference; use AdverMCTS for the
terminology and the discrimination framing.
