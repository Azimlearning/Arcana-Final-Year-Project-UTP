# Literature Notes — Index

> 20 notes supporting the MCAIT 2026 GenUI-pivot paper (Synapse / EduNova).
> One note per source: what it does · why it matters to Synapse · the gap it leaves · how to cite it.
> Synthesis and the Chapter-2-style table: `../LiteratureReviewTable.md`
> Strategy and the MCAIT-specific findings: `../LiteratureBaseGenUIPivot.md`
> Recency compliance: `_RecencyAudit.md`

## Verification legend
✅ full bibliographic record confirmed at source · 🟡 abstract and content confirmed, some fields
missing · ⚠️ needs checking before citing

---

## 2.1 Generative UI — foundations

| Note | Year | Venue | Verified |
|---|---|---|---|
| [[Leviathan2026-GenerativeUI]] ⭐ | 2026 | arXiv:2604.09577 (Google) | ✅ |
| [[Liu2026-AlignUI]] | 2026 | arXiv:2601.17614 | ✅ |
| [[CrowdGenUI2024]] | 2024 | arXiv:2411.03477 | ⚠️ venue |

## 2.2 Generative UI in education

| Note | Year | Venue | Verified |
|---|---|---|---|
| [[MAICUI2026]] ⭐⭐ | 2026 | arXiv:2604.25806 | 🟡 authors |
| [[Neshaei2026-MissingLayer]] ⭐⭐ | 2026 | arXiv:2606.15902 | 🟡 |
| [[Calo2024-TutorAuthoring]] | 2024 | workshop | ⚠️ venue, authors |
| [[LearnMate2-2026]] | 2026 | **ACM DIS 2026** | 🟡 authors |

## 2.3 LLM-generated science simulations

| Note | Year | Venue | Verified |
|---|---|---|---|
| [[PromptBasedSimulations2024]] ⭐ | 2024 | arXiv:2412.07482 | ⚠️ **title + authors** |
| [[Shofa2026-DopplerSimulation]] ⭐ | 2026 | *Physics Education* 61(1) | ✅ |
| [[Tran2025-ChemersiveLLM]] | 2025 | **ACM VRST '25** | ✅ |

## 2.4 Verification of generated code

| Note | Year | Venue | Verified |
|---|---|---|---|
| [[Li2026-PROBE]] ⭐ | 2026 | **Findings of ACL 2026** | ✅ |
| [[CodeMonitorRedTeaming2026]] ⭐ | 2026 | arXiv:2607.20852 | 🟡 authors |
| [[AdverMCTS2026]] | 2026 | arXiv:2604.10449 | 🟡 authors |
| [[Kwok2026-LLMasVerifier]] | 2026 | arXiv:2607.05391 | 🟡 |

## 2.5 Interactive simulations and learning theory

| Note | Year | Venue | Verified |
|---|---|---|---|
| [[Mayer2024-CTML]] ⭐ | 2024 | *Educational Psychology Review* | ✅ |
| [[Ningrum2026-PhETSystematicReview]] ⭐ | 2026 | *Multimodal Technol. Interact.* 10(7) | ✅ |
| [[PhETMetaAnalysis2026]] ⭐ | 2026 | *iJOE* | 🟡 authors |
| [[BandaNzabahimana2021-PhET]] ❌ | 2021 | *Phys. Rev. Phys. Educ. Res.* 17 | ✅ but **out of window** |

## 2.6 Risk in AI-generated educational content

| Note | Year | Venue | Verified |
|---|---|---|---|
| [[EduEVALDB2026]] ⭐ | 2026 | arXiv:2602.15531 | 🟡 authors |
| [[Shoufan2026-StudentHallucination]] | 2026 | arXiv:2602.17671 | 🟡 |

---

## The four that matter most

If time collapses and only four sources can be read properly:

1. **[[Neshaei2026-MissingLayer]]** — states the objection the paper exists to answer. The thesis
   comes from here.
2. **[[MAICUI2026]]** — closest prior art. Must be cited and differentiated or the paper is rejected.
3. **[[Leviathan2026-GenerativeUI]]** — makes the premise legitimate; supplies an evaluation design.
4. **[[Li2026-PROBE]]** — the peer-reviewed anchor for adversarial verification.

## Carried over from the FYP review

`FYP DOCS/Interim-report/Literature-review/GoogleA2UI2025.md` still applies, but its role **inverts**
under the pivot. A2UI streams typed intent into a *trusted fixed component registry* — that is
Arcana's model, and Synapse deliberately rejects it. Cite it as the contrast that defines what
"no predefined component library" means.

The other 19 FYP sources (GraphRAG, multi-agent, re-ranking, spaced repetition) are **out of scope**
for this paper unless the graph layer is retained. Do not carry them over by default.

## Outstanding

- ~10 notes need author lists or venue confirmation before citing — see the Verified column
- `PromptBasedSimulations2024` needs title and authors verified directly on arXiv; it carries a
  load-bearing example
- Decide with the supervisor whether foundational exceptions to the 4-year rule are permitted
  (`_RecencyAudit.md`)
