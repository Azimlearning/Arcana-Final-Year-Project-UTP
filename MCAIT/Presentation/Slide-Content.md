# MCAIT 2026 slide content

Generated from the deck file. Refer to slide numbers when asking for changes.


## Slide 1. Title slide

MCAIT 2026

Graph-Grounded Generative User Interfaces for Learning: Retrieval Structure Determines Interface Expressiveness

Fakhrul Azim Bin Ahmed Mardzukie  ·  Universiti Teknologi PETRONAS, Malaysia
Presenter: Fakhrul Azim  ·  Parallel Session 6 (Virtual), Track 2

3–5 NOVEMBER 2026  ·  TAIBAH UNIVERSITY  ·  MADINAH

**Say:** Good afternoon. I am Fakhrul Azim from Universiti Teknologi PETRONAS. My paper asks why learners working across their own documents still get a chat box, and what it would take to give them something better.


## Slide 2. The claim of this paper

The components an interface can honestly offer are bounded by what retrieval can supply.

1

Problem

Learners get prose

2

Gap

What the literature leaves open

3

Approach

Compose, do not write

4

Bound

Retrieval limits the catalogue

5

Evaluation

Protocol and results

6

Conclusion

Limits and next steps

**Say:** Here is the claim in one sentence. The interface components a learning system can honestly offer are bounded by what its retrieval layer can supply. I will go through the problem, the gap in the literature, the approach, the formal bound and the evaluation. I will also show Arcana, which is this paper put into practice, and what we measured on it after the paper was accepted.


## Slide 3. Learners ask relational questions and get prose

What a learner asks across their documents

Which of these papers agree?

Where do they conflict?

What does the set not cover?

What they get back

d = 0.83

pooled effect of interactive representations, 20 physics studies, human-authored [5]

Why these views are missing

Someone must author each one per topic
Retrieval has nothing structured to fill it

A flat answer asserts relations it never retrieved, and hands the synthesis back as more text to read [4].

**Say:** When you study across many documents, the useful questions are about relationships: which sources agree, where they conflict, what is missing. Current tools answer with a paragraph, which hands the work of connecting the sources back to the learner. Interactive representations can work very well: one meta-analysis found a pooled effect of 0.83 across twenty physics studies. But that material was authored by people. Comparison grids and concept maps are absent from corpus tools for two reasons: someone must build them per topic, and the retrieval layer has nothing structured to fill them with.


## Slide 4. Flat retrieval has no way to represent a relation

Flat retrieval

Graph-hybrid retrieval

Query

Passage, scored alone

Passage, scored alone

Passage, scored alone

Cited prose
Relations asserted, never retrieved

Query

Temperature

Collision frequency

Activation energy

Effective collisions

Reaction rate

Relational components
Grid, concept map, contradiction alert

Blue: from one document. Gold: from another. A shared entity brings them into one retrieved set. Similarity encodes how alike texts are, not how entities connect [3].

**Say:** The cause sits in retrieval. Standard retrieval scores every chunk independently. It finds the passage most similar to the question, but holds no record that two passages disagree or that one concept depends on another. A larger embedding model does not fix this, because similarity measures how alike two texts are, not how the things inside them connect. Graph retrieval changes what is stored. Entities and relations are extracted, so a shared entity can bring passages from different documents together.


## Slide 5. Four literatures, and the gap between them

| Area | What it establishes | What it leaves open |
|---|---|---|
| Retrieval [1-3, 14-17] | Hybrid and graph retrieval, schema-free extraction | Never treats retrieved structure as a substrate for presentation |
| Generative UI [6, 18-20] | Feasible, preferred to markdown, protocols for typed intent | None asks whether the content is supported by a source |
| Generated artifacts in education [7-9, 21, 22] | Authoring-time generation with a human reviewer | None generates for the learner at request time from evidence |
| Verification and risk [10-13, 23-25] | Adversarial checks for code; risks of generated instruction | Oracles do not transfer; the safety objection stands unanswered |

Gap: a learning interface composed at request time, from retrieved evidence, with a stated bound on what it may assert.

