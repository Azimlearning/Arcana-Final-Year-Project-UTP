import { useState } from "react";

const AGENTS = {
  // TIER 1: ORCHESTRATION
  orchestrator: { name: "Orchestrator", tier: 1, icon: "🧠", cat: "Orchestration",
    desc: "Routes intent, sequences agents, assembles responses. The central nervous system.",
    tools: ["route_to_agent(agent, query)", "sequence_agents(chain[])", "assemble_response(outputs[])", "get_conversation_history()", "get_user_context()"],
    invokes: "All agents", src: "MetaGPT, AnythingLLM Intelligent Tool Selection" },

  // TIER 2: CORE INTELLIGENCE
  research: { name: "Research Agent", tier: 2, icon: "🔬", cat: "Core Intelligence",
    desc: "Multi-doc synthesis with cross-source citations. Primary workhorse for academic queries.",
    tools: ["hybrid_retrieve(query, top_k)", "graph_expand(entity, hops)", "cross_document_compare(concept, docs[])", "cite_sources(chunks[])", "detect_contradictions(topic)", "find_research_gaps(topic)", "summarise_with_grounding(chunks[], query)"],
    invokes: "Graph, Fact Checker", src: "LightRAG dual-level retrieval, HippoRAG PageRank" },

  learning: { name: "Learning Agent", tier: 2, icon: "📚", cat: "Core Intelligence",
    desc: "Study material generation powered by evidence-based learning science.",
    tools: ["generate_flashcards(concepts[], style)", "generate_quiz(topic, difficulty, n)", "feynman_explain(concept)", "cornell_notes(doc_id)", "assess_knowledge_gap(history)", "schedule_spaced_review(cards[])", "generate_blurting_prompt(topic)", "create_interleaving_set(topics[])"],
    invokes: "Graph, Research", src: "Spaceforge FSRS/SM-2, Cognitive science research" },

  writing: { name: "Writing Agent", tier: 2, icon: "✍️", cat: "Core Intelligence",
    desc: "Drafts structured documents grounded in the knowledge base.",
    tools: ["draft_section(title, context)", "generate_outline(topic)", "build_literature_review(topic)", "check_consistency(draft, graph)", "generate_annotated_bibliography()", "literature_matrix(papers[], dims[])"],
    invokes: "Research, Graph, Fact Checker", src: "GPT-Newspaper pipeline, AnythingLLM Doc Gen" },

  graph: { name: "Graph Agent", tier: 2, icon: "🕸️", cat: "Core Intelligence",
    desc: "Graph traversal, community detection, relationship surfacing.",
    tools: ["graph_expand(entity, hops)", "find_shortest_path(a, b)", "detect_communities(algo)", "find_bridge_concepts()", "pagerank_concepts()", "detect_entity_contradictions()", "subgraph_extract(topic)"],
    invokes: "None", src: "obra/knowledge-graph Louvain+PageRank, Microsoft GraphRAG" },

  // TIER 3: OUTPUT GENERATION
  document: { name: "Document Agent", tier: 3, icon: "📄", cat: "Output Generation",
    desc: "Generates downloadable artifacts — PDF, DOCX, PPTX, Obsidian vault exports.",
    tools: ["generate_pdf_report(sections[])", "generate_slide_deck(outline)", "export_literature_matrix(format)", "export_to_obsidian(graph)", "generate_docx(sections[])"],
    invokes: "Writing, Research", src: "NotebookLM Reports/Slides, AnythingLLM Save Files" },

  audio: { name: "Audio Agent", tier: 3, icon: "🎙️", cat: "Output Generation",
    desc: "Audio summaries, podcast-style overviews, spoken study materials.",
    tools: ["generate_audio_summary(topic)", "generate_podcast_script(style)", "text_to_speech(text, voice)", "generate_audio_flashcards(cards[])"],
    invokes: "Research, Learning", src: "NotebookLM Audio Overview (most viral feature)" },

  visual: { name: "Visual Agent", tier: 3, icon: "📊", cat: "Output Generation",
    desc: "Charts, concept maps, knowledge graph visualisations, timelines.",
    tools: ["render_concept_map(entities[])", "render_comparison_chart(items[])", "render_timeline(events[])", "render_data_table(data[])", "render_knowledge_graph_view(subgraph)", "render_infographic(topic)"],
    invokes: "Graph, Research", src: "LightRAG WebUI, Obsidian Graph View" },

  // TIER 4: QUALITY & META
  factchecker: { name: "Fact Checker", tier: 4, icon: "✅", cat: "Quality & Meta",
    desc: "Verifies claims against KB, flags hallucinations and unsupported statements.",
    tools: ["verify_claim(claim)", "check_citation_accuracy(text, sources[])", "flag_hallucination(text, context)", "cross_reference_sources(claim)"],
    invokes: "Graph, Research", src: "VERA AI 94% citation accuracy policy" },

  ui: { name: "UI Agent", tier: 4, icon: "🎨", cat: "Quality & Meta",
    desc: "GenUI layer — selects React components based on intent + mode. A2UI principles.",
    tools: ["select_output_components(intent, data)", "determine_layout(mode)", "get_user_preferences()", "adapt_complexity_level(profile)", "stream_component(type, data)"],
    invokes: "None", src: "Google A2UI, Vercel AI SDK streamUI" },

  annotation: { name: "Annotation Agent", tier: 4, icon: "📝", cat: "Quality & Meta",
    desc: "Ingests user highlights and notes back into the knowledge graph.",
    tools: ["add_user_annotation(text, doc_id)", "enrich_graph_node(entity)", "link_user_note_to_entity(note)", "capture_highlight(selection)", "import_obsidian_vault(path)"],
    invokes: "Graph", src: "ObsidianGraphRAG wikilink preservation" },

  // === NEW 20 AGENTS ===

  // TIER 2 ADDITIONS
  socratic: { name: "Socratic Tutor", tier: 2, icon: "🏛️", cat: "Core Intelligence",
    desc: "Never gives direct answers. Uses Socratic questioning to guide students to discover answers themselves. Tracks reasoning chains.",
    tools: ["ask_probing_question(topic, depth)", "evaluate_reasoning(student_answer)", "generate_hint(concept, difficulty)", "track_reasoning_chain(session)", "bloom_taxonomy_assess(response)"],
    invokes: "Graph, Learning", src: "Khanmigo, OpenAI Study Mode, SocraticLLM (CIKM 2024)" },

  debate: { name: "Debate Agent", tier: 2, icon: "⚔️", cat: "Core Intelligence",
    desc: "Simulates academic debate. Takes opposing position on user's thesis to strengthen argumentation. Devil's advocate mode.",
    tools: ["generate_counterargument(thesis)", "find_opposing_evidence(claim)", "steelman_position(argument)", "evaluate_argument_strength(text)", "simulate_peer_review(paper)"],
    invokes: "Research, Fact Checker", src: "DeepDebater multi-agent system, ACL 2025 SoDa" },

  discovery: { name: "Discovery Agent", tier: 2, icon: "🔭", cat: "Core Intelligence",
    desc: "Proactively surfaces unexpected connections and serendipitous insights from the knowledge graph that the user hasn't asked about.",
    tools: ["find_surprising_connections(graph)", "detect_cross_domain_links()", "generate_insight_cards()", "surface_underexplored_areas(graph)", "weekly_discovery_digest()"],
    invokes: "Graph", src: "Obsidian RAG 'insight generation' feature, Research Rabbit" },

  methodology: { name: "Methodology Agent", tier: 2, icon: "🧪", cat: "Core Intelligence",
    desc: "Helps design research methodology — sample size, variables, frameworks, evaluation criteria.",
    tools: ["suggest_methodology(research_question)", "calculate_sample_size(params)", "design_evaluation_framework(objectives)", "compare_methodologies(options[])", "generate_research_design(type)"],
    invokes: "Research", src: "Paperguide systematic review, academic methodology guides" },

  // TIER 3 ADDITIONS
  citation: { name: "Citation Agent", tier: 3, icon: "📎", cat: "Output Generation",
    desc: "Formats citations in APA/MLA/Chicago/IEEE. Auto-generates bibliographies. BibTeX/RIS export. Zotero integration.",
    tools: ["format_citation(source, style)", "generate_bibliography(docs[], style)", "export_bibtex(docs[])", "export_ris(docs[])", "convert_citation_style(from, to)", "validate_citations(text)", "suggest_missing_citations(text)"],
    invokes: "Research", src: "Grammarly Citation Finder, Scribbr, Zotero integration ecosystem" },

  translator: { name: "Translation Agent", tier: 3, icon: "🌍", cat: "Output Generation",
    desc: "Translates content across 50+ languages while preserving academic terminology and citation formatting.",
    tools: ["translate_text(text, from, to)", "translate_document(doc_id, target)", "translate_abstract(text, languages[])", "preserve_technical_terms(text, domain)", "bilingual_summary(doc_id, lang)"],
    invokes: "Writing", src: "NotebookLM 50+ language Audio Overviews, Paperpal 50+ lang" },

  paraphrase: { name: "Paraphrase Agent", tier: 3, icon: "🔄", cat: "Output Generation",
    desc: "Rewrites content at different complexity levels — simplify for undergrads, complexify for journals, maintain academic tone.",
    tools: ["simplify_text(text, level)", "academify_text(text)", "change_reading_level(text, target)", "paraphrase_paragraph(text, style)", "reduce_word_count(text, target)"],
    invokes: "Writing, Fact Checker", src: "QuillBot, Paperpal contextual rewriting" },

  presentation: { name: "Presentation Agent", tier: 3, icon: "🎬", cat: "Output Generation",
    desc: "Generates video overviews and animated explainers from knowledge base content.",
    tools: ["generate_video_script(topic)", "create_animated_explainer(concept)", "generate_video_overview(docs[])", "create_visual_abstract(paper)"],
    invokes: "Research, Visual, Audio", src: "NotebookLM Video Overview, Nano Banana Pro" },

  export: { name: "Export Agent", tier: 3, icon: "📦", cat: "Output Generation",
    desc: "Handles all export formats and integrations — Google Drive sync, bulk import/export, folder watching.",
    tools: ["export_notebook(format)", "sync_google_drive(folder_id)", "bulk_import_urls(urls[])", "watch_folder(path)", "export_to_notion(workspace)", "export_to_anki(cards[])"],
    invokes: "Document", src: "NotebookLM missing features: bulk import, Drive sync, export options" },

  // TIER 4 ADDITIONS
  plagiarism: { name: "Plagiarism Agent", tier: 4, icon: "🔍", cat: "Quality & Meta",
    desc: "Checks writing for originality. Detects accidental plagiarism, suggests citations for unattributed claims, AI content detection.",
    tools: ["check_plagiarism(text)", "detect_ai_content(text)", "suggest_citations_needed(text)", "calculate_originality_score(text)", "flag_close_paraphrasing(text, sources[])"],
    invokes: "Research, Citation", src: "Grammarly Plagiarism Checker, Scribbr, Copyleaks" },

  grammar: { name: "Grammar & Style Agent", tier: 4, icon: "✏️", cat: "Quality & Meta",
    desc: "Academic writing polish — grammar, tone, clarity, readability scoring, journal submission readiness.",
    tools: ["check_grammar(text)", "assess_readability(text)", "improve_academic_tone(text)", "check_journal_readiness(text, journal)", "highlight_passive_voice(text)", "suggest_stronger_verbs(text)"],
    invokes: "Writing", src: "Paperpal 30+ journal readiness checks, Grammarly academic mode" },

  planner: { name: "Study Planner Agent", tier: 4, icon: "📅", cat: "Quality & Meta",
    desc: "Creates personalised study schedules. Pomodoro sessions. Deadline tracking. Workload forecasting based on content difficulty.",
    tools: ["create_study_plan(topics[], deadline)", "schedule_pomodoro_session(topic, duration)", "forecast_workload(content_volume)", "track_deadline(task, date)", "suggest_study_order(topics[], dependencies)", "generate_daily_schedule(date)"],
    invokes: "Learning", src: "Spaceforge Pomodoro + calendar, study-planner GitHub repos" },

  memory: { name: "Memory Agent", tier: 4, icon: "🧩", cat: "Quality & Meta",
    desc: "Persistent user context across sessions. Tracks what user has learned, preferences, interaction patterns. Enables personalisation.",
    tools: ["store_user_context(key, value)", "retrieve_user_history(timeframe)", "track_learning_progress(topic)", "get_interaction_patterns()", "update_user_profile(data)", "forget_context(key)"],
    invokes: "Learning, Graph", src: "Mem0 memory, NotebookLM 'expanding working memory' (Reddit)" },

  ingestion: { name: "Ingestion Agent", tier: 4, icon: "📥", cat: "Quality & Meta",
    desc: "Handles all document processing — PDF/DOCX/URL/YouTube parsing, entity extraction, graph construction, chunking, embedding.",
    tools: ["ingest_pdf(file)", "ingest_docx(file)", "ingest_url(url)", "ingest_youtube(url)", "extract_entities(text)", "build_graph_triples(entities[])", "chunk_and_embed(text)", "ocr_scan(image)"],
    invokes: "Graph", src: "EDC Framework (Paper [7]), AnythingLLM collector pipeline" },

  search: { name: "Web Search Agent", tier: 4, icon: "🌐", cat: "Quality & Meta",
    desc: "Searches external academic databases — Semantic Scholar, arXiv, Google Scholar. Discovers new papers related to user's KB.",
    tools: ["search_semantic_scholar(query)", "search_arxiv(query)", "search_google_scholar(query)", "find_related_papers(doc_id)", "get_citation_network(paper_id)", "monitor_new_papers(topics[])"],
    invokes: "Research, Citation", src: "Elicit, WisPaper Scholar Search, Research Rabbit, Perplexity" },

  collab: { name: "Collaboration Agent", tier: 4, icon: "👥", cat: "Quality & Meta",
    desc: "Enables shared notebooks, real-time co-editing, comment threads, and team knowledge bases.",
    tools: ["create_shared_notebook(users[])", "add_comment_thread(doc_id, text)", "merge_knowledge_bases(kb_ids[])", "track_contributions(user_id)", "notify_team_updates()"],
    invokes: "Annotation", src: "NotebookLM Share feature, Notion team collaboration" },

  template: { name: "Template Agent", tier: 4, icon: "📋", cat: "Quality & Meta",
    desc: "Pre-built research workflow templates — lit review, thesis chapter, lab report, systematic review, case study.",
    tools: ["load_template(type)", "customise_template(template, params)", "suggest_template(intent)", "create_custom_template(structure)", "list_templates()"],
    invokes: "Writing, Document", src: "Paperguide systematic review formatting, academic workflow tools" },

  analytics: { name: "Analytics Agent", tier: 4, icon: "📈", cat: "Quality & Meta",
    desc: "Tracks usage patterns, study effectiveness, retrieval quality metrics. Dashboard for learning progress.",
    tools: ["track_study_session(data)", "calculate_retention_rate(topic)", "measure_retrieval_quality()", "generate_progress_dashboard()", "weekly_analytics_report()", "compare_study_methods(methods[])"],
    invokes: "Memory, Learning", src: "NotebookLM Analytics tab, Spaceforge session tracking" },

  security: { name: "Privacy & Security Agent", tier: 4, icon: "🔒", cat: "Quality & Meta",
    desc: "Manages data privacy, user permissions, encryption, and ensures no sensitive data leaks to external APIs.",
    tools: ["sanitize_before_api_call(text)", "encrypt_user_data(data)", "manage_permissions(user, level)", "audit_data_access_log()", "anonymize_content(text)"],
    invokes: "None", src: "AnythingLLM privacy-first architecture, GDPR compliance" },
};

