# MCAIT 2026 presentation plan

Updated 1 November 2026. Two decks to choose between: `179.pptx` (25 slides, 2 videos, about 16 minutes) and `179-v2.pptx` (34 slides plus 7 backup, 8 videos, about 14 minutes of speech at a faster pace). `Slide-Content.md` and `Slide-Content-v2.md` are generated from them. Whichever is chosen must be uploaded named `179.pptx`.

## Framing

- The paper is its own work and leads the talk. Arcana is the paper in practice, and is only ever called Arcana.
- Results carry one of two tags: `In the paper` or `After the paper`, so nothing appears to contradict the proceedings.
- VERA AI and market products are the only comparisons. Both compare designs or public descriptions, never results.
- Adaptive UI is presented as the paper's expressiveness argument. Synapse appears only as the generated-component level, credited to Team EduNova and not compared with Arcana.
- Main message: the graph has not been shown to rank passages better, but it is what lets an interface honestly show relations between sources.

## Running order

| Part | Slides | Content |
|---|---|---|
| Opening | 1-2 | Title, the claim, outline |
| Problem | 3-4 | Relational questions get prose; flat retrieval cannot represent a relation |
| Related work | 5-6 | Four literatures and the gap; market products from public descriptions |
| This paper | 7-8 | Contributions; 29-second animated explainer |
| Method | 9-13 | Three regimes, architecture, composition and safeguards, adaptive interface, worked request |
| Central claim | 14 | The formal bound |
| Evaluation | 15 | Committed protocol and the null pilot |
| Practice | 16-19 | VERA to Arcana; 36-second demo; real graph and comparison grid; generated, verified labs |
| New findings | 20-22 | Retrieval gain not shown; 2 components against 5; grounding held, relevance not shown |
| Close | 23-25 | What is and is not shown, references, thank you |

The organisers' email of 2 Nov gives each talk 20 minutes: 15 for the presentation and 5 for questions, with the camera on throughout. Speaker notes for `179.pptx` come to 2,093 words, about 16 minutes at 130 words a minute. `179-v2.pptx` comes to about 14 minutes of speech.

## Visuals

| Asset | What it is | Where |
|---|---|---|
| `build/assets/arcana-explainer.mp4` | Animated explainer, silent, labelled as an illustration of the paper's worked example | `179.pptx` slide 8 |
| `build/assets/video-adaptive.mp4` | Layouts rearranging per question | `179.pptx` slide 12, `179-v2.pptx` slide 16 |
| `build/assets/arcana-demo.mp4` | Real screens and a recording, silent, so you can speak over it | `179.pptx` slide 17 |
| `build/assets/video-ingest.mp4`, `video-traverse.mp4`, `video-fuse.mp4` | Real sentences, route and scores for question q-cross-06 | `179-v2.pptx` slides 11, 13, 14 |
| `build/assets/video-compose.mp4`, `video-bound.mp4` | Cut from the explainer | `179-v2.pptx` slides 15, 20 |
| `build/assets/video-demo-questions.mp4`, `video-demo-tools.mp4` | The demo split in two | `179-v2.pptx` slides 23, 24 |
| `build/assets/knowledge-graph.png` | Drawn from the real graph of 16 papers | `179.pptx` slide 18 |
| `build/assets/visual-*.png` | Five stills from the explainer, spare for other uses | Not placed |

To change anything, edit `build/build_deck.py` or `build/build_deck_v2.py` (which builds on `179.pptx`) and run it, then `build/export_content.py <deck>`.

## Before presenting

1. Read `Slide-Content.md` and change anything that does not sound like you.
2. Choose a deck, open it in PowerPoint and play every video.
3. Do one timed run-through out loud.
4. Upload the chosen deck, named `179.pptx`, to the organisers' SharePoint folder and confirm it appears.
5. Practise the questions at the end of `Slide-Content.md`.
