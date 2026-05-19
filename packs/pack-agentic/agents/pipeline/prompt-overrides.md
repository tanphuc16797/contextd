# pack-agentic — Prompt Overrides

## Self-Check append

```
### Agent (pack-agentic)
- Loop has MAX_STEPS bound + explicit termination condition
- Repeated-state detection in place
- Every tool call wrapped in timeout
- Tool input has schema validation; tool error returned structured
- Destructive tools require confirm param or human approval checkpoint
- Per-step trace logged (step_n, action, latency, status)
- Token budget tracked; context compaction strategy explicit
- Subagent handoff has clear protocol + bounded depth
```

## Common Pitfalls (Top 10)

Mỗi task PHẢI rà soát anti-patterns trong [`../common-pitfalls.md`](../common-pitfalls.md):

```md
### Common Pitfalls — check trước khi commit
- Không vi phạm bất kỳ P01..P10 trong common-pitfalls.md (rule/why/detect/severity)
- Pitfall regex-detectable: confirm Layer-1 validator PASS
- Pitfall design-only: tick từng item ở Layer-2 self-check
```