**Say:** Four bodies of work touch this problem. Graph retrieval is evaluated as retrieval, by answer quality. Generative interface work is evaluated by preference, and preference is not correctness in instruction. Educational systems keep a human between generation and learner, so they are safe but limited to what an educator anticipated. And verification work relies on oracles and executable contracts, which a learning presentation does not have. One recent paper argues that runtime generation is unsafe because it cannot be verified at scale. No existing mechanism answers that, and that is the gap.


## Slide 6. Generative interfaces are reaching the market

|   | Gemini Notebook (formerly NotebookLM) | ChatGPT Intelligent UI | Gemini dynamic view | This paper |
|---|---|---|---|---|
| Described input | the learner's uploaded sources and instructions | the question | the prompt, with tools such as web search | evidence retrieved from the learner's corpus |
| How the view arises | the learner picks an output: mind map, data table, flashcards | the model chooses the format automatically | the model designs and codes it per prompt | the model selects from a typed catalogue |
| Stated rule linking a view to retrieved structure | not stated | not stated | not stated | a precondition on every component |

This compares public descriptions only. Not stated does not mean absent, and no product was tested.

Sources, checked 1 Nov 2026: Gemini Notebook Help; OpenAI release notes, 7 Oct 2026; Google Research blog, 18 Nov 2025.

**Say:** This is no longer only a research question, because products are moving the same way. Gemini Notebook, formerly NotebookLM, answers from your sources, and the learner picks an output such as a mind map or a data table. ChatGPT's Intelligent UI chooses the format automatically. Gemini's dynamic view writes custom code for each prompt. I am only reporting what the vendors publish, and I have not tested these systems. The paper makes no claim about how they work inside. What I can say is that none of these public descriptions states a rule linking a view to the retrieved structure that justifies it. Stating that rule is what this paper does.


## Slide 7. Contributions

1

Architecture

Graph-native hybrid retrieval coupled to a typed generative interface. Evidence fills components, not prose.

2

Verified interface layer

Composed at request time. One schema, fail-closed validation, registry-only rendering, provenance on every claim.

3

A formal bound

A definition, with a component-by-component mapping to study activities, that retrieval bounds expressiveness.

4

Committed evaluation

Ablation harness, paired test and extraction audit fixed before any run, with a pilot reported as found.

Arcana is this paper in practice: a learning workspace where the ideas above run, and can be measured.

**Say:** The paper makes four contributions. First, an architecture that couples graph-native hybrid retrieval to a typed generative interface. Second, an interface composed at request time, held to the standard developed for verified generated artifacts. Third, a formal statement that retrieval structure bounds interface expressiveness. Fourth, an evaluation protocol committed before any run, with a pilot reported as found. Arcana is what these ideas look like in practice. The claims belong to the paper, and Arcana is where they can be run and checked.


## Slide 8. The method in thirty seconds

Click the video to play. An illustration of the method, using the worked example from the paper. Not captured output.

**Say:** Here is the whole method in thirty seconds. A learner asks a relational question and today gets a paragraph. Instead, documents become entities and relations, so sources can connect. Three signals are fused by rank, so evidence from different documents arrives together. The model then composes verified components, and writes no markup. A malformed block is rejected at the gate. And what retrieval can supply sets the limit: flat retrieval can honestly fill three of these, and graph-hybrid retrieval can fill all six.


## Slide 9. Three regimes for producing a learning interface

|   | Authored ahead | Markup emitted at runtime | Composed at request time |
|---|---|---|---|
| Coverage | what was anticipated | any question | any question |
| Produced by | a person | the model, as code | the model, as typed selections |
| Correctness rests on | human review | post-hoc verification | retrieved evidence and schema |
| Expressiveness | fixed catalogue | unbounded | combinatorial over a vocabulary |
| Failure mode | no answer exists | confident wrong artifact | closest available component |

Table I of the paper. Runtime markup: assessed as unverifiable at scale [10].

The components are fixed. What is generated per question is which components, and the evidence that fills them.

**Say:** This table is the core of the approach. Authoring ahead is safe, but only covers what someone anticipated. Emitting markup at runtime covers anything, but the field regards it as unverifiable at scale. We take a third route. The model composes from a verified vocabulary, so we keep the coverage of runtime generation and the accountability of authoring. The price is expressiveness: a question whose best answer is an unimplemented view gets the closest available component.


