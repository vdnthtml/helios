# Next agent — Helios build continuation

Current founder request authorizes fast reversible feature implementation and a daily shipping cadence. Read root AGENTS and context/BUILD_PLAN.md, STATE's latest build update, and DECISIONS's build authorization. Earlier research-only/zero-code summaries are historical baseline statements.

Actual first feature: `/tmp/helios-evidence`, branch `feat/evidence-foundation`, commits 020a751 and 3b2c776 over 70bd982. Eighteen local tests pass. Working code is also preserved as `releases/helios-evidence-foundation.bundle` (full Git history) and `.patch` (diff from baseline). Use the verified bundle if the temp worktree is missing.

The evidence feature has generated stable IDs, source-scoped external identifiers, body content hashes, observation idempotency, evidence-linked assertions, modality/status, ingestion-cutoff queries, scope filtering and append-only corrections. It is a trusted-caller SQLite reference library; it does not implement production auth/RLS, actual Postgres, model inference, semantic entailment validation or complete public-availability replay.

Push attempted but github.com DNS failed; gh reports no active login. PyPI resolution also failed, so no API/model dependency was installed. Do not claim a remote branch, PR, deployed service or scheduled daily push. Preserve another agent's main-branch changes.

Next task: make the existing feature branch available in the canonical authenticated repo, then implement and test the Postgres adapter and Pydantic/API contracts, followed by one permitted real source. Models: compare GLiNER and schema extraction with Qwen3-8B/14B, Qwen3-Embedding-0.6B and Qwen3-Reranker-0.6B; verify checkpoints/licenses and performance before adoption. Capture reviewed labels first; extractor LoRA is the first fine-tuning candidate after a measured gap.

Founder-review proposal: `context/proposals/HELIOS_SIGNAL_V0_1_PROPOSAL.md` reconciles the earlier IWM architecture with six later specialist audits and competitor research. It is not an approved implementation plan. It specifically requires authenticated read-only remote inspection before reconciling or mutating GitHub, source/weight licence verification before pinning dependencies, and founder approval before a docs branch/diff/commit/push. Treat all external component and pricing claims there as dated research inputs, not present facts.

At session end log code/test/commit/push evidence, update state and decisions, and leave one concrete next feature.
