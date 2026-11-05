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

**Say:** Here is the claim in one sentence. The components a learning interface can honestly offer are bounded by what its retrieval can supply. I will take you through the problem, the method with one real worked question, the bound, and what we measured.


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

**Say:** When you study across documents, the useful questions are about relationships: which sources agree, where they conflict, what is missing. Current tools answer with a paragraph. Interactive views can work very well, with a pooled effect of 0.83 in physics, but someone has to author them, and retrieval has nothing structured to fill them with.


## Slide 4. Three learners hit the same wall

A

Aisha

Final-year undergraduate writing a literature review

THEIR QUESTION

How do 15 to 20 papers relate, agree and conflict?

THE VIEW IT CALLS FOR

Comparison grid, contradiction view

D

Daniel

Master's student with a growing thesis corpus

THEIR QUESTION

What does my corpus not cover yet?

THE VIEW IT CALLS FOR

Connected knowledge base, gap view

M

Mei

Undergraduate revising dense modules for exams

THEIR QUESTION

Summaries help me read. How do I remember?

THE VIEW IT CALLS FOR

Quizzes, flashcards, Socratic questions

Design personas from the project requirements, not study participants.

**Say:** Picture three learners. Aisha is writing a literature review across twenty papers and connects them by hand. Daniel keeps a growing thesis corpus and keeps losing context. Mei is revising, and summaries help her read but not remember. Each needs a different view of the same documents, and each gets the same chat box.


## Slide 5. Flat retrieval has no way to represent a relation

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

**Say:** The cause sits in retrieval. Standard retrieval scores every passage on its own. It holds no record that two passages disagree or that one concept depends on another. Graph retrieval changes what is stored, so a shared entity can bring passages from different documents together.


## Slide 6. Four literatures, and the gap between them

| Area | What it establishes | What it leaves open |
|---|---|---|
| Retrieval [1-3, 14-17] | Hybrid and graph retrieval, schema-free extraction | Never treats retrieved structure as a substrate for presentation |
| Generative UI [6, 18-20] | Feasible, preferred to markdown, protocols for typed intent | None asks whether the content is supported by a source |
| Generated artifacts in education [7-9, 21, 22] | Authoring-time generation with a human reviewer | None generates for the learner at request time from evidence |
| Verification and risk [10-13, 23-25] | Adversarial checks for code; risks of generated instruction | Oracles do not transfer; the safety objection stands unanswered |

Gap: a learning interface composed at request time, from retrieved evidence, with a stated bound on what it may assert.

**Say:** Four literatures touch this. Graph retrieval is evaluated as retrieval. Generative interfaces are evaluated by preference. Educational systems keep a human reviewer. Verification relies on oracles a learning view does not have. One recent paper argues runtime generation is unsafe because it cannot be verified at scale, and that objection stands unanswered.


## Slide 7. Generative interfaces are reaching the market

|   | Gemini Notebook (formerly NotebookLM) | ChatGPT Intelligent UI | Gemini dynamic view | This paper |
|---|---|---|---|---|
| Described input | the learner's uploaded sources and instructions | the question | the prompt, with tools such as web search | evidence retrieved from the learner's corpus |
| How the view arises | the learner picks an output: mind map, data table, flashcards | the model chooses the format automatically | the model designs and codes it per prompt | the model selects from a typed catalogue |
| Stated rule linking a view to retrieved structure | not stated | not stated | not stated | a precondition on every component |

This compares public descriptions only. Not stated does not mean absent, and no product was tested.

Sources, checked 1 Nov 2026: Gemini Notebook Help; OpenAI release notes, 7 Oct 2026; Google Research blog, 18 Nov 2025.

**Say:** Products are moving the same way. Gemini Notebook answers from your sources. ChatGPT chooses a format automatically. Gemini's dynamic view writes code per prompt. I report only what vendors publish, and I did not test them. None of these public descriptions states a rule linking a view to the retrieved structure behind it. Stating that rule is this paper's work.


## Slide 8. Contributions

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

