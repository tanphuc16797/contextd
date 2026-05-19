# pack-claude-plugin-dev — Prompt Overrides

## Self-Check append

```
### Claude Code Plugin (pack-claude-plugin-dev)
- Plugin manifest exists with name (kebab-case), version (semver), description (>=20 chars), author
- Every slash command has description: frontmatter (single action-verb sentence)
- argument-hint set when command takes args; allowed-tools restricts to minimum
- Every subagent has explicit tools: list (no wildcard / no missing field)
- Subagent model: chosen per task complexity (haiku/sonnet/opus)
- Every skill description >= 50 chars with TRIGGER when: phrase for auto-invoke
- No hardcoded API key / token anywhere (sk-, ghp_, AKIA, AIzaSy, xoxb-)
- Hook script idempotent, <2s, errors to stderr, exit 0 on non-critical fail
- MCP server config uses env vars for credentials
- README install instructions + min Claude Code version
- CHANGELOG entry for each version with breaking changes flagged
```

## Common Pitfalls (Top 10)

Mỗi task PHẢI rà soát anti-patterns trong [`../common-pitfalls.md`](../common-pitfalls.md):

```md
### Common Pitfalls — check trước khi commit
- Không vi phạm bất kỳ P01..P10 trong common-pitfalls.md (rule/why/detect/severity)
- Pitfall regex-detectable: confirm Layer-1 validator PASS
- Pitfall design-only: tick từng item ở Layer-2 self-check
```
