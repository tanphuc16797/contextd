# pack-qc — Retrieval Map

Component → wiki doc mapping for this pack.

| Component | Docs to retrieve |
|-----------|------------------|
| `test-case-design` | `{ws}/projects/{project}/services/`, `{ws}/platform/contracts/`, `{ws}/domains/{domain}/` |
| `test-execution` | `{ws}/runbooks/`, `{ws}/projects/{project}/services/`, `{ws}/evidence/` |
| `defect-triage` | `{ws}/runbooks/`, `{ws}/projects/{project}/services/`, `{ws}/domains/{domain}/` |
| `regression-plan` | `{ws}/projects/{project}/knowledge-map.md`, `{ws}/platform/contracts/`, `{ws}/runbooks/` |
| `performance-profiling` (perf) | `{ws}/projects/{project}/services/`, `{ws}/runbooks/`, `{ws}/decisions/` |
| `bottleneck-analysis` (perf) | `{ws}/platform/architecture/`, `{ws}/projects/{project}/services/` |
| `optimization-safety` (perf) | `{ws}/platform/contracts/`, `{ws}/domains/{domain}/workflow.md` |
| `regression-guard` (perf) | `{ws}/runbooks/`, `{ws}/projects/{project}/knowledge-map.md` |

Components must match `pack.yaml#components`.