**Say:** The paper makes four contributions: the architecture, a verified interface layer, the formal bound, and a committed evaluation. Arcana is these ideas in practice. The claims belong to the paper, and Arcana is where they can be run and checked.


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

**Say:** Authoring ahead is safe, but covers only what someone anticipated. Emitting markup at runtime covers anything, but is hard to verify. We take a third route: the model composes from a verified vocabulary. The price is expressiveness, because a question gets the closest available component.


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

**Say:** Here is the design. Ingestion writes a vector index and a graph in one pass. Three signals are fused by rank. Task agents hand off through one routing function, and every path ends at validated components. Let me now walk one real question through this.


## Slide 11. Ingestion: a sentence becomes an edge

After the paper

Schema-free

Entities and relations are extracted with no fixed ontology, so any discipline works.

One pass

The vector index and the graph are written together, over the same passages.

One concept, three papers

BM25 is one node reached from all three passages, across document boundaries.

Click to play. Real sentences and edges from the stored graph of 16 papers. Extraction by one model, one pass per passage.

**Say:** Let me follow one real question through the system, starting with ingestion. Here are real sentences from three papers in the corpus. Extraction turns each stated relation into an edge. The same concept, BM25, appears in all three, so three documents become connected. Nobody defined these relation types in advance.


## Slide 12. What the extracted graph really holds

After the paper

*[Chart: Largest hubs by edges: GraphRAG 477, RAG 420, Large Language Models 299, Knowledge graphs 268, Self-RAG 240, LLMs 198, LLM 177]*

From 13,972 edges to those stated in one sentence

13,972

All edges

9,821

Both labels in the source passage

4,830

Stated in one sentence

11.6%

of concepts appear in 2 or more papers

20.4%

of concepts have no edge at all

1,604

relation strings; authorship alone is spelled four ways

3

nodes for one idea: "Large Language Models", "LLMs", "LLM"

Structure only, not correctness. 'Stated' is a strict lexical test, so the rest are not necessarily wrong. 16 papers, 1,570 passages, one extraction.

**Say:** This is what that produces at scale: over eleven thousand concepts and nearly fourteen thousand edges. On the left, the biggest hubs. On the right, the honest part. Only about a third of edges are stated in one sentence of their passage. Only eleven point six percent of concepts appear in more than one paper, and one idea can be several nodes. So the cross-document structure is real, but thin.


## Slide 13. Graph traversal: one real route

After the paper

Across 20 questions

111 concepts resolved, 37% by approximate match. 16 to 755 edges followed per question.

How passages are reached

87% mention a resolved concept. 13% come only through a neighbour.

Hubs are noisy

Broad seeds such as "Retrieval" pull in passages that are not relevant.

Click to play. Real route for question q-cross-06. Gold-relevant means covering an approved gold passage under the frozen rule.

**Say:** Now the question: how do the papers compare BM25 with dense retrieval? Its words resolve to four concepts. From those, the system follows seventy-four edges, one hop out. Passages that mention those concepts are then ranked. Three of the top ten are relevant, and they all came through BM25. The broad concept Retrieval drags in noise. That is resolution quality showing through.


## Slide 14. Rank fusion: why a second vote matters

After the paper

Comparable by rank

Cosine, keyword and traversal scores differ in kind, so only ranks are combined [26].

A second vote

The rank 2 passage: dense 6, graph 7. Flat ranked it outside its top 10.

Chosen as an example

This is one of the largest gains. The next slides show the whole distribution.

Click to play. Scores recomputed from the stored rankings at k = 60; ties keep the stored order. Question q-cross-06.

**Say:** Here is the fusion, with real numbers. The FEVER passage gets a vote from keywords and one from the graph, and rises to first. The second passage was not in the flat top ten at all, and got in only because the graph gave it a second vote. nDCG goes from point two four to point five nine. But this is one of the largest gains. Averaged over all questions, the difference is zero.


## Slide 15. Composition: verified components, nothing else

In the paper

Fails closed

One schema generates both sides of the wire. Any violation becomes an error, not a partial render.

