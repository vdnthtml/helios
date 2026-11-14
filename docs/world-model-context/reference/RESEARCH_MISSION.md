# Complete specialist research mission

Source: `context/sources/conversation-2026-11-14.txt`, lines 5670–7589.
Status: preserved conversation extract; assistant-authored proposals are not independently verified findings or automatically accepted decisions. Original dates and claims are preserved as history.

---

now what i want you to do is - get all the relevant infomration you have around our topic and build hand offs to other ais, and also at the same time build a parallel infomation thingy which contains what are the architectural needs, dont worry about it like dont think about what exists for you, the other ai is a specialist into finding inforation on such topics and we will let it rip, it will get the relevant githubs - just tell it every single crook and penny and it can find everyhting legit everything


hence this is what we need - think of handoff and that - make these two things for me
Information World Model — AI Research & Architecture Handoff Pack
These are two documents with different jobs.

Document 1 — Specialist AI Research Handoff: Give this to an AI with strong web, GitHub, technical-paper, and code-repository research capabilities. Its job is to discover everything relevant, compare implementations, uncover missing architectural concepts, and recommend technologies based on evidence.

Document 2 — Complete Architecture Requirements Register: This defines what we're trying to build, every major capability, how the components should interact, what needs to be tested, and which decisions are still open.

Use Document 2 as the source of requirements. Document 1 tells the research AI what to do with those requirements. Neither document should be treated as permission for an AI to silently redesign the company.

Document 1 — Specialist AI Research Handoff
SPECIALIST RESEARCH AGENT — MASTER HANDOFF
Information World Model: Technical Discovery, Prior Art, GitHub Research & Architecture Evaluation
Mission: Comprehensive technical and scientific research.

Status: Pre-implementation.

Your role: Act as a senior research engineer, AI systems architect, open-source intelligence researcher, and technical due-diligence specialist.

Primary task: Discover, verify, compare, and evaluate the technologies, algorithms, research papers, repositories, datasets, architectures, and established systems that could help us build the Information World Model described below.

This is not a request for a generic list of AI tools.

We need a rigorous technical investigation that can directly inform architecture and implementation.

1. PROJECT CONTEXT
1.1 What we are building
We are exploring an Information World Model (IWM).

It is intended to represent and continuously update relationships among:

People and their documented activities.

Information, claims, ideas, and narratives.

Companies, institutions, and organizations.

Capital, transactions, supply chains, and economic relationships.

Technologies, products, industries, and communities.

Events, decisions, historical developments, and outcomes.

The mechanisms through which information and decisions influence observable changes.

None of these categories is inherently more important than another.

The goal is to reason across their intersections.

For example:

A researcher publishes an idea. An executive discusses it. A company subsequently invests in a related technology. Other companies expand their operations. Financial and technological developments reshape public discussion.

We want a system that can reconstruct the documented events, investigate possible relationships, identify competing explanations, recognize uncertainties, and explore potential consequences.

We are not assuming that chronological relationships prove causality.

The system should learn from historical outcomes and improve the reliability of its investigations.

1.2 Original motivation
The project began with questions about information influence and AI security:

How do people encounter and interpret information?

How do narratives form, spread, evolve, and disappear?

How can information pathways be reconstructed?

How does information influence organizational decisions?

How do decisions lead to economic changes?

Can historical patterns help predict future developments?

Can an independent information system explain the evidence behind its conclusions?

The project subsequently expanded into economic intelligence, organizational relationships, temporal knowledge graphs, decision science, and agent-based intelligence.

Do not reduce it to only one of these areas.

1.3 The central technical hypothesis
A system combining:

Evidence-native information representation.

Temporal relationship modeling.

Context-sensitive memory segmentation.

Adaptive cross-domain retrieval.

Explicit hypothesis and attribution reasoning.

Human analytical frameworks.

Historical forecasting and feedback.

...may produce better answers and predictions than ordinary RAG, isolated graph databases, or unrestricted LLM reasoning.

This is an untested hypothesis.

Your research must evaluate it critically.

2. WHAT SUCCESS LOOKS LIKE
We want to build an initial prototype capable of:

Ingesting a selected body of heterogeneous real-world information.

Extracting structured entities, claims, events, and relationships.

Organizing information into distinct but connected contexts.

Resolving identities accurately.

Preserving source provenance and temporal history.

Finding relationships across information domains.

Generating and evaluating competing explanations.

Distinguishing documented connections from speculative attribution.

Conducting bounded autonomous investigations.

Replaying historical information states without future-data leakage.

Generating measurable forecasts.

