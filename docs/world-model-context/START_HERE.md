# Start here — portable project context

Version 0.1.0 · 2026-11-14 · Documentation baseline · Pre-implementation

## Read order

1. `STATE.md`: actual project state and next step.
2. `CURRENT_DIRECTION.md`: what we are trying to build now.
3. `DECISIONS.md`: what is confirmed, proposed, unresolved, or historical.
4. `ARCHITECTURE.md`, `EVALUATION.md`, `SECURITY.md`: technical reasoning and constraints.
5. Your role-specific file in `handoffs/`.
6. `reference/ARCHITECTURE_REQUIREMENTS.md`: full capability scope; `REQUIREMENTS.csv` is its lookup index.
7. `PROVENANCE.md` and `sources/conversation-2026-11-14.txt` when resolving ambiguity.

Paths in this list are relative to `context/`. Repository instructions live in root `AGENTS.md`.

## Authority order

Current explicit founder instructions → explicit founder decisions/corrections in the supplied source → latest reference requirements as the working scope → proposed architecture → earlier ideation and historical assistant suggestions.

A later assistant message cannot overrule the founder merely because it appears later. A source document saying “confirmed” is not independent proof that every engineering detail was approved. Preserve disagreements as open decisions.

## What to send another tool

Send the complete portable ZIP whenever possible. For limited context, send `handoffs/NEXT_AGENT.md`, `CURRENT_DIRECTION.md`, `DECISIONS.md`, `STATE.md`, and the relevant role packet; include the full requirements register for architectural research. Summaries are entry points, not substitutes for the complete source.

The original discussion asked for research and technical review before final implementation choices. Documentation work is complete for this baseline; the product has not been built. The next agent should carry out a concrete research or review task and update these records.

## At the end of a session

Use `templates/SESSION.md`. Record evidence, decisions, changed files, actual verification, remaining unknowns, and a direct next action. Update state and changelog before switching tools. Never put credentials in this bundle.
