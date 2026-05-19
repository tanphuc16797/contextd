# pack-web-api — Prompt Overrides

## Self-Check append

```
### API Boundary (pack-web-api)
- Input validated at the boundary (framework validation, not ad-hoc if-checks)
- Error response uses structured shape — no raw exception/stack trace in body
- Auth check precedes business logic (middleware/decorator, not inline)
- Mutating endpoint has idempotency strategy (key header or upsert)
- No PII/secret in request/response log
- No hardcoded base URL (read from config/env)
```

## Common Pitfalls (Top 10)

Mỗi task PHẢI rà soát anti-patterns trong [`../common-pitfalls.md`](../common-pitfalls.md):

```md
### Common Pitfalls — check trước khi commit
- Không vi phạm bất kỳ P01..P10 trong common-pitfalls.md (rule/why/detect/severity)
- Pitfall regex-detectable: confirm Layer-1 validator PASS
- Pitfall design-only: tick từng item ở Layer-2 self-check
```
