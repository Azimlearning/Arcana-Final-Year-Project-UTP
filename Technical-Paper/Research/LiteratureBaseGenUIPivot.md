# MCAIT 2026 — Literature Base for the GenUI Pivot

> Reference set for the repositioned paper: **Synapse / EduNova** (verified generative learning
> artifacts) rather than Arcana's GraphRAG platform.
> Compiled **18 August 2026** via live search. Companion docs: `MCAIT2026CompetitionContext.md`,
> `PreparationPlan.md`, `IEEEPaperOutlineandReferenceGuide.md`, `SubmissionChecklist.md`.
> FYP source of record: `C:\Users\User\Documents\FYP DOCS` (existing 20-source review lives in
> `Interim-report/Literature-review/`).

---

## 0. Read this first — two papers changed the shape of the paper

The search turned up two works that matter more than the other thirteen combined.

**MAIC-UI (arXiv:2604.25806)** is the closest prior art that exists. A zero-code system where
educators generate interactive STEM courseware from documents, built on a **"two-stage
generate-verify-optimize pipeline"**, with a three-month classroom deployment (53 high school
students, +9.21 points vs −2.32 control). It explicitly cites the Google Generative UI paper.
This is uncomfortably close to Synapse and **must be cited and differentiated in Related Work** —
a reviewer who knows this paper and doesn't see it cited will reject.

The differentiation is real and defensible:

| | MAIC-UI | Synapse |
|---|---|---|
| Who triggers generation | Teacher, at authoring time | Learner, at request time |
| Input | Textbook / PPT / PDF | A natural-language science question |
| Verification | Quality/layout optimisation stage | Adversarial verifier with revision retries |
| Safety property | Human review before delivery | **Structural** gate — delivery requires a type only the verifier can mint |

**"The Missing Layer" (arXiv:2606.15902, Neshaei et al.)** is the gift. It argues *against*
runtime GenUI in education, on the grounds that runtime generation "might lead to inaccurate
learning content due to the **inability to conduct verification at scale**," and that at runtime
"errors may be exposed directly to learners."

That is a named, published, 2026 objection to exactly what Synapse does — and Synapse's
adversarial verifier plus structural delivery gate is precisely the mechanism that answers it.
**This is the paper's thesis.** Position against it directly:

> Prior work argues that runtime generative UI is pedagogically unsafe because generated content
> cannot be verified at scale before reaching learners [Missing Layer]. We show this is an
> architectural limitation rather than a fundamental one: by making verification a structural
> precondition of delivery rather than a review step, request-time generation can retain the
> safety property that authoring-time review provides.

That framing gives you a contribution claim that is specific, falsifiable, and not "we built a
system."

---

## 1. The fifteen

Ordered by how load-bearing each is, not by topic. ⭐ = must cite.

### Group A — Generative UI (the core technical claim)

**[1] ⭐ Leviathan, Valevski, Kalman, Lumen, Segalis, Molad, Pasternak, Natchu, Nygaard,
Venkatachary, Manyika & Matias — "Generative UI: LLMs are Effective UI Generators"**
arXiv:2604.09577, Feb 2026 (Google). Project page: generativeui.github.io
The anchor citation for the whole premise. Demonstrates robust LLM generation of custom UIs;
human raters overwhelmingly prefer generated UIs over markdown output; comparable to expert-crafted
in ~50% of cases. Releases **PAGEN**, an expert-crafted evaluation dataset.
*Use it for:* establishing that generative UI is now a real capability, not speculation. Also
consider PAGEN as an evaluation precedent — a human-preference comparison against a text baseline
is a design you could mirror cheaply.

**[2] Liu, Sra & Xiao — "AlignUI: A Method for Designing LLM-Generated UIs Aligned with User
Preferences"** — arXiv:2601.17614, Jan 2026.
Crowdsourced preference dataset (50 users, 720 UI control preferences, 8 tasks); multi-stage
reasoning to align generated UI with task and preference; evaluated on 6 unseen tasks with 72 users.
*Use it for:* the alignment/personalisation dimension, and as an evaluation-design precedent.