const TIERS = [
  { id: 1, name: "Orchestration", color: "#FF6B35", desc: "Central routing" },
  { id: 2, name: "Core Intelligence", color: "#4ECDC4", desc: "Thinking & reasoning" },
  { id: 3, name: "Output Generation", color: "#A855F7", desc: "Creating deliverables" },
  { id: 4, name: "Quality & Meta", color: "#EF4444", desc: "Validation & infrastructure" },
];

const TIER_COLORS = { 1: "#FF6B35", 2: "#4ECDC4", 3: "#A855F7", 4: "#EF4444" };

const UI_PANELS = [
  { name: "Sources Panel", width: "20%", desc: "Document list, add sources, search, web/research toggle. Obsidian vault import. Drag-drop upload.", color: "#3B82F6" },
  { name: "Chat Panel", width: "45%", desc: "Main interaction. GenUI components stream here. Cited responses, inline graphs, interactive cards. Mode indicator (Research/Writing/Study).", color: "#10B981" },
  { name: "Studio Panel", width: "35%", desc: "Output tools grid (like NotebookLM but expanded). Generated notes list. Quick actions. Agent status indicators.", color: "#F59E0B" },
];

const COMPONENT_CATALOG = [
  { name: "CitedSummary", agent: "Research", desc: "Multi-source answer with inline citations" },
  { name: "FlashcardDeck", agent: "Learning", desc: "Interactive SR-scheduled flashcards" },
  { name: "QuizCard", agent: "Learning", desc: "MCQ/short answer with scoring" },
  { name: "ConceptMap", agent: "Visual", desc: "Interactive node-edge concept visualisation" },
  { name: "ComparisonTable", agent: "Visual", desc: "Side-by-side paper/concept comparison" },
  { name: "Timeline", agent: "Visual", desc: "Chronological concept evolution" },
  { name: "LiteratureMatrix", agent: "Writing", desc: "Multi-paper comparison grid" },
  { name: "ContradictionAlert", agent: "Fact Checker", desc: "Sources that disagree" },
  { name: "KnowledgeGraphView", agent: "Graph", desc: "Obsidian-style interactive graph" },
  { name: "CornellNotes", agent: "Learning", desc: "3-column structured notes" },
  { name: "FeynmanExplainer", agent: "Learning", desc: "Teach-it-simply output" },
  { name: "BlurtingPrompt", agent: "Learning", desc: "Topic + blank, then compare vs KB" },
  { name: "AudioPlayer", agent: "Audio", desc: "Podcast-style audio summary" },
  { name: "SlidePreview", agent: "Document", desc: "Generated slide deck preview" },
  { name: "GapAnalysis", agent: "Research", desc: "What sources don't cover" },
  { name: "SocraticDialog", agent: "Socratic", desc: "Question-guided learning interface" },
  { name: "DebateView", agent: "Debate", desc: "Pro/con argument cards" },
  { name: "InsightCard", agent: "Discovery", desc: "Surprise connection notification" },
  { name: "CitationPreview", agent: "Citation", desc: "Formatted reference with style picker" },
  { name: "StudyPlanCalendar", agent: "Planner", desc: "Visual study schedule with Pomodoro" },
  { name: "ProgressDashboard", agent: "Analytics", desc: "Learning analytics visualisation" },
  { name: "PlagiarismReport", agent: "Plagiarism", desc: "Originality score with highlights" },
  { name: "MethodologyBuilder", agent: "Methodology", desc: "Research design wizard" },
  { name: "PaperDiscovery", agent: "Search", desc: "Related papers with citation graph" },
];

