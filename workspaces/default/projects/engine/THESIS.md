# THESIS — engine

## Scope

Project-level thesis for `workspaces/default/projects/engine/` in workspace `wiki`.

## Problem Statement

Engine knowledge must stay actionable for users while preserving strict workspace isolation and deterministic decision rules. Without a single canonical thesis document, governance intent can drift across service docs, patterns, and audits.

## Core Thesis

1. Workspace isolation is mandatory for every retrieval and execution step.
2. Layering is explicit: engine specs explain how internals work; workspace patterns explain what to apply.
3. Decision priority is deterministic and enforced: Contracts > Platform Patterns > Project Docs > Domain Knowledge.
4. Contract-first and pattern-reuse are default; avoid inventing architecture when reusable patterns already exist.
5. Observability and traceability are required through lint, checks, and run artifacts.

## Non-Negotiables

- Never read or apply knowledge from a non-active workspace.
- Never bypass higher-priority contracts with lower-priority docs.
- Never encode assumptions as facts when workspace knowledge is missing.
- Keep service mapping and command behavior documentation consistent.

## Decision Priority Order

1. Contracts (`workspaces/default/platform/contracts/`)
2. Platform Patterns (`workspaces/default/platform/patterns/`)
3. Project Docs (`workspaces/default/projects/engine/`)
4. Domain Knowledge (`workspaces/default/domains/`)

## Out of Scope

- Detailed engine internal architecture specifications.
- Pack-specific rules that are not active in workspace `wiki`.
- Cross-workspace pattern import or fallback behavior.

## How to Validate

Run:

```bash
python3 scripts/lint-wiki.py --all-workspaces --wiki-root .
python3 scripts/check-patterns-index.py
```

Then verify project mappings and thesis references stay consistent across:

- `workspaces/default/projects/engine/knowledge-map.md`
- `workspaces/default/projects/engine/thesis-audit-report.md`

## Related

- [Knowledge Map — engine](knowledge-map.md)
- [Thesis Audit Report — wiki-template-plugin](thesis-audit-report.md)
- [ADR-003: Self-Referential Engine Workspace](../../decisions/003-self-referential-engine-workspace.md)
- [Workspace — wiki](../../workspace.md)