## Slide 10. From document to rendered component

Ingestion, one pass

Hybrid retrieval

Generative interface

Learner's documents

Parse, chunk, embed

Extract entities and relations

Vector index

Knowledge graph

Dense similarity

Sparse keyword (BM25)

Graph traversal, 1 hop

Reciprocal rank fusion

Task agents, one routing function

Typed component selection

Fail-closed validation

Registry-only rendering

RRF(d) = Σr∈R  1 / (k + r(d)),  k = 60     Fusing by rank, because cosine, keyword and traversal scores are not comparable [26].

**Say:** Here is the system design. A document is parsed, chunked and embedded. In the same pass, entities and relations are extracted with no fixed ontology, because a learner's documents can come from any discipline. At query time there are three signals: dense similarity, keyword matching and graph traversal. They are fused by rank using reciprocal rank fusion, because their raw scores are not comparable. The model then selects components and fills them from that evidence. Every request ends at this stage, so no agent can reply to the learner directly, and everything passes validation first.


## Slide 11. The model composes the interface. It does not write it.

In the paper

Fixed

Components, layout, typography, interaction

Chosen per question

Which components, in what order

From retrieved evidence

Every payload that fills them

| Safeguard | Failure it contains |
|---|---|
| One schema generates both sides of the wire | producer and consumer drift |
| Retrieval before synthesis | assertions from outside retrieved material |
| Per-claim checking [25] | unsupported citations |
| Server-side validation that fails closed | malformed presentations |
| Registry-only rendering | unregistered presentations |

Stated in the paper: claim checking fails open on a provider error, and a contradiction quote is not yet matched verbatim. Status: 24 of 24 components registered, 645 tests passing in CI.

**Say:** This is what makes it defensible. The model outputs typed component selections, with payloads built from retrieved evidence. Layout and interaction are not under its control. Each safeguard names the failure it contains. One schema generates both sides of the wire, so a mismatch is a compile error. The validator runs on the server and rejects on any violation. We fail closed on purpose: a visible error can be recovered from, a confident wrong presentation cannot. The paper states the limits too. Malformed interfaces are prevented, but one that misreads a source is still possible.


## Slide 12. Adaptive interface: where expressiveness shows

In the paper

Combinatorial

An ordered selection of k from n components, with payload structure derived per query.

The workspace reshapes

Surveying, revising, drafting and Socratic questioning need different components. Mode is inferred.

Bounded by retrieval

Which layouts are honest depends on the evidence. Expressiveness is the bound's other face.

Click to play. Section IV-A of the paper. Counts in the video are block combinations from one live run of 39 questions.

**Say:** This is where expressiveness becomes visible. The paper's claim is that the space of interfaces is combinatorial: an ordered choice of components from a vocabulary, with payloads decided per question. So the interface adapts. A single-paper question gets an answer and sources. A comparison gets a dashboard. A connected path adds a concept map. And the workspace reshapes with the task, including study. Nobody authored these layouts in advance.


## Slide 13. A worked request from the paper

In the paper

Learner asks:  Why does raising the temperature increase the rate of a reaction?

Cited summary

Contradiction alert

Concept map

Higher temperature gives more frequent collisions [notes], and a larger share of collisions above the activation energy [chapter].

Each claim carries a citation to its source.

Lecture notes
Particles collide more often

Textbook chapter
More collisions exceed the activation energy

Each side shows its document and stance, side by side.

Temperature

Collision frequency

Activation energy threshold

Effective collisions

Concepts linked across the corpus.

Section IV-B of the paper. An illustration of what is composed, not captured output.

**Say:** Here is the example from the paper. A learner revising chemistry asks why raising the temperature increases reaction rate. Their notes attribute it to particles colliding more often. The textbook chapter attributes it mainly to more collisions exceeding the activation energy. Both are real, and the difference in emphasis is what a learner reproduces in an exam without noticing. The graph brings both passages into one retrieved set. A language model then detects the disagreement. It is not read from a typed edge. The response composes three blocks, none authored for this question. A biology question would get a comparison grid instead.


## Slide 14. Retrieval structure bounds interface expressiveness

In the paper

