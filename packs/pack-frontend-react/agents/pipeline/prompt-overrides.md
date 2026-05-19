# pack-frontend-react — Prompt Overrides

## Self-Check append

```
### React (pack-frontend-react)
- Hooks called at top level only (no condition/loop)
- No direct state mutation — use setter / functional update
- All effects with subscription/listener/timer have cleanup
- All <img> have alt attribute, interactive elements have accessible label
- List items have stable key (not array index unless list is immutable)
- Server vs Client boundary respected (Next.js: "use client" only when needed)
- No expensive computation in render body without useMemo
```

## Common Pitfalls (Top 10)

Mỗi task PHẢI rà soát anti-patterns trong [`../common-pitfalls.md`](../common-pitfalls.md):

```md
### Common Pitfalls — check trước khi commit
- Không vi phạm bất kỳ P01..P10 trong common-pitfalls.md (rule/why/detect/severity)
- Pitfall regex-detectable: confirm Layer-1 validator PASS
- Pitfall design-only: tick từng item ở Layer-2 self-check
```