Evaluating those forecasts against actual outcomes.

Learning from errors through controlled update mechanisms.

Presenting findings through a simple messaging-style interface.

Operating at low initial infrastructure cost.

The first version need not process the entire internet.

It should demonstrate the core architecture on a relatively small, interconnected dataset.

The architecture should be expandable without being unnecessarily overengineered.

3. YOUR RESEARCH OPERATING RULES
3.1 Search comprehensively
Search GitHub, GitLab where relevant, research papers, official documentation, academic repositories, public benchmarks, engineering blogs, architectural case studies, and commercial product documentation.

Look for established systems and obscure but technically promising implementations.

Don't stop at the first well-known repository.

Research both mature implementations and relevant experimental work.

3.2 Verify every recommendation
For each repository or technology, establish:

Actual repository URL.

Project purpose.

License and relevant commercial restrictions.

Language and technology stack.

Architecture and core algorithms.

Relevant implemented capabilities.

Important missing capabilities.

Last verifiable development activity.

Maintenance and issue status.

Documentation quality.

Deployment requirements.

Self-hosting support.

Hardware and memory requirements where available.

Known integration difficulties.

Tests and benchmarks.

Evidence supporting performance claims.

Whether it is suitable for local development.

Whether it is suitable for commercial production.

Do not invent repositories, benchmarks, license permissions, or technical capabilities.

If you cannot inspect the code, say so.

If a claim comes only from marketing material, label it accordingly.

A GitHub star count is not evidence of technical suitability.

3.3 Compare rather than collect
We do not need 500 repository names without interpretation.

We need to know:

Which approaches solve similar problems?

Which implementations are strongest?

Which have overlapping functionality?

Which are complementary?

Which can be integrated?

Which would introduce unnecessary complexity?

Which are abandoned or unsuitable?

Which problems remain unsolved?

Separate direct matches from adjacent technologies and purely experimental research.

3.4 Challenge the architecture
You are authorized and expected to identify weaknesses.

If our proposed evidence-capsule architecture is redundant, say so.

If the ontology is unnecessarily complicated, explain why.

If a temporal graph database is a better starting point than PostgreSQL, provide evidence.

If our inference mechanism has no plausible advantage over existing GraphRAG methods, identify the problem.

If a proposed feature is not technically defensible, explain what could replace it.

Do not make silent substitutions. Present every significant proposed change with its rationale and tradeoffs.

3.5 Preserve the project boundaries
Research legitimate public, licensed, or consented information acquisition.

Do not propose covert access to AI conversation histories, unauthorized scraping, undisclosed meeting recording, or sensitive psychological profiling.

The system may investigate observable professional behavior and information networks. It must not assume access to people's private thoughts or treat speculative personal profiles as verified knowledge.

Private enterprise information should remain permission-controlled.

4. RESEARCH WORKSTREAM A — ONTOLOGY AND INFORMATION REPRESENTATION
Investigate how to represent a continuously changing world containing heterogeneous entities, events, claims, and relationships.

Search for:

Knowledge representation systems.

RDF, OWL, SHACL.

Property graphs.

Hypergraphs.

Event-centric knowledge graphs.

Event sourcing.

Temporal knowledge graphs.

Contextual and multilayer graphs.

Typed edges and relational schemas.

Knowledge graph schema evolution.

Ontology versioning.

Semantic data models.

Object-role modeling.

Reified statements.

Named graphs.

Claims and assertions as first-class objects.

Provenance-aware knowledge graphs.

Probabilistic knowledge graphs.

Uncertainty representations.

Knowledge representation for conflicting information.

Event-participant models.

Knowledge graphs with multiple relation qualifiers.

Questions to resolve
What is the most appropriate representation of a relationship involving several entities?

Should events be first-class graph nodes?

How should assertions differ from real-world events?

How should a claim about a relationship differ from the relationship itself?

How should uncertainty be represented?

How can the ontology expand without becoming unmanageable?

Which existing ontologies or standards should be reused?

What structures best support temporal and cross-domain reasoning?

How should information from different domain ontologies be joined?

Required output
Recommend two or three viable foundational ontology approaches.

Include concrete schemas, query examples, tradeoffs, and suitable libraries.

5. WORKSTREAM B — ENTITY RESOLUTION AND IDENTITY
Investigate systems capable of resolving people, organizations, products, and other entities across heterogeneous datasets.

Topics:

Entity resolution.

Record linkage.

Entity linking.

Named-entity recognition.

Cross-document coreference.

Organization matching.

Alias detection.

Multilingual identity resolution.