**[3] "CrowdGenUI: Aligning LLM-Based UI Generation with Crowdsourced User Preferences"**
arXiv:2411.03477. *Use it for:* the preceding step in the GenUI alignment line; cite alongside [2].

**[4] Google A2UI Team — declarative agent-to-UI protocol** (Dec 2025).
Already in the FYP review (`Interim-report/Literature-review/GoogleA2UI2025.md`). Carry it over —
but note it now plays a *contrast* role: A2UI streams into a **trusted fixed component registry**,
which is Arcana's model. Synapse deliberately rejects the fixed catalogue. That contrast is worth
one sentence in Related Work; it is the cleanest way to explain what "Tier 3" means.

### Group B — Generative UI in education (closest prior art)

**[5] ⭐⭐ "MAIC-UI: Making Interactive Courseware with Generative UI"** — arXiv:2604.25806.
See §0. Lab study n=40; 3-month deployment n=53; generate-verify-optimize pipeline; sub-10s
incremental editing via unified diffs. Code at github.com/THU-MAIC/MAIC-UI.
*Use it for:* the mandatory differentiation. Also a realistic template for what an educational
evaluation of this kind of system looks like.

**[6] ⭐⭐ Neshaei, Shibu & Güreş — "The Missing Layer: Why EdTech Needs Design-Time Generative UI,
Not Just Runtime Personalization"** — arXiv:2606.15902, Jun 2026.
See §0. The objection your architecture answers.

**[7] Calò et al. — "Towards Educator-Driven Tutor Authoring: Generative AI Approaches for Creating
Intelligent Tutor Interfaces"** — Learning Analytics & Knowledge / AI-Builder workshop, 2024.
LLM generation of tutor layouts and components, whole-interface vs component-level generation.
*Use it for:* the earlier, pre-2026 root of GenUI-for-education; shows the trajectory.

**[8] "LearnMate²: Design and Evaluation of an LLM-powered Personalized and Adaptive Support System
for Online Learning"** — ACM DIS 2026; arXiv:2605.06257. Preliminary study n=24, evaluation n=16
against a SOTA platform + LLM baseline.
*Use it for:* a published-venue example of evaluating an LLM learning system against a
combined-baseline. Good model for your own evaluation section given small n.

### Group C — LLM-generated simulations for science learning

**[9] "AI-Generated Simulations of Physical Phenomena / Prompt-Based Simulations"** —
arXiv:2412.07482, Dec 2024.
Prompt templates that produce interactive HTML/JS physics simulations (pendulum, Ising model,
random walker); documents the iterative human debugging loop needed to make them correct.
*Use it for:* **the strongest motivation for your verifier.** This paper shows that generating a
physics simulation by prompt requires a human in the loop to catch errors (their worked example is
literally correcting an analytical solution with the wrong period). Synapse automates that loop.
Cite it as the problem, not the solution.

**[10] Shofa et al. — "From prompt to physics: evaluating Doppler effect simulation generated by
ChatGPT"** — *Physics Education* 61(1), 015029, 2026. DOI: 10.1088/1361-6552/ae272c
Expert + self evaluation of a ChatGPT-generated physics simulation via Likert scale; accurate on
physics concepts, limited on interface flexibility.
*Use it for:* an existing evaluation instrument for "is a generated simulation pedagogically
sound?" — directly reusable as a rubric design for your eval.

**[11] Tran, Huynh, Poor, Tran & Nguyen — "ChemersiveLLM: Prompt-to-VR Simulation of Chemistry
Experiments Using Generative AI"** — ACM VRST '25, DOI: 10.1145/3756884.3770535.
LLM generates a structured JSON experiment spec rendered in Unity VR; within-subjects n=20;
ANOVA p<0.001 over traditional and chatbot baselines. Notes hallucination control as the open
limitation: *"expert review remains essential."*
*Use it for:* a three-condition evaluation design (traditional / chatbot / generated-interactive)
you could replicate, and another explicit statement that verification is the unsolved problem.

### Group D — Verification of generated code (your technical contribution)