export default function ArcanaV3() {
  const [selected, setSelected] = useState(null);
  const [tab, setTab] = useState("agents");
  const [tierFilter, setTierFilter] = useState(null);

  const agentList = Object.entries(AGENTS);
  const filtered = tierFilter ? agentList.filter(([,a]) => a.tier === tierFilter) : agentList;
  const agent = selected ? AGENTS[selected] : null;
  const totalTools = agentList.reduce((s, [,a]) => s + a.tools.length, 0);

  return (
    <div style={{ fontFamily: "'IBM Plex Sans', system-ui", background: "#08080d", color: "#d8d8e0", minHeight: "100vh", padding: 20 }}>
      <style>{`@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400&display=swap');
        * { box-sizing: border-box; } ::-webkit-scrollbar { width: 5px; } ::-webkit-scrollbar-thumb { background: #333; border-radius: 3px; }
        button { font-family: inherit; } .agent-btn:hover { transform: translateY(-1px); }`}</style>

      {/* Header */}
      <div style={{ textAlign: "center", marginBottom: 24 }}>
        <div style={{ fontSize: 10, letterSpacing: 5, color: "#555", marginBottom: 4 }}>SYSTEM ARCHITECTURE v3.0</div>
        <h1 style={{ fontSize: 32, fontWeight: 700, margin: 0, background: "linear-gradient(135deg, #FF6B35, #4ECDC4, #A855F7, #EF4444)", WebkitBackgroundClip: "text", WebkitTextFillColor: "transparent" }}>
          Arcana
        </h1>
        <p style={{ fontSize: 12, color: "#666", margin: "4px 0 0" }}>
          {agentList.length} Agents · {totalTools} Tool Calls · {COMPONENT_CATALOG.length} GenUI Components · GraphRAG · Composable Multi-Agent
        </p>
      </div>

      {/* Tabs */}
      <div style={{ display: "flex", gap: 6, justifyContent: "center", marginBottom: 20 }}>
        {[{id:"agents",l:"All Agents"},{id:"ui",l:"UI Layout"},{id:"genui",l:"Component Catalog"},{id:"stats",l:"Stats"}].map(t => (
          <button key={t.id} onClick={() => { setTab(t.id); setSelected(null); setTierFilter(null); }}
            style={{ padding: "5px 14px", borderRadius: 5, border: `1px solid ${tab===t.id?"#4ECDC4":"#1e1e28"}`, background: tab===t.id?"rgba(78,205,196,0.08)":"transparent", color: tab===t.id?"#4ECDC4":"#777", fontSize: 11, fontWeight: 500, cursor: "pointer" }}>
            {t.l}
          </button>
        ))}
      </div>

      <div style={{ display: "flex", gap: 16, maxWidth: 1300, margin: "0 auto" }}>
        {/* LEFT */}
        <div style={{ flex: 1, minWidth: 0 }}>

          {tab === "agents" && (<>
            {/* Tier filters */}
            <div style={{ display: "flex", gap: 6, marginBottom: 14, flexWrap: "wrap" }}>
              <button onClick={() => setTierFilter(null)} style={{ padding: "3px 10px", borderRadius: 4, fontSize: 10, border: `1px solid ${!tierFilter?"#fff":"#1e1e28"}`, background: !tierFilter?"rgba(255,255,255,0.06)":"transparent", color: !tierFilter?"#fff":"#666", cursor: "pointer" }}>All ({agentList.length})</button>
              {TIERS.map(t => {
                const count = agentList.filter(([,a]) => a.tier === t.id).length;
                return (
                  <button key={t.id} onClick={() => setTierFilter(tierFilter===t.id?null:t.id)} style={{ padding: "3px 10px", borderRadius: 4, fontSize: 10, border: `1px solid ${tierFilter===t.id?t.color:"#1e1e28"}`, background: tierFilter===t.id?`${t.color}15`:"transparent", color: tierFilter===t.id?t.color:"#666", cursor: "pointer" }}>
                    {t.name} ({count})
                  </button>
                );
              })}
            </div>

            {/* Agent grid */}
            <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(155px, 1fr))", gap: 6 }}>
              {filtered.map(([id, a]) => {
                const c = TIER_COLORS[a.tier];
                const isSel = selected === id;
                return (
                  <button key={id} className="agent-btn" onClick={() => setSelected(isSel?null:id)}
                    style={{ padding: "10px 8px", borderRadius: 8, border: `1px solid ${isSel?c:"#161620"}`, background: isSel?`${c}10`:"#0e0e16", cursor: "pointer", textAlign: "left", transition: "all 0.15s" }}>
                    <div style={{ fontSize: 18 }}>{a.icon}</div>
                    <div style={{ fontSize: 11, fontWeight: 600, color: "#ddd", marginTop: 4 }}>{a.name}</div>
                    <div style={{ fontSize: 9, color: c, marginTop: 2 }}>{a.tools.length} tools</div>
                  </button>
                );
              })}
            </div>
          </>)}

          {tab === "ui" && (
            <div>
              <div style={{ fontSize: 11, fontWeight: 600, color: "#888", letterSpacing: 2, marginBottom: 12 }}>NOTEBOOKLM-INSPIRED LAYOUT (ADAPTED FOR ARCANA)</div>
              {/* 3-panel mockup */}
              <div style={{ display: "flex", gap: 2, height: 400, borderRadius: 10, overflow: "hidden", border: "1px solid #1e1e28" }}>
                {UI_PANELS.map(p => (
                  <div key={p.name} style={{ width: p.width, background: "#0c0c14", padding: 14, borderRight: "1px solid #1a1a24", display: "flex", flexDirection: "column" }}>
                    <div style={{ fontSize: 11, fontWeight: 700, color: p.color, marginBottom: 8 }}>{p.name}</div>
                    <div style={{ fontSize: 10, color: "#777", lineHeight: 1.6, flex: 1 }}>{p.desc}</div>
                    {p.name === "Studio Panel" && (
                      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr 1fr", gap: 4, marginTop: 8 }}>
                        {["Audio Overview","Slide Deck","Video Overview","Mind Map","Reports","Flashcards","Quiz","Infographic","Data Table","Socratic Mode","Debate Mode","Study Plan"].map(o => (
                          <div key={o} style={{ padding: "6px 4px", borderRadius: 4, background: "#161620", fontSize: 8, color: "#999", textAlign: "center" }}>{o}</div>
                        ))}
                      </div>
                    )}
                    {p.name === "Sources Panel" && (
                      <div style={{ marginTop: 8 }}>
                        {["Research Papers.pdf","Concept Doc.docx","arXiv: GraphRAG","YouTube: LangGraph","Obsidian Vault"].map(s => (
                          <div key={s} style={{ padding: "4px 6px", borderRadius: 3, fontSize: 9, color: "#666", borderBottom: "1px solid #161620" }}>{s}</div>
                        ))}
                      </div>
                    )}
                    {p.name === "Chat Panel" && (
                      <div style={{ marginTop: 8 }}>
                        <div style={{ display: "flex", gap: 4, marginBottom: 8 }}>
                          {["Research","Writing","Study"].map(m => (
                            <span key={m} style={{ padding: "2px 8px", borderRadius: 3, fontSize: 9, background: m==="Research"?"rgba(78,205,196,0.15)":"#161620", color: m==="Research"?"#4ECDC4":"#555" }}>{m}</span>
                          ))}
                        </div>
                        <div style={{ padding: 8, borderRadius: 6, background: "#161620", fontSize: 9, color: "#888" }}>
                          GenUI components stream here: CitedSummary, FlashcardDeck, KnowledgeGraphView...
                        </div>
                      </div>
                    )}
                  </div>
                ))}
              </div>
              <div style={{ marginTop: 16, padding: 14, borderRadius: 8, border: "1px solid #1e1e28", background: "#0c0c14" }}>
                <div style={{ fontSize: 11, fontWeight: 600, color: "#FF6B35", marginBottom: 8 }}>Key Differences from NotebookLM</div>
                <div style={{ fontSize: 10, color: "#888", lineHeight: 1.8 }}>
                  <strong style={{ color: "#ccc" }}>Mode Switching</strong> — Research/Writing/Study modes change available tools + agent priority + UI density<br/>
                  <strong style={{ color: "#ccc" }}>GenUI Streaming</strong> — Components render dynamically based on agent output, not static buttons<br/>
                  <strong style={{ color: "#ccc" }}>Knowledge Graph</strong> — Interactive Obsidian-style graph view embedded in Sources panel<br/>
                  <strong style={{ color: "#ccc" }}>12 Output Types</strong> — vs NotebookLM's 9. Added: Socratic Mode, Debate Mode, Study Plan<br/>
                  <strong style={{ color: "#ccc" }}>Studio Expansion</strong> — Notes list replaced with generated artifacts list + analytics preview<br/>
                  <strong style={{ color: "#ccc" }}>Drive Sync</strong> — Folder watching + auto-refresh (top NotebookLM complaint solved)<br/>
                  <strong style={{ color: "#ccc" }}>Bulk Import</strong> — URLs, YouTube playlists, Obsidian vaults, Zotero libraries
                </div>
              </div>
            </div>
          )}

          {tab === "genui" && (
            <div>
              <div style={{ fontSize: 10, color: "#666", marginBottom: 12 }}>Agent outputs map to pre-built React components. UI Agent selects + streams them via Vercel AI SDK.</div>
              <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 6 }}>
                {COMPONENT_CATALOG.map(c => (
                  <div key={c.name} style={{ padding: 10, borderRadius: 6, border: "1px solid #161620", background: "#0c0c14" }}>
                    <div style={{ fontFamily: "'IBM Plex Mono'", fontSize: 10, color: "#A855F7" }}>{"<"}{c.name}{" />"}</div>
                    <div style={{ fontSize: 9, color: "#888", marginTop: 3 }}>{c.desc}</div>
                    <div style={{ fontSize: 8, color: "#555", marginTop: 2 }}>→ {c.agent}</div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {tab === "stats" && (
            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 10 }}>
              {[
                { label: "Total Agents", value: agentList.length, color: "#FF6B35" },
                { label: "Total Tool Calls", value: totalTools, color: "#4ECDC4" },
                { label: "GenUI Components", value: COMPONENT_CATALOG.length, color: "#A855F7" },
                { label: "Research Papers", value: 13, color: "#EF4444" },
                { label: "Open Source Repos Referenced", value: 8, color: "#F59E0B" },
                { label: "Study Methods Supported", value: 8, color: "#10B981" },
              ].map(s => (
                <div key={s.label} style={{ padding: 16, borderRadius: 8, border: "1px solid #161620", background: "#0c0c14", textAlign: "center" }}>
                  <div style={{ fontSize: 28, fontWeight: 700, color: s.color }}>{s.value}</div>
                  <div style={{ fontSize: 10, color: "#666", marginTop: 4 }}>{s.label}</div>
                </div>
              ))}
              <div style={{ gridColumn: "1/3", padding: 14, borderRadius: 8, border: "1px solid #161620", background: "#0c0c14" }}>
                <div style={{ fontSize: 11, fontWeight: 600, color: "#4ECDC4", marginBottom: 8 }}>Study Methods Integrated</div>
                <div style={{ display: "flex", flexWrap: "wrap", gap: 4 }}>
                  {["Active Recall","Spaced Repetition (FSRS/SM-2)","Feynman Technique","Cornell Notes","Blurting Method","Interleaving","Socratic Questioning","Pomodoro Technique"].map(m => (
                    <span key={m} style={{ padding: "3px 8px", borderRadius: 4, fontSize: 9, background: "rgba(78,205,196,0.08)", border: "1px solid rgba(78,205,196,0.2)", color: "#4ECDC4" }}>{m}</span>
                  ))}
                </div>
              </div>
            </div>
          )}
        </div>

        {/* RIGHT: Detail Panel */}
        <div style={{ width: 340, flexShrink: 0, position: "sticky", top: 20, alignSelf: "flex-start", maxHeight: "calc(100vh - 40px)", overflowY: "auto" }}>
          {agent ? (
            <div style={{ borderRadius: 10, border: `1px solid ${TIER_COLORS[agent.tier]}25`, background: "#0c0c14", padding: 16 }}>
              <div style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 10 }}>
                <span style={{ fontSize: 24 }}>{agent.icon}</span>
                <div>
                  <div style={{ fontSize: 14, fontWeight: 700 }}>{agent.name}</div>
                  <div style={{ fontSize: 9, color: TIER_COLORS[agent.tier], fontWeight: 600, letterSpacing: 1, textTransform: "uppercase" }}>{agent.cat}</div>
                </div>
              </div>
              <p style={{ fontSize: 11, color: "#999", lineHeight: 1.6, marginBottom: 14 }}>{agent.desc}</p>

              <div style={{ fontSize: 9, fontWeight: 600, letterSpacing: 2, color: "#555", marginBottom: 6 }}>TOOLS ({agent.tools.length})</div>
              {agent.tools.map((t, i) => (
                <div key={i} style={{ padding: "5px 7px", marginBottom: 3, borderRadius: 4, background: "#0a0a12", fontFamily: "'IBM Plex Mono'", fontSize: 9.5, color: "#4ECDC4", wordBreak: "break-all" }}>
                  {t}
                </div>
              ))}

              <div style={{ marginTop: 12, fontSize: 9, fontWeight: 600, letterSpacing: 2, color: "#555", marginBottom: 6 }}>INVOKES</div>
              <div style={{ fontSize: 10, color: "#888" }}>{agent.invokes}</div>

              <div style={{ marginTop: 12, fontSize: 9, fontWeight: 600, letterSpacing: 2, color: "#555", marginBottom: 6 }}>INSPIRED BY</div>
              <div style={{ padding: 8, borderRadius: 5, background: "rgba(255,107,53,0.04)", border: "1px solid rgba(255,107,53,0.1)", fontSize: 10, color: "#FF6B35", lineHeight: 1.5 }}>
                {agent.src}
              </div>
            </div>
          ) : (
            <div style={{ borderRadius: 10, border: "1px dashed #1e1e28", padding: 30, textAlign: "center" }}>
              <div style={{ fontSize: 28, opacity: 0.2, marginBottom: 8 }}>👆</div>
              <div style={{ fontSize: 11, color: "#444" }}>
                {tab === "agents" ? "Click an agent to explore" : "Switch to Agents tab"}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