Registry only

An unregistered block has no path to the screen, and omitting one fails the build.

Stated in the paper

Claim checking fails open on a provider error. Contradiction quotes are not yet matched verbatim.

Click to play. Illustration of the method, using the paper's worked example. 24 of 24 components registered, 645 tests passing in CI.

**Say:** With evidence in hand, the model composes. It picks typed components and fills them from what was retrieved. It writes no markup. A malformed block hits the validator on the server and is rejected, not repaired. We fail closed on purpose: a visible error can be recovered from, a confident wrong presentation cannot. The paper also states the gaps, shown here.


## Slide 16. Adaptive interface: where expressiveness shows

In the paper

Combinatorial

An ordered selection of k from n components, with payload structure derived per query.

The workspace reshapes

Surveying, revising, drafting and Socratic questioning need different components. Mode is inferred.

Bounded by retrieval

Which layouts are honest depends on the evidence. Expressiveness is the bound's other face.

Click to play. Section IV-A of the paper. Counts in the video are block combinations from one live run of 39 questions.

**Say:** This is where expressiveness becomes visible. The paper's claim is that the space of interfaces is combinatorial: an ordered choice of components from a vocabulary, with payloads decided per question. So the interface adapts. A single-paper question gets an answer and sources. A comparison gets a dashboard. A connected path adds a concept map. And the workspace reshapes with the task, including study. Nobody authored these layouts in advance.


## Slide 17. One request, traced end to end

After the paper

Orchestrator
routes: compare

Graph
structure, alignment

Research
8 passages, 6 quotes

Fact Checker
removed 1 of 6

Composer
5 blocks

Question q-cross-01: 11.1 seconds, about US$0.02

Routing across 39 questions

29

compare

9

single

1

relate

Agents never import each other. Every hand-off goes through one routing function, within hop and token budgets.

*[Chart: Seven combinations of components across 39 questions: 13, 9, 6, 5, 3, 2 and 1 questions]*

7 combinations of components across 39 questions

One live run, real model, no repeat. Route = TraversalView. Every combination also includes a cited summary and a source list.

**Say:** This is one real turn from the live run. The Orchestrator routes it, the Graph agent and Research gather evidence, and the Fact Checker removed one of six claims. Agents never call each other directly, and every path ends at composition. And across thirty-nine questions, there were seven different combinations of components. That is the interface following the question.


## Slide 18. A worked request from the paper

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

**Say:** Here is the paper's teaching example. A chemistry learner asks why temperature raises reaction rate. Their notes stress collision frequency, and the chapter stresses activation energy. That difference is what a learner reproduces in an exam. The response composes three blocks, none authored for this question. A language model detects the disagreement, not a typed edge.


## Slide 19. Retrieval structure bounds interface expressiveness

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

**Say:** Formally: a component is a claim about the shape of an answer, and its precondition is what must hold in the evidence. Expressiveness is the set of components a retrieval layer can satisfy. So the catalogue you can honestly offer is a function of the retrieval beneath it.


## Slide 20. The bound, as a picture

In the paper

Not a rendering limit

Any renderer can draw a grid. The question is what fills it.

A design rule

Admit a component only once retrieval can satisfy what it asserts.

Why it matters

A rich catalogue on flat retrieval is filled by the model, not by evidence.

Click to play. Illustration of Table III of the paper.

**Say:** Here is the bound as a picture. Each retrieval layer can honestly fill only some components. Flat retrieval lights up three. Graph-hybrid lights up all six. The dark ones on the left could still be drawn, but the model would have to supply the relation itself.


## Slide 21. Committed protocol, and a pilot reported as found

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

**Say:** The protocol was committed before any run. A provider quota stopped extraction, so the paper reports a pilot on four of sixteen documents. The result was null, and traversal returned nothing on fifteen questions, because entities needed an exact match. So the pilot located the ceiling: query entity resolution.


## Slide 22. Where Arcana began: VERA AI