**[12] ⭐ Li, Liu, Zhang, Gao & Sun — "Beyond Superficial Tests: Adversarial Refinement for Reliable
Property-Based Testing"** — Findings of ACL 2026, pp. 13957–13974. DOI: 10.18653/v1/2026.findings-acl.683
PROBE: a Validator agent generates *counter-implementations* — semantically wrong code that still
satisfies the property — to expose specification loopholes. +9.79% mutation score; 45 confirmed
real-world bugs.
*Use it for:* the peer-reviewed anchor for "adversarial verification." Prefer this over arXiv-only
items in Group D — it is a published ACL venue and carries more weight with reviewers.

**[13] "Code Monitor Red Teaming for Public-Test-Passing Code"** — arXiv:2607.20852.
71,000 candidates; 43,677 pass public tests; **23,081 of those still fail hidden tests.** Weak
verifiers miss most residual bugs at 5% FPR. Conclusion: *"public-test passing is not a stopping
rule."*
*Use it for:* the hardest empirical justification for adversarial verification over simple checks.
The 23,081/43,677 figure is a citable number that motivates your whole delivery gate.

**[14] "AdverMCTS: Combating Pseudo-Correctness in Code Generation via Adversarial Monte Carlo Tree
Search"** — arXiv:2604.10449.
Minimax game between a Solver that writes code and an Attacker that evolves corner-case tests;
names the failure mode **"pseudo-correctness"** — passing visible checks while failing the real
logic.
*Use it for:* the vocabulary. "Pseudo-correctness" is exactly the failure mode a science artifact
exhibits when it renders beautifully and teaches the wrong physics. Borrow the term.

**[15] Kwok, Li, Atreya, Liu, Jiang, Finn et al. — "LLM-as-a-Verifier: A General-Purpose
Verification Framework"** — arXiv:2607.05391.
Verification as a scaling axis; continuous scores over logit distributions rather than discrete
judgments; scaling via granularity, repeated evaluation, and criteria decomposition.
*Use it for:* framing your verifier's design choices (criteria decomposition especially) as
instances of a general principle rather than ad-hoc prompt engineering.

---

## 2. Supplementary — pedagogical grounding (pick 3–4)

A reviewer in Track 2 will ask *why interactive artifacts help learning at all.* You cannot assert
it. These are the citations that settle it cheaply:

| Work | Venue | Use for |
|---|---|---|
| **Mayer — "The Past, Present, and Future of the Cognitive Theory of Multimedia Learning"** | *Educational Psychology Review*, 2024. DOI: 10.1007/s10648-023-09842-1 | The single best modern CTML citation. Dual channels, limited capacity, active processing; **generative processing** is the construct that justifies "interactive beats text" |
| **Ningrum et al. — PhET effectiveness in science and chemistry education: a systematic review** | *Multimodal Technol. Interact.* 10(7), 69, 2026. DOI: 10.3390/mti10070069 | PRISMA review, 14 studies. **Use this, not Banda & Nzabahimana** — same claim, inside the 4-year window, open access, Indonesian authorship (regional signal) |
| **Meta-analysis of PhET effectiveness in physics education** | *iJOE*, Feb 2026 — 47 effect sizes, 20 studies, 4,563 students, **d = 0.83** | One number that justifies the entire artifact premise. Very quotable in the Introduction |
| ~~Banda & Nzabahimana — PhET review~~ | ~~*Phys. Rev. Phys. Educ. Res.* 17, 023108, 2021~~ | ❌ **2021 — outside the 4-year window.** Superseded by Ningrum. Retained as background only; see `Literature-notes/_RecencyAudit.md` |
| **Fiorella & Mayer — generative activity principle** | *Cambridge Handbook of Multimedia Learning* | Only if you frame artifacts as generative-learning activities — check the edition year against the recency rule first |

> ⚠️ **Recency constraint (supervisor guidance):** sources should be no older than ~4 years, i.e.
> **2022 onward** as of Aug 2026. Full audit in `Literature-notes/_RecencyAudit.md`. Note that the
> FYP's own review spans 2016–2025, so confirm with Prof. Ahmad Sobri whether foundational
> exceptions are permitted before cutting theory anchors.

> **Framing note.** PhET is the strongest rhetorical move available to you. PhET simulations are
> hand-built by a funded team over years, cover a fixed catalogue, and demonstrably work (d = 0.83).
> Synapse generates a PhET-like artifact for an arbitrary question in seconds. The Introduction
> writes itself: *the evidence for interactive simulations is settled; the bottleneck is that
> someone must build each one.*

