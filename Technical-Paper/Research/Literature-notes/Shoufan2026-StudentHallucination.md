# AI Hallucination from Students' Perspective: A Thematic Analysis

**Abdulhadi Shoufan & Ahmad Azmi Abdelhamid Esmaeil** · 2026 · arXiv:2602.17671 (11 Jan 2026)
**Domain:** Risk in AI-generated educational content — learner side · **Verified:** 🟡 abstract,
authors and findings confirmed
**Priority:** supporting — one very good idea

## What it does
Thematic analysis of how students actually encounter and respond to LLM hallucinations. Context:
adoption is near-universal (~86–90% of students across multiple surveys), while most hallucination
research addresses detection and mitigation rather than user experience.

The central finding is a **verifiability gap**:

> Students most often detected hallucinations in coding and technical topics because the output is
> verifiable: code can be executed and checked against expected outcomes. Yet students frequently use
> AI for tasks where verification is not feasible, such as conceptual understanding.

Also finds that over half of students relied on intuition rather than systematic checking, that many
technically-trained students still hold a mistaken mental model of LLMs as retrieval systems, and
that model sycophancy risks reinforcing misconceptions rather than correcting them.

## Why it matters to Synapse
The verifiability gap is a genuinely elegant argument for the system, and it is not obvious until
stated.

Students can catch AI errors when output is executable and checkable. They cannot when it is
conceptual. **Synapse's artifacts sit exactly at that intersection** — they are conceptual content
(science explanation) delivered through an executable medium (running HTML/JS). Left unverified,
that is the worst combination: a running simulation carries the authority of executable output while
being conceptually wrong, and the student's usual defence — "I'd notice if it broke" — does not
apply, because it does not break.

The Verifier closes the gap the student cannot close themselves. That is a sharper motivation than
generic hallucination concern, and it is learner-centred, which suits Track 2.

The sycophancy finding supports a Limitations sentence: a system that generates whatever the student
asks for risks confirming a mistaken premise embedded in the question. Worth naming honestly.

## The gap it leaves
Perceptions and self-reported behaviour, not measured outcomes — it establishes that students
struggle to verify conceptual content, not what that costs them in learning terms. Also a preprint
with no venue.

## How to cite it
Introduction, one sentence on the verifiability gap — the framing is worth more than the study
itself. Optionally Limitations, for sycophancy. Cut before cutting EduEVAL-DB if space is tight.