Knowledge-graph entity alignment.

Deduplication.

Probabilistic identity matching.

Stable canonical identifiers.

Candidate generation.

Match confidence.

Reversible merges.

Identity versioning.

Human review workflows.

Entity resolution with incomplete information.

Investigate relevant open-source tools and algorithms, including probabilistic record linkage and embedding-based entity matching.

Required capabilities
The system must not automatically merge two people because they have the same name.

It should support:

Authoritative external identifiers.

Source-specific identifiers.

Provisional identities.

Ambiguous matches.

Separate identity evidence.

Corrections.

Reversible merges.

Downstream dependency correction.

Research questions
Which methods offer the best accuracy and cost for a heterogeneous, growing information graph?

Should identity resolution be primarily deterministic, statistical, neural, or hybrid?

How can a mistaken merge be reversed without corrupting historical records?

6. WORKSTREAM C — TEMPORAL INFORMATION AND MEMORY
Investigate:

Bitemporal databases.

Event-time and system-time modeling.

Historical knowledge graphs.

Temporal event storage.

Append-only logs.

Change data capture.

Event sourcing and projection rebuilding.

Temporal relationship validity.

Historical snapshot reconstruction.

Temporal entity resolution.

Time-aware embeddings.

Temporal graph retrieval.

Incremental graph updating.

Knowledge revisions.

Historical contradiction tracking.

Time-dependent graph algorithms.

Relevant questions:

How can we reconstruct what was knowable on a particular date?

How do we distinguish an event's occurrence from the date of its disclosure?

How can historical snapshots be reconstructed efficiently?

How can current graph projections be rebuilt from original evidence?

How can the system correct past errors without destroying its historical state?

How do we prevent future information from leaking into historical evaluations?

Pay special attention to temporal knowledge-graph and event-sourcing implementations.

7. WORKSTREAM D — PROVENANCE, SOURCE QUALITY, AND VERIFICATION
Research:

Data provenance.

W3C PROV and PROV-O.

Processing lineage.

Claim verification.

Evidence-backed reasoning.

Fact-checking pipelines.

Source independence.

Citation dependency graphs.

Information provenance.

Claim-level contradiction detection.

Duplicate information propagation.

Source reliability modeling.

Evidence aggregation.

Retraction handling.

Assertion confidence calibration.

Probabilistic reasoning over uncertain evidence.

Truth discovery from conflicting sources.

Information-integrity analysis.

We need to distinguish:

A source reporting something.

The reported claim being true.

Multiple sources repeating the same original source.

Independent sources corroborating a claim.

A claim becoming prominent.

A claim being causally relevant.

Important design question
Should the provenance graph be separate from the semantic world graph?

Compare implementations and implications.

Required output
Recommend an evidence model that preserves:

Original source.

Source independence.

Extraction lineage.

Supporting evidence.

Contradictory evidence.

Model version.

Historical revision.

Permissions.

Reproducibility.

8. WORKSTREAM E — GRAPH DATABASES AND STORAGE
Do not assume we must use PostgreSQL or Neo4j.

Evaluate candidates across relational, graph, vector, document, search, and analytical storage.

Research relevant systems such as:

PostgreSQL.

pgvector.

Neo4j.

FalkorDB.

Memgraph.

ArangoDB.

TypeDB.

Kuzu.

NebulaGraph.

DuckDB.

ClickHouse.

OpenSearch.

Elasticsearch.

Other credible graph and temporal storage engines.

These names are research leads, not preapproved selections.

Compare
Native graph query capabilities.

Temporal data support.

Complex relationship modeling.

Hyperedge or event modeling.

Traversal performance.

Full-text search.

Semantic retrieval.

Hybrid retrieval.

Indexing.

Update performance.

Storage efficiency.

Transactional consistency.

Local development.

Backup and migration.

Open-source licensing.

Commercial deployment.

Operational complexity.

Multitenancy.

Access control.

Expected scaling limitations.

Required output
Produce a technical comparison for:

Single-database MVP.

Relational canonical store with graph projections.

Dedicated graph database with separate evidence storage.

Hybrid analytical architecture for larger scale.

Recommend the simplest architecture that meets the actual requirements.

9. WORKSTREAM F — MEMORY SEGMENTATION AND CONTEXT CONSTRUCTION
This is one of our most important research areas.

We need to represent broad information while activating only the relevant parts for each investigation.

Research:

Graph partitioning.

Dynamic graph communities.

Hierarchical memory.

Episodic versus semantic memory.

Agent long-term memory.

Contextual memory graphs.

