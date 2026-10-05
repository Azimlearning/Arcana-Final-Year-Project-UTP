# Code Monitor Red Teaming for Public-Test-Passing Code

**Authors not confirmed** · 2026 · arXiv:2607.20852
**Domain:** Verification of generated code — empirical limits · **Verified:** 🟡 abstract and results
confirmed; authors and venue not established
**Priority:** ⭐ the hard number

## What it does
Studies a deployment-realistic monitoring problem: after LLM-generated code has already passed
visible tests, can a verifier still find the residual hidden bugs? Introduces CodeMonitorBench
across function-level, data-science and workflow code.

The headline numbers, from 71,000 generated candidates:

- **43,677 passed public tests**
- **23,081 of those still failed hidden tests** — roughly **53% of everything that passed visible
  checks was still wrong**
- Weak verifiers miss most hidden bugs even at a 10% false-positive budget
- Adversarial pressure (generators told to pass public tests while leaving a subtle bug) degrades
  verifier AUROC further
- A stronger verifier recovers only part of the gap

Their conclusion: **"public-test passing is not a stopping rule."**

## Why it matters to Synapse
This supplies the one thing a motivation section most needs and most often lacks: a **hard,
quotable number** showing that the obvious cheap solution is insufficient.

The obvious reviewer question about Synapse is "why not just run the generated code and see if it
works?" This paper answers it empirically at scale. Over half of all code that passed its visible
checks was still broken. Execution success is not correctness — which is precisely why the Verifier
cannot be replaced by a smoke test, and why the delivery gate has to be structural rather than "we
ran it and it didn't crash."

The 23,081/43,677 figure belongs in the Introduction. It is more persuasive than any amount of
argument about hallucination in the abstract.

## The gap it leaves
Software engineering domains — functions, data science, workflows — with hidden test suites
available as ground truth. Educational artifacts have no hidden test suite. There is no oracle for
"does this simulation teach the right physics," which makes Synapse's verification problem harder
than the one measured here, not easier. Worth acknowledging honestly rather than borrowing their
numbers as if they transfer directly.

## How to cite it
Introduction (the number) and Method (why execution-based checking alone is insufficient).
**Confirm authors and any published venue before submission** — an unattributed arXiv preprint
carrying a load-bearing statistic is a weak point a reviewer may probe.