X(R) = { c ∈ C  |  P(c) satisfiable from E(R, q) }        X(flat)  ⊂  X(graph-hybrid)

| Component | Structural precondition | Supplied by | Study activity |
|---|---|---|---|
| Cited summary | ranked passages with sources | flat retrieval | reading, orientation |
| Recall cards | atomic facts with sources | flat retrieval | retrieval practice |
| Comparison grid | documents aligned on shared dimensions | cross-document entity alignment | comparison |
| Contradiction alert | claim pairs on one entity that disagree | co-retrieval via the graph | reconciling sources |
| Concept map | concept-to-concept relations | graph traversal | organising knowledge |

The catalogue a generative learning interface can honestly offer is a function of the retrieval beneath it.

**Say:** This is the central idea. A component is a claim about the shape of an answer. A comparison grid claims that documents line up on shared dimensions. A concept map claims that concepts stand in labelled relations. So we define expressiveness as the set of components whose preconditions a retrieval layer can satisfy from evidence alone. Flat retrieval can of course draw a grid. But to fill it, the model must supply a relation retrieval never returned. A rich catalogue on flat retrieval is not richer. Its extra components are filled by the model, in a more convincing package than prose.


## Slide 15. Committed protocol, and a pilot reported as found

In the paper

Protocol, fixed 9 June 2026

20 questions: 12 cross-document, 4 single-document, 4 contradiction
16 public papers, 1,570 chunks
5 arms: dense, sparse, graph, flat, hybrid
Metrics: distinct sources, latency
Paired Wilcoxon, hybrid against flat

| Arm | Mean distinct sources | Median latency (ms) |
|---|---|---|
| Dense only | 2.50 | 670 |
| Sparse only | 3.35 | 208 |
| Graph only | 0.60 | 2,500 |
| Flat (dense + sparse) | 3.15 | 897 |
| Hybrid (all three) | 3.15 | 900 |

Null: tied on 18 of 20 questions (p = 1.0). Traversal returned nothing on 15 of 20. The pilot locates the ceiling in query entity resolution.

Pilot index: 4 of 16 documents (796 nodes, 859 edges). Table V of the paper.

**Say:** The protocol was committed before any run: twenty questions, with signals switched off one at a time across five arms. Extraction was interrupted by a provider quota, so the paper reports a pilot on four of sixteen documents. The result was null. Hybrid and flat tied on eighteen of twenty questions. The reason is the finding: traversal returned nothing on fifteen questions, because query entities needed an exact match to a graph node. On those questions the hybrid simply was flat retrieval. So the pilot does not test the graph. It shows that the ceiling on the graph signal is query entity resolution.


## Slide 16. Where Arcana began: VERA AI

|   | VERA AI | Arcana |
|---|---|---|
| Knowledge | Flat vector chunks, one silo per document | Entities and relations across all documents |
| Retrieval | BM25 + vector, fused by RRF | BM25 + vector + graph traversal, fused by RRF |
| Agents | Six fixed, independent agents | Task agents, routed through one function |
| Interface | Static three-panel layout | Typed components composed per question |
| Domain | Enterprise knowledge base | Learners working across their own documents |

VERA could cite its answers, but had nothing structured to show how sources relate. That limit is what this paper formalises.

A design comparison, not a benchmark: different domains and corpora.

**Say:** Before the results, a word on where this came from. Arcana grew out of VERA AI, an enterprise knowledge assistant from my internship. VERA already had hybrid retrieval and a no-citation, no-answer policy. But documents were separate silos, the layout was fixed, and the agents did not work together. Working on it showed me the limit this paper formalises: a system with flat retrieval can cite its answers well, but it has nothing structured to show how sources relate. This is a comparison of designs, not of results, because the domains and corpora are different.


## Slide 17. Arcana: the paper in practice

After the paper

Click to play. First three screens: real-model run. Learning tools: no model call. The lab's function is a test fixture, passed through the real verifier.

Same corpus, different shapes

A summary with a graph, a comparison grid, or a refusal, depending on the question.

Grounded relations

Each stated relation shows the sentence and page behind it.

Beyond answers

A quiz, mastery on the graph, and a lab verified on every slider setting.