Incremental knowledge summarization.

Semantic clustering.

Entity-centered memory.

Event-centered memory.

Domain-specific indexes.

Dynamic subgraph extraction.

Adaptive graph expansion.

Context caching.

Retrieval-time graph construction.

Materialized views.

Memory compression.

Query-specific graph projections.

Multi-hop retrieval.

Multi-index retrieval.

Information bottleneck approaches.

Retrieval with computation budgets.

Information-loss measurement.

Proposed concept to investigate: Evidence Capsules
A capsule would be a compact, rebuildable representation of relevant entities, events, claims, relationships, source references, and context.

It may be built around an entity, event, domain, community, or investigation.

Determine whether this concept provides an actual benefit over existing graph communities, materialized views, hierarchical summaries, or dynamic retrieval.

Required experiments
Compare:

No segmentation.

Static domain partitioning.

Entity-centered partitioning.

Event-centered partitioning.

Graph-community partitioning.

Dynamic query-specific segmentation.

Measure recall, precision, cross-domain completeness, token cost, latency, and historical accuracy.

10. WORKSTREAM G — GRAPH RETRIEVAL AND GRAPH-RAG
Search broadly for:

GraphRAG.

Hybrid RAG.

Knowledge-graph RAG.

Agentic RAG.

Multi-hop question answering.

Query-aware graph traversal.

Graph community summaries.

DRIFT-style retrieval.

Path-based retrieval.

Subgraph retrieval.

Graph reranking.

Relation-aware retrieval.

Structure-aware embeddings.

Graph-enhanced language models.

Hierarchical retrieval.

Context compression.

Retrieval planning.

Adaptive search depth.

Evidence-aware reranking.

Retrieval uncertainty estimation.

Investigate existing projects and papers, including relevant implementations of:

Microsoft GraphRAG.

Graphiti.

LightRAG.

HippoRAG.

Path-based GraphRAG systems.

Other newer or less well-known systems.

Do not assume any specific named project is best.

Key questions
Which methods best support cross-domain questions?

How do they handle evolving information?

How do they handle explicit provenance?

How do they prevent irrelevant graph expansion?

How do they deal with contradictory evidence?

Which can reconstruct historical information states?

Which offer practical cost advantages?

Which methods are sufficiently mature to reuse?

11. WORKSTREAM H — INFERENCE, LOGIC, AND HYPOTHESIS EVALUATION
Investigate the actual reasoning methods appropriate for our system.

Topics:

Neuro-symbolic reasoning.

Knowledge graph reasoning.

Abductive inference.

Deductive reasoning.

Inductive reasoning.

Probabilistic relational reasoning.

Bayesian networks.

Factor graphs.

Probabilistic programming.

Rule engines.

Datalog.

Constraint reasoning.

Graph reasoning with LLMs.

Hypothesis generation.

Hypothesis ranking.

Contradiction detection.

Explanatory reasoning.

Counterfactual reasoning.

Evidence-weighted inference.

Uncertainty calibration.

Structured planning.

Tool-assisted reasoning.

Multi-stage verification.

Automated hypothesis revision.

Our requirement
The system should not simply generate one attractive explanation.

It should maintain alternative hypotheses and identify evidence supporting or contradicting each.

Required output
Recommend which reasoning operations should be:

Deterministic.

Rule-based.

Statistical.

Neural.

LLM-assisted.

Human-reviewed.

Provide concrete algorithmic alternatives and their limitations.

12. WORKSTREAM I — ATTRIBUTION, INFORMATION PROPAGATION, AND CAUSAL INFERENCE
Research the scientific foundations of information propagation.

Include:

Information diffusion.

Network cascades.

Temporal text networks.

Information-source attribution.

Provenance reconstruction.

Influence versus homophily.

Shared-source effects.

Diffusion-tree inference.

Independent cascades.

Hawkes processes.

Temporal influence networks.

Network contagion models.

Causal graphical models.

Structural causal models.

Process tracing.

Natural experiments.

Quasi-experimental methods.

Causal discovery limitations.

Confounding.

Selection bias.

Counterfactual estimation.

Economic event studies.

Historical causal attribution.

Investigate software frameworks such as DoWhy, EconML, and relevant graph-causality research where appropriate.

Required distinctions
We need to measure separately:

Whether a source is authentic.

Whether a claim was actually made.

Whether a transmission path is documented.

Whether a relationship is plausibly inferred.

Whether evidence supports a causal conclusion.

Whether predicted consequences occurred.

Important research requirement
Identify which attribution problems are realistically solvable using observational data and which require direct interviews, experiments, or other evidence.