|   | VERA AI | Arcana |
|---|---|---|
| Knowledge | Flat vector chunks, one silo per document | Entities and relations across all documents |
| Retrieval | BM25 + vector, fused by RRF | BM25 + vector + graph traversal, fused by RRF |
| Agents | Six fixed, independent agents | Task agents, routed through one function |
| Interface | Static three-panel layout | Typed components composed per question |
| Domain | Enterprise knowledge base | Learners working across their own documents |

VERA could cite its answers, but had nothing structured to show how sources relate. That limit is what this paper formalises.

A design comparison, not a benchmark: different domains and corpora.

**Say:** A word on where this began. Arcana grew out of VERA AI, an enterprise assistant from my internship, which already cited its answers. But documents were silos and the layout was fixed. It could cite well, yet had nothing structured to show how sources relate. This compares designs, not results.


## Slide 23. Demo: same corpus, different questions

After the paper

Relational question

A cited summary, and relations that each cite their sentence.

Comparison

A grid. Each cell quotes its source, or says "No evidence in this paper".

Unanswerable

It says so, instead of inventing an answer.

Click to play. Real-model run on 16 papers.

**Say:** This is Arcana on the sixteen papers, with a real model. A relational question gets a cited summary and a graph. A comparison gets a grid, where a cell says no evidence if a paper has nothing. A question the papers cannot answer gets a refusal. Nobody designed these screens in advance.


## Slide 24. Demo: from answers to learning

After the paper

Concept pages

Built from the graph. Every stated link shows its sentence and page.

Quiz and mastery

A wrong answer is corrected with its source, and the graph recolours.

Verified lab

Offered only where a passage states the formula. 120 of 120 planted defects refused.

Click to play. No model call in these tools. The lab's function is a test fixture, passed through the real verifier. Planted set written by the project.

**Say:** And the learning side. Concept pages are built from the graph, and each stated link shows its sentence and page. The quiz comes from the learner's own documents. A wrong answer is corrected, and the graph recolours by mastery. And a lab is offered only where a stored passage states the formula, verified across every slider setting.


## Slide 25. Beyond the catalogue: generated, then verified

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


## Slide 26. On the full corpus, a retrieval gain is not shown

After the paper

*[Chart: nDCG at 10. Original 19 questions: flat 0.169, hybrid 0.208. New 19: flat 0.394, hybrid 0.352. Pooled 38: flat 0.281, hybrid 0.280.]*

| Question set | Hybrid minus flat | Better / tied / worse | p |
|---|---|---|---|
| Original 19, cross-document | +0.039 | 7 / 8 / 4 | 0.15 |
| New 19, declared extension | -0.042 | 2 / 6 / 11 | 0.068 |
| Pooled 38 | -0.001 | 9 / 14 / 15 | 0.69 |

No pair reaches p < 0.05. Not shown to help is not the same as shown not to help.

nDCG@10 against gold passages, 16 papers, 1,570 passages, paired Wilcoxon. A different metric from the pilot. Not peer reviewed.

**Say:** After the paper we completed the study: all sixteen papers, repaired matching, and a gold set. On the harder original questions the hybrid is ahead, not significantly. On new questions it falls behind. Pooled, the difference is zero. So I claim no retrieval gain. Not shown to help is not the same as shown not to help.


## Slide 27. Every question: the graph helps some and hurts others

After the paper

*[Chart: Hybrid minus flat nDCG for 38 questions, sorted, from minus 0.343 to plus 0.420. 15 worse, 14 tied, 9 better.]*

Hybrid minus flat, nDCG@10, 38 questions sorted

9

better

14

tied

15

worse

| Set, category | n | Flat | Hybrid |
|---|---|---|---|
| Original, cross-document | 12 | 0.126 | 0.197 |
| Original, single-document | 3 | 0.399 | 0.363 |
| Original, contradiction | 4 | 0.124 | 0.124 |
| New, cross-document | 11 | 0.268 | 0.217 |
| New, single-document | 8 | 0.566 | 0.537 |