**Say:** This is Arcana on the sixteen retrieval papers. First, three questions with a real model. A relational question gets a cited summary and a graph. A comparison gets a grid. A question the papers cannot answer gets a refusal. Nobody designed these screens for these questions. Then the learning tools. Concept pages show the sentences behind each link. A wrong quiz answer is corrected, and the graph recolours by mastery. And a lab appears only where a passage states the formula.


## Slide 18. What retrieval structure makes possible

After the paper

*[Image: Knowledge graph]*

| Paper | BM25 | Graph traversal |
|---|---|---|
| RAG Survey | "a sparse encoder (BM25) and a dense retriever" (page 9) | No evidence in this paper |
| RAG with Graphs | "Methods like BM25 and TF-IDF primarily focus on lexical signals" (page 9) | "GraphRAG employs graph traversal methods" (page 5) |
| From Local to Global | No evidence in this paper | No evidence in this paper |

11,173 concepts, 13,972 edges, 11.6% of concepts in 2+ papers

A real comparison grid: quote and page, or an honest gap

Real graph, 16 papers. Drawn: the most widely shared concepts. About a third of edges are stated in one sentence. Grid simplified from Arcana, quotes shortened.

**Say:** Here is what that structure looks like. On the left is part of the real graph extracted from the sixteen papers, showing the concepts found across the most papers. About one in nine concepts appears in two or more papers, and those are the points where documents connect. You can also see an extraction weakness: LLM and LLMs are separate nodes. On the right is part of a comparison grid filled from that structure. Each cell is a quote from that paper with its page. Where a paper has nothing to say, the cell says so instead of inventing an answer.


## Slide 19. Beyond the catalogue: generated, then verified

After the paper

Level 1: typed components
Fixed, verified, filled from evidence

Level 2: adaptive layout
Arranged per question and task

Level 3: generated component
Written per question, shown only if verified

