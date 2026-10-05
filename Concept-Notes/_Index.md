---
tags: [moc]
---

# Concept Notes — Index

Atomic notes from the frozen FYP proposal/concept planning session (`concept/FYP_Context_Document.md`), plus four notes from the PRD's stable sections only (personas, goals, non-goals, success metrics).

**Deliberately excluded:** `Arcana/docs/arcana_prd.md`'s phase-tagged sections, `checklist.md`, `project_file_structure.md`, `deployment.md`, `env_generation_guide.md`. These are live engineering docs with their own drift-tracking (ADRs in `.claude/memory/DECISIONS.md`, the `docs-drift-auditor` subagent) — atomizing them here would just create a second copy that goes stale as the build progresses.

## Proposal & planning (static — won't change)
- [[StudentProfile]]
- [[VERA-AI-PriorWork]]
- [[ProjectConcept-ThreeInnovations]]
- [[ExtendsVERA-Comparison]]
- [[Objectives]]
- [[LLMCouncilAssessment]]
- [[FORM01A-Content]]
- [[AdvisorSlidesOutline]]
- [[KeyDecisions]]
- [[ContinuityNotes]]

## Superseded (kept for how the thinking evolved — check the PRD for current state)
- [[TechStack-Early-Superseded]]
- [[AgentSuite-Early-Superseded]]
- [[Scope-Early]]
- [[Timeline-Preliminary]]

## From the PRD's stable sections
- [[PRD-ExecutiveSummary]]
- [[PRD-ProblemsAndBackground]]
- [[PRD-GoalsNonGoalsMetrics]]
- [[PRD-Personas]]

## All notes (live table)
```dataview
TABLE tags, source
FROM "Concept-Notes"
WHERE file.name != "_Index"
SORT tags ASC
```