---

## 3. Supplementary — risk and safety in educational AI (pick 1–2)

These justify why an *unverified* generated artifact is worse than no artifact — the premise of
your hard rule.

- **EduEVAL-DB** (arXiv:2602.15531) — pedagogical risk rubric over five dimensions (factual
  correctness, depth, focus/relevance, level-appropriateness, ideological bias); 854 explanations.
  Names the key risk: **"concept corruption, where misconceptions are implanted in the learner,"**
  amplified by the illusion-of-truth effect and the difficulty of unlearning.
- **AIriskEval-edu** (arXiv:2607.01934) — the extended version, 1,639 explanations, adds risk
  localisation annotations.
- **"Multi-Agent Intelligent Tutoring with 4D Personalization and Hallucination Detection"**
  (Intelligent Tutoring Systems 2026) — 17 agents, hybrid hallucination detection (semantic entropy
  + token uncertainty), n=47, +28.9% learning gain (d=1.29). A direct competitor framing for
  "multi-agent + verification in education."
- **Shoufan & Esmaeil — "AI Hallucination from Students' Perspective"** (arXiv:2602.17671, Jan 2026)
  — students detect hallucinations most reliably in code *because it can be executed and checked*;
  identifies a **"verifiability gap"** for conceptual content. Useful sentence for your motivation.

---

## 4. Strategic regional citations (cite 1–2, only if genuinely relevant)

Prof. **Shahrul Azman Mohd Noah** (UKM CAIT, MCAIT keynote and organiser) heads the Knowledge
Technology group — semantic technology, IR, recommender systems, and now LLMs. His recent work is
adjacent enough to cite honestly *if* you retain any graph/retrieval component from Arcana:

- Tiwary, Noah, Fauzi & Tan — "Max Explainability Score: A quantitative metric for explainability
  evaluation in knowledge graph-based recommendations," *Computers and Electrical Engineering*, 2024.
- Saat, Mohd, Noah & Al-ghuribi — "Beyond Relevance: Enhancing Serendipity in Content-Based
  Recommendations With Knowledge Graphs," *IEEE Access*, 2025, pp. 142980–142989.
- Tiwary, Noah & Fauzi — "Prioritising explainable AI-driven recommendations with knowledge graphs
  and reinforcement learning," *J. King Saud Univ. Comput. Inf. Sci.*, 2025.

> **Honesty gate:** only cite these if the paper actually retains a knowledge-graph or
> explainability component. If the GenUI pivot drops Arcana's graph layer entirely, these become
> padding, and padding against IEEE's own guidance ("cite only what supports the work"). In that
> case, cite nothing from this group and accept it.

---

## 5. MCAIT winning / best papers — the honest answer

**There is no publicly retrievable corpus of MCAIT best papers, and no evidence a best-paper award
exists.** I checked and could not find one. What I did establish:

| Finding | Source |
|---|---|
| MCAIT 2024 and M-CAIT 2021 published accepted papers as **e-proceedings with ISBN**, issued by CAIT, FTSM, UKM — *not* IEEE, *not* Xplore, *not* Scopus | ftsm.ukm.my/mcait2024/cfp.html |
| Selected papers were invited to extend into the **Asia-Pacific Journal of Information Technology and Multimedia (APJITM)** | same |
| Earlier editions accepted **Bahasa Melayu or English**, single-column, with inconsistent page guidance (the 2024 CfP contradicts itself: "2–4 pages" then "more than 6 pages, maximum 15") | same |
| The 2024 CfP's publication line is literally a **blank underline** — the venue was undecided at CfP time | same |
| No best-paper award, prize list, or awards page is published for 2021 or 2024 | searched |

**What this means, and it is important:**