Do not confuse association with causal influence.

13. WORKSTREAM J — HUMAN DECISION PROCESSES AND EXPERT FRAMEWORKS
Research ways to represent professional decision-making methods as reusable computational structures.

Include:

Decision theory.

Bayesian decision-making.

Behavioral economics.

Organizational decision-making.

Management consulting issue trees.

Investment research frameworks.

Quantitative research processes.

Market intelligence methodologies.

Scenario planning.

Business strategy frameworks.

Causal decision models.

Evidence synthesis.

Expert systems.

Case-based reasoning.

Decision records.

Decision provenance.

Outcome-based evaluation.

Process mining.

Workflow mining.

Multi-criteria decision analysis.

Required capability
The system should be able to select an appropriate analytical method for a question.

For example, an acquisition investigation may require corporate strategy, financial relationships, public information analysis, and historical comparison.

Research how to:

Store expert methods.

Represent their assumptions.

Determine applicability.

Compose multiple methods.

Evaluate their performance.

Detect when a framework is unsuitable.

Update framework-selection policies.

Treat expert opinion as research input, not automatically as ground truth.

14. WORKSTREAM K — ECONOMIC AND ORGANIZATIONAL INTELLIGENCE
Investigate:

Corporate ownership networks.

Financial transaction graphs.

Capital-flow modeling.

Investment commitments versus completed transfers.

Acquisitions.

Contract relationships.

Procurement.

Supply-chain dependencies.

Economic input-output models.

Second-order economic effects.

Industrial capacity constraints.

Corporate event extraction.

Market shock analysis.

Competitive intelligence.

Private-market intelligence.

Institutional and regulatory changes.

Legal-entity resolution.

Financial knowledge graphs.

Circular investment and intercompany transaction analysis.

Research questions
How do existing firms reconstruct ownership, financing, and commercial relationships?

How much of that information is available through public records?

What cannot be observed without licensed datasets or primary research?

How should financial relationships be modeled to avoid falsely assuming that money actually changed hands?

How can we distinguish useful economic dependencies from speculative opportunity narratives?

Research relevant existing companies and products, including Palantir, CB Insights, AlphaSense, Recorded Future, Tracxn, PitchBook, and other relevant providers.

Identify legitimate data sources and practical costs.

15. WORKSTREAM L — NARRATIVE INTELLIGENCE AND INFORMATION NETWORKS
Research:

Narrative detection.

Narrative clustering.

Topic evolution.

Concept drift.

Information propagation.

Text reuse detection.

Cross-platform citation tracking.

Public discussion networks.

Network community detection.

Public opinion measurement limitations.

Narrative emergence.

Narrative decline.

Historical recurrence.

Coordinated amplification detection.

Source attribution.

Credibility and attention differences.

Temporal semantic similarity.

Multi-platform event alignment.

Study technical methods rather than focusing exclusively on sentiment analysis.

Relevant competitor categories include online narrative intelligence, information-integrity systems, and social network analytics.

Investigate Graphika and other relevant providers.

Crucial boundary
Understand observable information movement and publicly expressed positions without inventing hidden private beliefs or covertly exploiting personal psychological vulnerabilities.

16. WORKSTREAM M — FORECASTING AND HISTORICAL LEARNING
Research:

Temporal graph prediction.

Dynamic link prediction.

Event forecasting.

Knowledge graph completion.

Time-series forecasting.

Probabilistic forecasting.

Forecast calibration.

Brier scores.

Proper scoring rules.

Backtesting.

Walk-forward validation.

Concept drift.

Change-point detection.

Historical replay.

Temporal machine learning.

Online learning.

Continual learning.

Model updating.

Catastrophic forgetting.

Feedback loops.

Prediction markets as research references.

Human-machine forecasting.

Outcome-resolution methods.

Required experiment
Given an information cutoff date:

Reconstruct only the evidence available at that date.

Generate a forecast.

Commit the prediction.

Reveal subsequent outcomes.

Score the result.

Inspect the failure.

Measure whether the inference system improves over a baseline.

Find public benchmarks and open-source evaluation frameworks that support this.

Prioritize reproducibility and leakage prevention.

17. WORKSTREAM N — MODEL SELECTION, FINE-TUNING, AND MACHINE LEARNING
Research models and frameworks for:

Entity extraction.

Relation extraction.

Event extraction.

Coreference.

Entity resolution.

Semantic embeddings.

Reranking.

Hypothesis classification.

Contradiction detection.

Relation prediction.

Temporal graph embeddings.