Range: -0.343 to +0.420. Mean nDCG@10 per set. No pair reaches p < 0.05. Questions were not randomly sampled. Not peer reviewed.

**Say:** Here is every question, sorted. Nine improve with the graph, fourteen tie, fifteen get worse. So the average hides large swings in both directions. The table shows where. On the original cross-document questions the hybrid is ahead. On single-document questions, it is behind. A good system would know when to use the graph, and that is a direction this suggests.


## Slide 28. What we tried, and what did not hold up

After the paper

| Change | Looked like | When tested | Verdict |
|---|---|---|---|
| 30 candidates per signal | Recall@10 +0.093, 19 questions (p = 0.094) | -0.007 on 19 new questions (p = 1.0) | Reversed, by a rule fixed in advance |
| Graph signal at larger scale | -0.022 at 285 passages, +0.039 at 1,570 | -0.042 on new questions, -0.001 pooled | Did not replicate |
| Pretrained cross-encoder re-ranker | Standard next step | -0.007 nDCG@10 (p = 0.90), about 5 s per query | Left off |
| Cleaner atomic-note graph | 61% of the nodes, 40% of the edges | +0.010 fused, pooled (p = 0.86) | About level from a smaller graph |

The rule for the new questions was fixed before they ran, so a result could not be quietly kept.

Descriptive, 38 questions in two differently drawn sets, one corpus. Not peer reviewed.

**Say:** Evaluation also killed some of our own ideas. On the original questions, deeper retrieval looked like a real gain, but a rule fixed in advance reversed it when it failed on new questions. The graph seemed to help more as the corpus grew, and that did not replicate either. A trained re-ranker did not help. A cleaner graph with forty percent of the edges did about as well. I report these because negative results are part of the evidence.


## Slide 29. The graph does extend the interface: 2 components against 5

After the paper

*[Chart: Questions admitted of 20. Flat: cited summary 20, source list 20, graph view 0, comparison grid 0, concept map 0. Hybrid: 20, 20, 16, 20, 3.]*

What is measured

How often the evidence for each component exists, of 20 questions.

What is by construction

Flat admits none of the three. The preconditions read graph structure.

What it does not show

Admitted is not correct or useful. The grid is not yet selective.

Admission over 20 questions, one graph, five components measured. Not peer reviewed.

**Say:** The other half. Flat retrieval admits two of five measured components, and the hybrid all five. That flat cannot admit the other three follows from the definitions. What we measured is how often the evidence exists: sixteen questions for a graph, three for a multi-hop path. Admitted does not mean useful.


## Slide 30. Grounding holds with a real model, relevance is not yet shown

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

**Say:** With a real model, all answerable questions were answered, the unanswerable one was refused, and every quote was verbatim. But citation precision is about 0.21. The gold set is incomplete, so this does not show the answers are wrong. It does show that grounded and relevant are different things.


## Slide 31. We tested the checkers too

After the paper

*[Chart: Planted defects detected of 50: quote not verbatim 50, wrong passage 50, wrong document 50, invented other document 49, invented same document 48, negated claim 0]*

Fact-check defects detected, of 50 each, word-overlap rule only

The blind spot

Word overlap cannot see a negated or altered claim: 0 of 50.

Why a judge is needed

In the live run the model judge removed 10 of 140 claims under valid quotes.

Clean answers

50 of 50 clean answers were kept, so the rule did not over-refuse.

A planted set written by the project: known shapes, not an unbiased rate. The judge's own accuracy is not yet measured.

**Say:** A checker you have not tested is just a claim, so we planted defects. Fake quotes and wrong citations were caught every time. Invented claims nearly always. But a negated claim, zero out of fifty. A word-overlap rule cannot see the word not. That is why claim checking needs a model judge, and in the live run the judge removed ten claims that a real quote did not support. These defects were written by the project, so they show known shapes, not a general rate.


## Slide 32. What this does and does not show

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

**Say:** To conclude. The guarantees hold by construction, and the bound follows from the preconditions. The empirical picture is more modest: no retrieval gain shown, and no learning outcome, because no user study has run. The point to keep: the components an interface can honestly offer are those whose preconditions retrieval can satisfy.