1. **2026 is a genuine discontinuity.** MCAIT 2026 is the first edition under an IEEE Conference
   Record (#71376) with Xplore + Scopus indexing, two-column IEEE template, EDAS, 4–6 pages, and
   a <20% similarity gate. Prior editions were a regional e-proceedings conference. **Do not
   calibrate quality, length, or formatting against past MCAIT papers.** They are not a guide, and
   the existing `MCAIT2026CompetitionContext.md` §1 warning about this is confirmed correct.
2. **There is no "what wins at MCAIT" signal to mine.** Anyone claiming otherwise is guessing.
   Calibrate against **IEEE conference norms generally**, not this venue's history.
3. **The real signal is the reviewer pool, not past winners.** Reviewers are drawn from UKM CAIT
   and the Saudi IEEE sections. Their published work skews toward semantic technology, IR,
   recommender systems, ontologies, NLP, and applied AI — heavily *systems-and-evaluation* papers,
   not theory. That favours you: a working system with an honest evaluation is the shape this
   community rewards.

**Two things worth doing about this:**

- Add to the secretariat email (`MCAIT2026CompetitionContext.md` §10 already drafts one): *"Is
  there a best paper award and/or a student paper category?"* — it was already question 4 on that
  list. Still unanswered; still worth asking.
- If you want a real quality bar to calibrate against, use **APJITM** back issues (the journal
  MCAIT extends selected papers into) rather than hunting the e-proceedings. It is publicly
  browsable and tells you what this community's editors consider publishable.

---

## 6. Verification status — read before citing anything

Per the standing rule in `IEEEPaperOutlineandReferenceGuide.md` §4: **open every paper before you
cite it.** Current status of this list:

| Confidence | Items |
|---|---|
| **High — venue and identifiers confirmed** | [1] arXiv abs page + project site; [2] arXiv abs page; [12] ACL Anthology entry with DOI, volume, page numbers; [10] IOPscience DOI; [11] ACM DOI; Mayer 2024 Springer DOI; Banda & Nzabahimana APS DOI |
| **Medium — abstract and content confirmed, full bibliographic details not** | [5], [6], [8], [13], [14], [15], EduEVAL-DB, AIriskEval-edu, iJOE meta-analysis |
| **Needs checking before use** | [3] CrowdGenUI (v2 HTML only — find the published venue, it may have appeared at a CHI-adjacent venue); [7] Calò et al. (workshop PDF from an author site — confirm the venue name and year); [9] arXiv:2412.07482 (no title/author metadata returned — **verify authors and title directly**); the ITS 2026 multi-agent tutoring paper (PDF hosted on a lab site — confirm the proceedings citation) |

Several Group D items are 2026 arXiv preprints with no citation count. Under the ≥40% 2024–2026
recency target this is fine, but **prefer a published version where one exists** — that is why [12]
should carry the adversarial-verification argument rather than [14].

---

## 7. What this does to the paper's shape

The reference base now supports a much stronger claim than the Arcana framing did. Suggested
positioning, three moves:

1. **Interactive simulations demonstrably improve science learning** (PhET, d = 0.83) **but each
   one must be hand-built** — a fixed catalogue cannot cover an arbitrary student question.
2. **Generative UI can now produce them on demand** [1], **including for education** [5] — **but
   the field's own position is that runtime generation is unsafe because it cannot be verified
   before it reaches a learner** [6], and unverified generated instruction risks implanting
   misconceptions [EduEVAL-DB], while passing surface checks is not correctness [13].
3. **We make verification structural rather than procedural** — the delivery path is typed so that
   an unverified artifact cannot reach the client — **and evaluate whether request-time generation
   can hold the safety property that authoring-time review provides.**

Every one of those three moves now has a citation behind it, and move 3 is a contribution claim
rather than a system description. That is the thing the old Arcana framing never had.

**Suggested title direction** (avoiding "novel"/"new" per IEEE guidance):

- *Verified Generative Interfaces for Science Learning: Request-Time Artifact Generation with a Structural Delivery Gate*
- *Adversarially Verified Generative UI for Interactive Science Education*

**Keyword set** (Xplore/Scopus discoverability, must include an education-signalling term):
`generative user interfaces` · `AI in education` · `large language models` · `code verification` ·
`interactive simulation`

---

*Compiled 18 August 2026. Search conducted live; conference facts re-verified against
ftsm.ukm.my/mcait2024 and mcait2026.org. Bibliographic details flagged in §6 must be confirmed at
source before submission.*