*[Image: Hooke's law]*

Hooke's law

*[Image: Acid-base titration]*

Acid-base titration

*[Image: Newton's cannonball]*

Newton's cannonball

The trust path: the model plans over an audited kit, a real browser moves every control, only the verifier can mint the deliverable, and it runs in a sandbox.

219 of 224

planted defects refused, 0 of 30 false alarms

20 of 20

hostile attack shapes blocked

13 of 14

new questions built a lab, labelled model-checked

Synapse, by Team EduNova (UTP), Form 4 and 5 science. Prototype screens. Planted sets written by the team. No teacher review or learner study yet.

**Say:** The paper names a cost: the catalogue is a ceiling. A question whose best answer is an interactive experiment gets the closest component. Our team's system, Synapse, explores the way past that ceiling for school science. The model plans a lab over an audited kit, and a verifier runs it in a real browser before a student can see it. Arcana's formula labs use the same discipline. This is a different domain, so I do not compare results.


## Slide 20. On the full corpus, a retrieval gain is not shown

After the paper

*[Chart: nDCG at 10. Original 19 questions: flat 0.169, hybrid 0.208. New 19: flat 0.394, hybrid 0.352. Pooled 38: flat 0.281, hybrid 0.280.]*

| Question set | Hybrid minus flat | Better / tied / worse | p |
|---|---|---|---|
| Original 19, cross-document | +0.039 | 7 / 8 / 4 | 0.15 |
| New 19, declared extension | -0.042 | 2 / 6 / 11 | 0.068 |
| Pooled 38 | -0.001 | 9 / 14 / 15 | 0.69 |

No pair reaches p < 0.05. Not shown to help is not the same as shown not to help.

nDCG@10 against gold passages, 16 papers, 1,570 passages, paired Wilcoxon. A different metric from the pilot. Not peer reviewed.

**Say:** Now the findings since the paper. We completed the study the paper called for: all sixteen papers, the repaired entity matching, and a gold set of relevant passages. The graph signal now fires. On the original harder, cross-document questions, the hybrid is ahead, but not significantly. On nineteen new questions, which lean towards single papers, it falls behind. Pooled, the difference is essentially zero. So I do not claim a retrieval gain. Not shown to help is not the same as shown not to help, but this corpus gives no support for that claim. The metric here is nDCG, so please do not compare it with the pilot.


## Slide 21. The graph does extend the interface: 2 components against 5

After the paper

*[Chart: Questions admitted of 20. Flat: cited summary 20, source list 20, graph view 0, comparison grid 0, concept map 0. Hybrid: 20, 20, 16, 20, 3.]*

What is measured

How often the evidence for each component exists, of 20 questions.

What is by construction

Flat admits none of the three. The preconditions read graph structure.

What it does not show

Admitted is not correct or useful. The grid is not yet selective.

Admission over 20 questions, one graph, five components measured. Not peer reviewed.

**Say:** Here is the other half of the argument. For each question, we counted which components had their preconditions met by the evidence. Flat retrieval admits two. The hybrid layer realises all five. Please read this carefully. That flat cannot admit the other three follows from how the preconditions are defined, so it is not a discovery. What the measurement adds is how often the evidence exists: a connection graph on sixteen questions, and a multi-hop path on only three, because every hop must be grounded in a stored sentence. And admitted does not mean useful. The grid was admitted on every question, so it is not yet selective.


## Slide 22. Grounding holds with a real model, relevance is not yet shown

After the paper

38 of 38

answerable questions answered

1 of 1

unanswerable control refused

125 of 125

quotes verbatim from the stored passage

10 of 140

claims removed as unsupported by the judge

0.21

citation precision

0.21

gold recall

19 of 38

answers cite no gold-relevant passage

Nothing appears without a verbatim source. Grounded and relevant are different things.

One live run, one model, no repeat. The gold set is a floor, not a full list. Not peer reviewed.

**Say:** We also ran the whole system with a real model. All thirty-eight answerable questions were answered. The one question the corpus cannot answer was refused. All one hundred and twenty-five citations were verbatim. And the judge removed ten claims that had a real citation under them but were not supported by it, which is the case for checking each claim. But look at the second row. Citation precision is about 0.21, and half the answers cite nothing in the gold set. The gold set is incomplete, so this does not show the answers are wrong. It does show that grounded and relevant are different things.


## Slide 23. What this does and does not show

Established

Interface guarantees hold by construction
The bound follows from preconditions
Grounding held in one live run

Not shown

A retrieval gain from the graph
Correctness of what is admitted
Extraction quality, by human audit
Any learning outcome

Next

Human audit of graph links
Check each block against its own edges at build time
Make components more selective
Run the interface study

The components an interface can honestly offer are those whose preconditions retrieval can satisfy.

**Say:** To conclude. The interface guarantees hold by construction, and the bound follows from the preconditions. The empirical picture is more modest. There is no evidence of a retrieval gain from the graph on this corpus, and no evidence yet about learning, because no user study has been run. Next comes a human audit of the graph's links, checking each block against its specific evidence at build time, and the interface study itself. The point I would like you to keep is this: the components an interface can honestly offer are those whose preconditions retrieval can satisfy.


## Slide 24. Selected references

[1] Y. Gao et al., RAG for large language models: a survey, arXiv:2312.10997, 2024.
[2] B. Sarmah et al., HybridRAG, arXiv:2408.04948, 2024.
[3] D. Edge et al., From local to global: a graph RAG approach, arXiv:2404.16130, 2024.
[4] R. E. Mayer, Cognitive theory of multimedia learning, Educ. Psychol. Rev., 2024.
[5] M. A. Fadillah et al., Meta-analysis of PhET simulations, Int. J. Online Biomed. Eng., 2026.
[6] Y. Leviathan et al., Generative UI, arXiv:2604.09577, 2026.
[7] S. Tu et al., MAIC-UI, arXiv:2604.25806, 2026.
[8] T. Calò and C. J. MacLellan, Educator-driven tutor authoring, L@S '24, 2024.
[9] X. J. Wang et al., LearnMate², DIS '26, 2026.
[10] S. P. Neshaei et al., The missing layer, arXiv:2606.15902, 2026.
[11] J. Irigoyen et al., EduEVAL-DB, arXiv:2602.15531, 2026.
[12] A. Shoufan and A. A. A. Esmaeil, AI hallucination from students' perspective, arXiv:2602.17671, 2026.
[13] J. Liao et al., Code monitor red teaming, arXiv:2607.20852, 2026.

[14] H. Han et al., RAG with graphs (GraphRAG), arXiv:2501.00309, 2024.
[15] B. J. Gutiérrez et al., HippoRAG, NeurIPS, 2024.
[16] Z. Guo et al., LightRAG, arXiv:2410.05779, 2024.
[17] T. Zhang and H. Soh, Extract, define, canonicalize, EMNLP, 2024.
[18] Y. Liu et al., AlignUI, arXiv:2601.17614, 2026.
[19] Y. Liu et al., CrowdGenUI, arXiv:2411.03477, 2024.
[20] Agent2UI, technical specification, 2025. Not peer reviewed.
[21] Y. Ben-Zion et al., AI for rapid generation of physics simulations, arXiv:2412.07482, 2024.
[22] T. N.-D. Tran et al., ChemersiveLLM, VRST '25, 2025.
[23] X. Li et al., Beyond superficial tests, Findings of ACL 2026.
[24] Q. Li et al., AdverMCTS, arXiv:2604.10449, 2026.
[25] J. Kwok et al., LLM-as-a-verifier, arXiv:2607.05391, 2026.
[26] G. V. Cormack et al., Reciprocal rank fusion, SIGIR, 2009.

**Say:** These are the references cited on the slides, numbered as in the paper. The full list is in the proceedings.


## Slide 25. Thank you

MCAIT 2026

Thank you

Questions are welcome.

Fakhrul Azim Bin Ahmed Mardzukie
fakhrul_22012087@utp.edu.my
github.com/Azimlearning/Arcana

3–5 NOVEMBER 2026  ·  TAIBAH UNIVERSITY  ·  MADINAH

**Say:** Thank you. The code and protocol are public, and I am happy to take questions.


---

Spoken length: 2093 words, about 16.1 minutes at 130 words a minute.


# Questions to prepare

**If the graph does not improve retrieval, why use it?**
Ranking is not its only job. On this corpus it has not been shown to rank better, but it supplies the relations that relational components need. Whether those components help learners is still untested.

**Isn't the bound true by definition?**
The subset relation is, and I say so. Its value is as a design rule: it forces you to state what each component asserts. The empirical part is how often the preconditions are met.

**Could a language model not just fill the grid from flat passages?**
It could, and it would often look fine. But the relation would come from the model, not from retrieved evidence, and that is the failure the education literature warns about.

**How is a contradiction computed?**
As the paper specifies, the graph helps place passages from different documents in one retrieved set, and a language model then detects the disagreement. It is not read from a typed edge, there is no numeric confidence, and the quote is not yet matched verbatim.

**Can you show a contradiction alert in Arcana today?**
The paper specifies it, and the current Arcana build does not yet carry contradiction judging. The screens shown are comparison, graph and cited summary.

**How does this compare with NotebookLM or ChatGPT?**
I only reported their public descriptions and did not test them. They may ground their views well. The paper removed a commercial comparison during review, because judging that needs documentation they do not publish.

**Is Synapse part of this paper?**
No. It is a separate system by my team, for school science, shown as the route past the paper's catalogue ceiling. Its results use different questions and metrics, so they are not compared with Arcana.

**Doesn't a generated lab break your argument against model-written interfaces?**
The paper objects to generated output reaching a learner unchecked. Here nothing is delivered unless a verifier has passed it, and every displayed number comes from an audited model. It works in a narrow domain where the science can be checked in code.

**Why are the new results not in the paper?**
They were measured after the camera-ready deadline, using the questions and corpus manifest the paper committed to, plus an extension declared before it was run.

**Are the 38 questions biased?**
Possibly. I drafted the extension questions myself, they lean towards single papers, and the extension has no contradiction questions. That is why the two sets are shown separately.

**How good is the extracted graph?**
Not yet established by a human. An assistant-labelled sample put asserted links at 0.86 and co-mention links at 0.58, but that is one labeller from the same model family as the extractor, and 30 of the 100 sampled sentences were bibliography entries. The human audit is still open.

**Did you measure learning?**
No. No user study has been run, and the interface study has not been conducted.

**How did VERA perform against Arcana?**
The slide compares designs only, because the domains and corpora differ. It makes no performance comparison.
