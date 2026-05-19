# pack-security

Security engineering **+ authorized pentest** pack. Threat modeling, secure design review, vulnerability management, security controls **and** scope discipline, evidence-based findings, risk rating, remediation reporting.

> **v0.2.0 absorbs `pack-pentest`** — workspaces that previously listed `- pack-pentest` should switch to `- pack-security`.

## When to enable

Workspace opts in by adding `- pack-security` under `## Packs` in `workspaces/{ws}/workspace.md`.

Enable when workspace needs:
- Security-by-design before implementation
- Consistent quality for security review/triage/control verification
- Standardized pentest output (fewer false positives, evidence-backed findings)
- Actionable remediation for engineering team

## What it adds

- **Constraints** (`agents/constraints.md`) — hard rules for security + pentest workflow (two sections)
- **Coding rules** (`agents/coding-rules.md`) — conventions for docs/checklists/findings/reports
- **Validator rules** (`agents/pipeline/validator-rules.md` + `scripts/rules.py`) — automated gates
- **Retrieval map** (`agents/pipeline/retrieval-map.md`) — component → knowledge docs mapping
- **Prompt overrides** (`agents/pipeline/prompt-overrides.md`) — security + pentest self-check
- **Common pitfalls** (`agents/common-pitfalls.md`) — Top 10 security + Top 10 pentest

## Components declared

Security engineering: `threat-modeling`, `secure-design-review`, `vulnerability-management`, `security-controls`

Pentest workflow: `attack-surface-mapping`, `finding-validation`, `exploit-safety`, `reporting-remediation`

## Conflicts with

(none)

## Related

- Pack mechanism: [packs/README.md](../README.md)
- Cross-cutting principles: [agents/cross-cutting-principles.md](../../agents/cross-cutting-principles.md)