## Slide 33. Selected references

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


## Slide 34. Thank you

MCAIT 2026

Thank you

Questions are welcome.

Fakhrul Azim Bin Ahmed Mardzukie
fakhrul_22012087@utp.edu.my
github.com/Azimlearning/Arcana

3–5 NOVEMBER 2026  ·  TAIBAH UNIVERSITY  ·  MADINAH

**Say:** Thank you. The code and protocol are public, and I am happy to take questions.


## Slide 35. Backup slides, for questions

Rank fusion: the full top 10 for the worked example
Admission by question: which components each question could support
The wire contract, and how a component is added
Cost and latency
The real graph and a comparison grid
Safeguards, and what each contains

**Say:** Backup only. Use these if a question calls for them.


## Slide 36. Rank fusion: the full top 10

After the paper

| # | Passage | Dense | Sparse | Graph | RRF | Gold | In flat top 10 |
|---|---|---|---|---|---|---|---|
| 1 | RAG for Knowledge-Intensive NLP, p7 | - | 5 | 3 | 0.03126 | yes | yes |
| 2 | RAG Survey, p9 | 6 | - | 7 | 0.03008 | yes | no |
| 3 | RAG Survey, p2 | - | - | 1 | 0.01639 | no | no |
| 4 | LightRAG, p5 | - | 1 | - | 0.01639 | no | yes |
| 5 | Precise Zero-Shot Dense Retrieval, p1 | 1 | - | - | 0.01639 | no | yes |
| 6 | RAG Survey, p3 | - | - | 2 | 0.01613 | no | no |
| 7 | RAG Survey, p9 | 2 | - | - | 0.01613 | yes | yes |
| 8 | From Local to Global, p7 | - | 2 | - | 0.01613 | no | yes |
| 9 | From Local to Global, p7 | - | 3 | - | 0.01587 | no | yes |
| 10 | Precise Zero-Shot Dense Retrieval, p8 | 3 | - | - | 0.01587 | no | yes |

Question q-cross-06, k = 60. Scores recomputed from stored rankings; ties keep the stored order.

**Say:** Backup. The full fused list for the worked question.


## Slide 37. Admission by question

After the paper

*[Image: Admission heat map]*

Dark = admitted. Availability, not quality. The worked example q-cross-06 has no graph view here: none of the edges returned by the Graph agent had a quote naming both ends.

**Say:** Backup. Each question and which graph components its evidence could support.


## Slide 38. The wire contract

After the paper

export interface ComparisonGrid {
type: "ComparisonGrid";
id: string;
meta: BlockMeta;
data: ComparisonGridData;
}
export type UIBlock =
| CitedSummary
| SourceList
| GraphView
| ComparisonGrid
| ...

Adding a component is three steps

1

Add the schema variant, and regenerate the server models

2

Implement the component, with its four states

3

Add one line to the registry

A payload change not reflected on both sides is a compile error. Generated models are strict and forbid unknown fields, so they fail closed.

From the shared schema package. Four states: empty, loading, partial, error.

**Say:** Backup. The block type as declared in the shared schema, and the three steps to add a component.


## Slide 39. Cost and latency

After the paper

US$5.81

to ingest 16 papers, 1,570 passages

US$0.0037

per passage: extraction plus embedding

15 of 1,570

passages failed extraction (0.95%)

US$0.017

mean per question, real model

US$0.045

mean per writing turn

481 ms

mean hybrid retrieval, against 296 ms flat

One ingestion, one live run, original 19 questions for latency. Embedding price is an assumption until reconciled with the provider.

**Say:** Backup. What it costs to build and run.


## Slide 40. What retrieval structure makes possible

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

**Say:** Backup. Part of the real graph, and a comparison grid filled from it.


## Slide 41. The model composes the interface. It does not write it.

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

**Say:** Backup. The safeguards and the failure each contains.


---

Spoken length: 1900 words, about 14.6 minutes at 130 words a minute.


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
