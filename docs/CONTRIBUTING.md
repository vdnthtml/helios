# Contributing to Helios

## Before making a change

1. Read the README, architecture, roadmap, and decision log.
2. Inspect the working tree; documentation is not proof that a component exists.
3. Keep founder direction, verified evidence, external research, and your own proposals separate.
4. If a change selects a technology, schema, model, or policy, add or update a decision record with alternatives and verification needed.

## Engineering rules

- Do not collapse observations, assertions, events, relationships, hypotheses, and outcomes into one generic “fact” record.
- Preserve raw source references, content hashes where appropriate, extraction/version lineage, time fields, scope, and correction history.
- Treat identity matching as evidence-based and reversible.
- Ensure derived indexes, graphs, summaries, and capsules can be rebuilt from canonical records.
- Enforce permission, licensing, and retention constraints in derived artifacts as well as raw input.
- State uncertainty and source dependence in user-visible answers.
- Bound automated investigations by scope, budget, and stopping conditions.
- Never claim a benchmark, license, capability, security property, or data right was checked unless the primary evidence and date are recorded.

## Documentation changes

Update the relevant architecture, roadmap, and decision log in the same change when you alter an architectural assumption. For implementation work, add tests and verification notes that distinguish what ran from what is merely planned.

## Security and data handling

Never commit secrets, access tokens, unredacted private material, or restricted source data. Do not scrape, retain, share, or train on material without authorization. When unsure about a source’s rights or a record’s scope, treat it as restricted until reviewed.