Graph neural networks.

Forecasting.

Evidence-grounded generation.

Structured tool use.

Small-model task routing.

Investigate:

Open-weight LLMs.

Information-extraction models.

Sequence labeling models.

Graph neural-network frameworks.

Parameter-efficient fine-tuning.

LoRA and related methods.

Distillation.

Calibration.

Synthetic data generation.

Model evaluation and regression.

Quantization.

Local CPU/GPU inference.

Required recommendation
What can be accomplished using existing models and deterministic systems?

What would justify fine-tuning?

What validated dataset would be needed?

What is realistic on limited hardware?

Do not recommend training a large foundation model unless evidence clearly justifies it.

18. WORKSTREAM O — DATA ACQUISITION AND DATASET DISCOVERY
Discover legitimate datasets and APIs across:

Corporate and financial
SEC EDGAR, GLEIF, Companies House, government procurement and spending, corporate registries, patents, public financial disclosures, and authorized market datasets.

Research
OpenAlex, Crossref, Semantic Scholar, scholarly citation datasets, research repositories, patents, and technical publications.

Information networks
Permitted social-platform APIs, Bluesky AT Protocol, public citation networks, archives, appropriately licensed news, podcasts, transcripts, and other public publications.

Google ecosystem
Research official Google APIs and datasets relevant to:

Search interest.

Video metadata.

Public datasets.

News and information discovery.

Business and organization information.

Authorized user data integrations.

Private enterprise
Research secure integration approaches for:

Customer-owned documents.

Meeting notes.

Research workspaces.

CRM records.

Gmail and calendar.

Slack and authorized collaboration systems.

Enterprise knowledge repositories.

For each source provide
Exact official documentation.

Data types and coverage.

Historical depth.

Update frequency.

Geographic coverage.

Access requirements.

Free allowances or published costs.

Commercial reuse permissions.

Training and retention restrictions.

Rate limits.

Export support.

Expected data quality.

Relevant example queries.

Integration complexity.

Do not assume publicly accessible information is freely licensed for every commercial purpose.

19. WORKSTREAM P — DATA ENGINEERING AND INCREMENTAL COMPUTATION
Research:

Streaming ingestion.

Batch processing.

Data pipelines.

Change data capture.

Incremental view maintenance.

Dependency graphs.

Cache invalidation.

Event-driven processing.

Content-addressed storage.

Idempotent jobs.

Retry systems.

Dead-letter queues.

Data contracts.

Schema evolution.

Index rebuilding.

Lineage.

Distributed processing.

Deduplication.

Source refresh policies.

Failure recovery.

Data quality monitoring.

Main question
How do we update only the affected part of the information world model when new evidence arrives?

We should not have to rebuild every index, graph, hypothesis, and summary.

Compare simple local solutions with more advanced production architectures.

20. WORKSTREAM Q — AUTONOMOUS AGENTS AND WORKFLOW ORCHESTRATION
Research systems for:

Investigation planning.

Tool-using agents.

Durable workflows.

Bounded recursive research.

Multi-step retrieval.

Asynchronous job execution.

Checkpointing.

Human escalation.

Scheduled monitoring.

Background investigations.

Model routing.

Agent state.

Task budgets.

Structured tool outputs.

Agent evaluation.

Error recovery.

Investigate orchestration options including LangGraph, Temporal, PydanticAI, workflow engines, and simpler custom implementations.

Requirement
We do not want a swarm of unconstrained agents.

Each autonomous component needs:

Defined input.

Defined output.

Access scope.

Resource budget.

Stop condition.

Error handling.

Evaluation criteria.

The initial design should remain simple enough for a small founding team to operate.

21. WORKSTREAM R — SECURITY, PERMISSIONS, AND PRIVATE INFORMATION
Research:

Multitenant data architecture.

Row-level security.

Attribute-based access control.

Role-based access control.

Policy engines.

Source-level permissions.

Derived-data access propagation.

Information-flow controls.

Encryption.

Customer-managed keys.

Private deployment.

Audit logs.

Secure connectors.

Prompt-injection defenses.

Data deletion and correction.

Provenance-based access control.

Model-provider data boundaries.

Secure retrieval.

Private inference.

Enterprise compliance.

Important problem
If confidential customer evidence contributes to a derived conclusion, the conclusion must not leak protected facts to unauthorized users.

Investigate practical ways to propagate permissions through derived relationships, graph projections, summaries, and generated answers.

Include threat models and required controls.

22. WORKSTREAM S — USER INTERFACES AND AGENT INTEROPERABILITY
Research:

