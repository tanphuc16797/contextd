# pack-ai-app — Prompt Overrides

## Self-Check append

```
### LLM App (pack-ai-app)
- Model ID read from config (not hardcoded)
- Prompt template has explicit version/name
- max_tokens set explicitly per LLM call
- Long static system prompt uses cache_control
- No PII / raw user prompt in logs (metadata only)
- Structured output via schema (tool_choice / response_format)
- RAG response cites source chunk/doc
- Token usage logged per call (input, output, cache_read)
```

## Common Pitfalls (Top 10)

Mỗi task PHẢI rà soát anti-patterns trong [`../common-pitfalls.md`](../common-pitfalls.md):

```md
### Common Pitfalls — check trước khi commit
- Không vi phạm bất kỳ P01..P10 trong common-pitfalls.md (rule/why/detect/severity)
- Pitfall regex-detectable: confirm Layer-1 validator PASS
- Pitfall design-only: tick từng item ở Layer-2 self-check
```
