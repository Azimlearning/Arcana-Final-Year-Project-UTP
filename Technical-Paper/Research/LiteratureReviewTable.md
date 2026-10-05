# Literature Review — Source Table and Research Gaps

> **19 papers · 6 domains · 2024–2026** (all within the 4-year window — see
> `Literature-notes/_RecencyAudit.md`)
> For the MCAIT 2026 paper on **Synapse / EduNova**: verified generative learning artifacts.
> Format follows `FYP DOCS/Interim-report/Docs/02-content.md` §2 — one subsection per domain,
> synthesise the papers **inside each subsection in prose**; do not write one paragraph per paper.
> Full per-paper notes: `Literature-notes/`

Sources: ACL, ACM (DIS, VRST), IOP Publishing, Springer, MDPI, iJOE, arXiv.

---

## 2.1 Generative UI — Foundations

1. **Leviathan et al., 2026** (arXiv:2604.09577, Google) — demonstrates that a properly prompted,
   tool-equipped LLM robustly generates high-quality custom interfaces for effectively any prompt;
   generated UIs are overwhelmingly preferred by humans over markdown output and comparable to
   expert-crafted work in ~50% of cases. Releases the PAGEN evaluation dataset. The foundational
   citation establishing that generative UI is a demonstrated capability, not an aspiration.
   *Gap: optimises for preference and quality; says nothing about whether generated content is factually correct.*

2. **Liu, Sra & Xiao, 2026** (arXiv:2601.17614) — AlignUI: aligns generated UIs to user tasks and
   preferences via a crowdsourced preference dataset (50 users, 720 control preferences), evaluated
   on six unseen tasks with 72 raters. Shows the field has moved past feasibility into alignment.
   *Gap: aligns to preference, not correctness; evaluated in image editing, a domain with no ground truth to violate.*

3. **CrowdGenUI, 2024** (arXiv:2411.03477) — crowdsourced preference corpus for LLM-based UI
   generation; the direct predecessor to AlignUI. Included to show the trajectory of the alignment
   line rather than a single point.
   *Gap: same preference-not-correctness limitation, and predates the 2026 capability jump.*

## 2.2 Generative UI in Education

4. **MAIC-UI, 2026** (arXiv:2604.25806) — zero-code system letting educators generate interactive
   STEM courseware from textbooks, PPTs and PDFs through a two-stage generate-verify-optimize
   pipeline; lab study n=40, three-month classroom deployment n=53 (+9.21 points vs −2.32 control).
   **The closest prior art in existence and mandatory to differentiate against.**
   *Gap: authoring-time and teacher-facing — the human reviews before any learner sees output, so coverage is bounded by what the teacher anticipated.*

5. **Neshaei, Shibu & Güreş, 2026** (arXiv:2606.15902) — position paper arguing runtime generative UI
   in EdTech is unsafe because of the "inability to conduct verification at scale," leaving errors
   "exposed directly to learners"; proposes a card-based authoring-time paradigm instead.
   **States the objection this paper exists to answer.**
   *Gap: treats verification-at-scale as impossible rather than as an open engineering problem; proposes no mechanism, presents no system or evaluation.*

6. **Calò et al., 2024** (workshop) — extends the Apprentice Tutor Builder with GPT-4 generation of
   tutor layouts and components so non-technical educators can author interfaces. Establishes that
   education-GenUI predates the 2026 wave and was framed as educator assistance from the start.
   *Gap: no evaluation of generated interface quality or pedagogical effect; no correctness verification at all.*

7. **LearnMate², 2026** (ACM DIS 2026, arXiv:2605.06257) — three coordinated LLM components
   (planning, real-time assistance, adaptive adjustment) forming a closed learning loop; evaluated
   n=24 then n=16 against a combined platform-plus-LLM baseline. Methodologically important: a
   peer-reviewed ACM venue publishing small-n system evaluation against a realistic baseline.
   *Gap: adapts around fixed course material; never generates the instructional artifact, so generated-content correctness never arises.*

## 2.3 LLM-Generated Science Simulations

8. **Prompt-Based Simulations, 2024** (arXiv:2412.07482) — prompt templates producing interactive
   HTML/JS physics simulations (pendulum, Ising model, random walker) with no programming skill
   required; documents the iterative human debugging loop needed for correctness, including
   correcting a generated pendulum whose analytical solution displayed exactly half the correct
   period. **The single clearest statement of the problem Synapse solves.**
   *Gap: no automated verification whatsoever — correctness depends entirely on an expert noticing a silent conceptual error.*

9. **Shofa et al., 2026** (*Physics Education* 61(1), 015029) — develops and evaluates a
   ChatGPT-generated Doppler effect simulation via self- and expert evaluation on a Likert scale,
   scoring conceptual accuracy, visualisation and interface separately; maximum scores on physics
   accuracy, limitations in interface flexibility. Supplies a published, reusable rubric.
   *Gap: n=1 simulation after human-guided iterative prompting; measures whether a shepherded generation can be good, not whether generation is reliably good unsupervised.*

