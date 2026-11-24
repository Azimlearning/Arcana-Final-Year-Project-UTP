# Synapse (formerly Arcana): A GraphRAG-Powered Generative UI Platform for Interactive Learning

**Final Year Project, Bachelor of Computer Science (Hons), Universiti Teknologi PETRONAS**

Fakhrul Azim Bin Ahmed Mardzukie. Supervisor: Dr Mazeyanti Bt M Ariffin. Co-supervisor:
AP Dr Noreen Izza Bt Arshad.

**Achievements:** MCAIT 2026 paper accepted and presented; Most Popular Team Award at the hackAstone 2026 Grand Final;
Top 10 finalist at UTP CodeFest '26 and the Codex Community Hackathon KL. See [`ACHIEVEMENTS.md`](ACHIEVEMENTS.md).

The project began as **Arcana** (FYP1) and became **Synapse** for FYP2: the same GraphRAG engine, plus an engine that
turns a science question into a tested interactive simulation. The paragraph below describes the Arcana core that the
paper is about.

Arcana is a learning workspace for a student's own documents. Documents are extracted into a
knowledge graph alongside a vector index; retrieval fuses graph traversal with dense and sparse
signals by rank; and the answer to a question is a composed, generative interface rather than a
stream of prose. The interface is held to a strict contract: typed components only, validated before
delivery, filled from retrieved evidence.

## Publication

> F. A. B. Ahmed Mardzukie, "Graph-Grounded Generative User Interfaces for Learning: Retrieval
> Structure Determines Interface Expressiveness," in *Proc. 6th International Multi-Conference on
> Artificial Intelligence Technology (MCAIT 2026)*, Madinah, Saudi Arabia, Nov. 2026. Accepted and presented on 5 November 2026.

The accepted manuscript and its LaTeX source are in [`Technical-Paper/`](Technical-Paper/). See
[`NOTICE.md`](NOTICE.md) for the IEEE copyright notice.

## Code

| Version | Repository | Status |
|---|---|---|
| Arcana v1 | [Azimlearning/Arcana](https://github.com/Azimlearning/Arcana) | Frozen at tag `v1.0`, the system the paper describes |
| Arcana v2 | [Azimlearning/Arcana-v2](https://github.com/Azimlearning/Arcana-v2) | Frozen: the version before Synapse |
| **Synapse (FYP2)** | [Azimlearning/Synapse-fyp2](https://github.com/Azimlearning/Synapse-fyp2) | **The final code**: Arcana v2 continued, with the simulation engine and the new interface |

## What is in this repository

| Folder | Contents |
|---|---|
| `ACHIEVEMENTS.md` | Competitions, awards and the publication, with dates and exactly what each result was |
| `FYP2-Final/Viva-Presentation/` | The FYP2 viva slides (PDF), presented 24 Nov 2026 |
| `Technical-Paper/` | The MCAIT 2026 paper: accepted manuscript (PDF), LaTeX source and figures, literature notes |
| `MCAIT/` | The MCAIT 2026 talk: slide decks, plain-language script, slide plan, evidence sources and the scripts that build the decks. The registration records, correspondence and reviews are not published |
| `Concept-Notes/` | Project concept, objectives, personas, scope and key decisions from the proposal stage |
| `concept/` | The original FYP context document and an architecture sketch |
| `proposal defence stuff/` | The proposal defence deck, speaking script and core narrative |
| `Interim-report/Literature-review/` | One note per paper cited in the FYP1 interim report |

This is a curated public subset of the project's working archive. Forms, signed documents and
review material are kept private.