Messaging-first AI applications.

WhatsApp Business API.

Slack integrations.

Supported iMessage integration options.

MCP server architecture.

API gateway design.

Authentication and OAuth.

CLI research tools.

Notification infrastructure.

Streaming responses.

Long-running research jobs.

Status updates.

Evidence inspection interfaces.

Explainability UI.

Source citations.

Graph investigation visualizations.

User feedback capture.

The first user experience should be simple and conversational.

The backend should remain independent of the messaging provider.

Required recommendation
What is the easiest legitimate messaging-style interface to launch locally?

What would it take to support WhatsApp later?

How should the same intelligence engine be exposed to MCP, APIs, and other systems?

23. WORKSTREAM T — EXISTING COMPETITORS AND INDUSTRY ARCHITECTURES
Investigate both direct competitors and adjacent systems.

Categories:

Enterprise operational intelligence.

Narrative and information-network intelligence.

Market and private-company intelligence.

Financial knowledge graphs.

Cyber threat intelligence.

Agent memory infrastructure.

Enterprise research assistants.

Public knowledge graph providers.

AI world-model research.

Decision-support platforms.

For each important competitor:

What do they sell?

Who buys it?

What information do they use?

What can be learned from their published architecture?

What is publicly known about their inference capabilities?

What cannot be established without product access?

How do they charge?

What is their likely competitive advantage?

Which of our proposed capabilities may already exist?

What demonstrable gap, if any, remains?

Do not manufacture a market gap simply because we want to build a company.

24. WORKSTREAM U — COST, PERFORMANCE, AND DEPLOYMENT
Research the expected economics of candidate architectures.

Evaluate:

Local laptop development.

CPU-only inference.

Consumer GPU inference.

Hosted model APIs.

Embedding costs.

Graph storage.

Vector indexing.

Source archiving.

Incremental updates.

Monitoring costs.

Long-running investigations.

Database operations.

Backup and recovery.

Enterprise hosting.

Scaling from thousands to millions of observations.

Provide explicit assumptions.

Estimate costs at several illustrative scales:

10,000 observations.

100,000 observations.

1 million observations.

10 million observations.

Do not invent precise costs where measurements are unavailable.

Give reproducible benchmark plans where necessary.

Identify the components likely to dominate costs.

25. WORKSTREAM V — EXPERIMENTS, BENCHMARKS, AND SCIENTIFIC VALIDITY
Find benchmarks and build evaluation proposals for:

Entity resolution.

Relation extraction.

Temporal reasoning.

Graph retrieval.

Multi-hop evidence retrieval.

Source-grounded question answering.

Attribution.

Forecasting.

Model calibration.

Context efficiency.

Source provenance.

Multi-domain reasoning.

Information extraction.

Continual knowledge updating.

Investigate Temporal Graph Benchmark and other relevant datasets.

Compare at least three approaches
Baseline A: Hybrid lexical/vector RAG.

Baseline B: Established GraphRAG or temporal-graph retrieval.

Candidate C: Our evidence-native, segmented, adaptive inference architecture.

All must use equivalent information access for fair evaluation.

Avoid
Future-data leakage.

Self-scored unsupported claims.

Cherry-picked historical examples.

Training/test contamination.

Confusing graph proximity with causality.

Comparing systems on unequal information.

Assuming longer explanations are better.

Mistaking a plausible answer for a correct answer.

26. WORKSTREAM W — FOUNDER RESEARCH, DOCUMENTATION, AND MIGRATION
We need to preserve learning across tools, people, and time.

Research:

Architecture decision records.

Technical knowledge bases.

Research-management systems.

Structured meeting intelligence.

Experiment tracking.

Dataset versioning.

Model versioning.

Prompt versioning.

Reproducible environments.

Agent handoff specifications.

Markdown/JSONL portability.

Schema migration.

Repository documentation.

Research citation management.

Long-term knowledge maintenance.

The system should eventually incorporate authorized founder meetings, objections, product decisions, customer interviews, and technical feedback as structured research records.

We also need instructions for how AI agents should exchange findings without losing provenance or silently changing requirements.

27. DISCOVER ADDITIONAL RESEARCH DOMAINS
The categories above are a starting inventory.

You are specifically instructed to identify missing fields.

Examples might include:

Scientific discovery systems.

Knowledge-grounded simulation.

Digital twins.

Probabilistic databases.

Database provenance semirings.

Truth-maintenance systems.

Active learning.

Value-of-information methods.

Mechanism design.

Dynamic Bayesian networks.

Graph change detection.