10. **Tran et al., 2025** (ACM VRST '25, DOI 10.1145/3756884.3770535) — ChemersiveLLM: LLM generates
    a constrained-JSON chemistry experiment specification rendered as an interactive VR lab;
    within-subjects n=20 across traditional, chatbot and immersive conditions, ANOVA p<0.001
    favouring the generated interactive condition. Supplies the three-condition evaluation design.
    *Gap: achieves safety by restricting output to a rigid schema, capping expressiveness; authors state "expert review remains essential" for hallucination control.*

## 2.4 Verification of Generated Code

11. **Li et al., 2026** (Findings of ACL 2026, pp. 13957–13974) — PROBE: names the "superficiality
    gap" and hardens software properties through adversarial refinement, using a Validator agent to
    generate counter-implementations that satisfy the property while being semantically wrong;
    +9.79% mutation score, 45 confirmed real-world bugs. **The peer-reviewed anchor for adversarial
    verification.**
    *Gap: verifies software correctness against specifications and invariants, not pedagogical correctness — there is no unit test for "this misrepresents the Doppler effect."*

12. **Code Monitor Red Teaming, 2026** (arXiv:2607.20852) — of 71,000 generated candidates, 43,677
    passed public tests and **23,081 of those still failed hidden tests**; weak verifiers miss most
    residual bugs even at a 10% false-positive budget. Concludes "public-test passing is not a
    stopping rule." The empirical answer to "why not just run it and see if it works?"
    *Gap: measured in software domains with hidden test suites as ground truth; educational artifacts have no oracle, making the problem harder rather than easier.*

13. **AdverMCTS, 2026** (arXiv:2604.10449) — frames robust code generation as a minimax game between
    a Solver and an Attacker evolving corner-case tests; names the failure mode
    **"pseudo-correctness"** and argues the bottleneck is "the environment's capacity to discriminate"
    good generations, not the generator's capacity to produce them.
    *Gap: relies on output divergence across multiple candidates and a defined input/output contract; a single generated science artifact has neither.*

14. **Kwok et al., 2026** (arXiv:2607.05391) — LLM-as-a-Verifier: argues verification is a scaling
    axis, with gains from score granularity, repeated evaluation and **criteria decomposition**;
    state of the art on four agentic benchmarks. Provides the design rationale for structuring a
    verifier's criteria rather than asking one global quality question.
    *Gap: general-purpose agentic tasks with benchmarkable outcomes; nothing on educational content or artifacts destined for a learner.*

## 2.5 Interactive Simulations and Learning Theory

15. **Mayer, 2024** (*Educational Psychology Review*, DOI 10.1007/s10648-023-09842-1) — four-decade
    retrospective on the Cognitive Theory of Multimedia Learning: dual channels, limited capacity,
    active processing, and 15 evidence-based design principles organised around reducing extraneous,
    managing essential, and fostering **generative** processing. Supplies the mechanism explaining
    *why* an interactive artifact should outperform text.
    *Gap: assumes carefully designed multimedia authored by humans applying the principles; silent on generated material where design quality varies per artifact and nothing verifies the principles were respected.*

16. **Ningrum et al., 2026** (*Multimodal Technologies and Interaction* 10(7), 69,
    DOI 10.3390/mti10070069) — PRISMA 2020 systematic review of 14 empirical studies (2020–2026) on
    PhET simulations; consistent improvement in academic achievement and conceptual understanding,
    attributed to visualising phenomena that cannot be observed directly; effectiveness depends on
    instructional design, teacher facilitation and accessibility.
    *Gap: reviews the human-authored PhET catalogue only; higher-order and affective outcomes under-investigated; says nothing about generated simulations.*

17. **PhET meta-analysis, 2026** (*iJOE*) — 47 effect sizes from 20 studies, 4,563 students;
    overall **d = 0.83** for PhET versus traditional instruction, strongest at secondary level and in
    abstract domains such as electricity and waves. The quantitative warrant for the entire premise.
    *Gap: aggregates human-authored simulations; the effect size cannot be assumed to transfer to generated artifacts.*

## 2.6 Risk in AI-Generated Educational Content

18. **EduEVAL-DB, 2026** (arXiv:2602.15531) — 854 explanations across 139 ScienceQA questions with a
    five-dimension pedagogical risk rubric (factual correctness, depth, focus/relevance, level
    appropriateness, ideological bias), including a "Confidently Inaccurate Teacher" role. Frames
    factual error in education as **concept corruption — misconceptions implanted in the learner**,
    amplified by the illusion-of-truth effect and the difficulty of unlearning.
    *Gap: evaluates static text explanations; nothing on interactive or executable artifacts, where the risk surface is larger and the failure more convincing.*

19. **Shoufan & Esmaeil, 2026** (arXiv:2602.17671) — thematic analysis of student encounters with
    hallucination; identifies a **verifiability gap**: students detect errors in code because it can
    be executed and checked, but not in conceptual content, which is where they most rely on AI.
    Over half relied on intuition rather than systematic checking.
    *Gap: self-reported perceptions rather than measured learning cost; establishes the gap exists without quantifying its consequences.*

---

## Research Gaps (G1–G7) — closing subsection of the review

- **G1:** Generative UI is evaluated for preference and quality, never for correctness of
  instructional content
- **G2:** Every GenUI-in-education system is authoring-time and teacher-facing; none generates for
  the learner at request time, so coverage is bounded by what an educator anticipated
- **G3:** Runtime generative UI is asserted to be unverifiable at scale, and no mechanism has been
  proposed that would make it safe
- **G4:** LLM-generated science simulations demonstrably require expert human review to catch silent
  conceptual errors; no automated verification exists for this class of content
- **G5:** Adversarial verification is developed for code correctness against test oracles, and has
  not been extended to pedagogical or conceptual correctness, where no oracle exists
- **G6:** Passing execution and visible checks is not correctness — over half of public-test-passing
  code still fails hidden tests — yet execution success remains the de facto gate in generated-content
  systems
- **G7:** The evidence base for interactive simulations (d = 0.83) derives entirely from
  human-authored catalogues; whether generated artifacts retain that benefit is unmeasured

**Framing line for the closing paragraph:**

> Synapse is not feature accumulation. Each architectural decision answers one of these seven
> documented gaps — and the central one, G3, is a claim the literature makes about what is
> impossible rather than a feature nobody has built yet.

**Mapping gaps to contributions** (use this to build the enumerated contributions list):

| Gap | Answered by |
|---|---|
| G1, G4, G5 | Adversarial Verifier with revision retries, applied to conceptual correctness |
| G2 | Request-time, learner-facing generation from a natural-language question |
| G3, G6 | Structural delivery gate — the delivery path requires a type only the Verifier can mint, so unverified output is unreachable rather than merely discouraged |
| G7 | Evaluation comparing generated artifacts against a text baseline (stated honestly as preliminary) |

---

## Competitive positioning table

For the Introduction as motivation, or as the closing subsection of the review. Same role as the
Arcana positioning table in `FYP DOCS/Interim-report/Docs/02-content.md` §Ch.2 (alt.).

| Capability | PhET | LLM chat (text) | MAIC-UI | ChemersiveLLM | **Synapse** |
|---|---|---|---|---|---|
| Interactive artifact | ✓ | ✗ | ✓ | ✓ | ✓ |
| Covers an arbitrary student question | ✗ | ✓ | ✗ | Partial | ✓ |
| Generated at request time | ✗ | ✓ | ✗ | ✓ | ✓ |
| No per-topic authoring effort | ✗ | ✓ | ✗ | Partial | ✓ |
| Automated correctness verification | n/a (hand-built) | ✗ | Partial | ✗ | ✓ |
| Unverified output structurally blocked | n/a | ✗ | ✗ | ✗ | ✓ |
| Unbounded output expressiveness | ✗ | ✓ | ✓ | ✗ (fixed schema) | ✓ |
| Runs on a commodity browser | ✓ | ✓ | ✓ | ✗ (VR headset) | ✓ |

> Read the table honestly. PhET wins on evidence — two decades of validated pedagogy that Synapse
> cannot claim. MAIC-UI wins on deployment evidence — a three-month classroom study. The column
> Synapse owns outright is the bottom-left quadrant: **verified generation of an artifact nobody
> authored in advance.** That is the contribution; everything else is context.

---

## Narrative arc for Chapter 2 / Related Work

Three moves, each now carrying citations:

1. **Interactive simulations demonstrably improve science learning** (Ningrum 2026; iJOE 2026,
   d = 0.83), and multimedia learning theory explains why (Mayer 2024) — **but each simulation must
   be hand-built**, so coverage is bounded by authoring effort.
2. **Generative UI can now produce them on demand** (Leviathan 2026), including for education
   (MAIC-UI 2026) — **but the field's own position is that runtime generation is unsafe because it
   cannot be verified before reaching a learner** (Neshaei 2026), unverified instruction risks
   implanting misconceptions (EduEVAL-DB 2026), students cannot verify conceptual content themselves
   (Shoufan 2026), and passing surface checks is not correctness (Code Monitor 2026).
3. **We make verification structural rather than procedural** — building on adversarial verification
   from code generation (PROBE 2026; AdverMCTS 2026) and criteria decomposition (Kwok 2026) — and
   evaluate whether request-time generation can hold the safety property that authoring-time review
   provides.

Move 3 is a contribution claim rather than a system description. That is what the Arcana framing
never had.

---

*Compiled 18 August 2026. Every entry must be opened and its bibliographic record confirmed before
citing — see the Verified column in `Literature-notes/_Index.md`; roughly half still need author
lists or venue confirmation.*