Industrial economic modeling.

Research agents.

Hybrid symbolic/neural world models.

Do not limit discovery to the keywords already supplied.

For every new domain, explain exactly which IWM requirement it addresses.

28. REQUIRED REPOSITORY RESEARCH FORMAT
For every serious candidate repository, provide:

Field	Required information
Name	Exact project name
URL	Verified repository URL
Category	Primary research workstream
License	Verified license
Maintenance	Last known activity and maintenance indicators
Technical approach	Key algorithms and architecture
Implemented capabilities	Supported by actual docs or code
Missing capabilities	Relevant limitations
Dependencies	Major infrastructure and frameworks
Local feasibility	Hardware and setup
Production suitability	Security, scale, maturity
Integration fit	How it could fit the IWM
Replacement scope	Which components it could replace
Risks	Technical, licensing, operational
Evidence	Repository/docs/papers supporting claims
Recommendation	Use / investigate / avoid / benchmark
Rank candidates within each workstream.

Do not return an arbitrary popularity ranking.

29. REQUIRED COMPARATIVE ARCHITECTURES
Design at least three plausible implementations.

Architecture A — Minimal local prototype
Optimized for speed, simplicity, and low cost.

Architecture B — Research-oriented system
Optimized for evaluating novel retrieval, inference, memory, and learning methods.

Architecture C — Production-oriented architecture
Optimized for scalability, multi-tenant security, monitoring, and enterprise reliability.

For each, provide:

Component diagram.

Information flow.

Storage choices.

Inference execution.

Security boundaries.

Update strategy.

Evaluation compatibility.

Expected bottlenecks.

Advantages.

Disadvantages.

Migration path.

Explain which components should be common across all three.

30. REQUIRED FINAL DELIVERABLES
Return a structured research package containing:

01 — Executive Research Verdict

Is the concept technically coherent? Which parts are feasible? Which assumptions are questionable?

02 — Research Landscape

Map the scientific and technical fields relevant to the project.

03 — Repository Atlas

Categorized, verified GitHub and open-source findings.

04 — Technology Comparison Matrix

Compare alternative implementations by capability, cost, maturity, and integration difficulty.

05 — Architecture Gap Analysis

Match existing technology against every requirement in the attached architecture register.

06 — Recommended Component Stack

Propose the most suitable initial technologies, with alternatives.

07 — Proprietary Research Opportunities

Identify where genuinely original algorithms, data structures, or inference methods might create an advantage.

08 — Data Source Catalogue

Verified, permissible APIs and datasets with licenses, costs, and scope.

09 — Benchmark and Evaluation Plan

Experiments designed to prove or disprove the project's core technical assumptions.

10 — Minimal Prototype Architecture

The simplest credible system demonstrating the entire information-to-inference-to-learning loop.

11 — Scaling Architecture

How the prototype could evolve without discarding its information contracts.

12 — Risks and Failure Modes

Technical, scientific, privacy, operational, and economic risks.

13 — Build-vs-Reuse Matrix

What should be built, integrated, researched, deferred, or avoided.

14 — Implementation Dependencies

A dependency-ordered roadmap with recommended research and implementation sequence.

15 — Unresolved Decisions

Questions that still require founder, expert, customer, or experimental input.

31. YOUR OUTPUT MUST BE DECISION-READY
Do not return only a narrative.

Use structured tables where useful.

Provide links to original sources.

For important claims, distinguish:

Verified directly from documentation or code.

Supported by published research.

Reported by a commercial provider.

Inferred from available information.

Unknown or unverified.

Include the date on which a changing technical claim was checked.

Where technologies compete, state which you recommend and under what assumptions.

Where information is unavailable, give a concrete method to verify it.

Where our architecture is mistaken, say so explicitly.

32. FINAL INSTRUCTION
Your purpose is to help us discover the strongest possible technical foundation for an evolving, relationship-native Information World Model.

We want an architecture that can understand evidence, relationships, history, information propagation, economic consequences, and professional decisions without pretending to possess complete knowledge.

We also want to discover whether our proposed approach is technically novel, economically viable, and measurably better than existing alternatives.

Do not prioritize confirmation of our existing architecture. Prioritize discovering the truth about what can be built, what already exists, and what is worth inventing.

The companion document, Complete Architecture Requirements Register, defines our functional requirements and must be used to evaluate candidate technologies.

Do not silently remove or reinterpret those requirements.

If a requirement is impractical, identify the conflict and recommend an explicit revision.

Start with a comprehensive research inventory, then narrow the results through technical evidence and comparative evaluation.
