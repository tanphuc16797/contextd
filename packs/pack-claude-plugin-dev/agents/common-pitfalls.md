# pack-claude-plugin-dev — Top 10 Common Pitfalls

Anti-pattern khi build Claude Code plugin (commands/agents/skills/hooks). Additive trên [constraints.md](constraints.md).

## P01 — Thiếu plugin.json manifest
- **NG**: zip plugin nhưng quên `plugin.json` ở root.
- **OK**: manifest có `name`, `version`, `description`, `entry`.
- **Why**: install fail silent; user không thấy plugin.
- **Detect**: Layer-1 `pack-claude-plugin-dev-missing-manifest` (new) — check zip root.
- **Severity**: error

## P02 — Slash command thiếu description
- **NG**: `.claude/commands/foo.md` không có front-matter `description`.
- **OK**: front-matter `description: "what it does"`.
- **Why**: `/help` không show; user không discover.
- **Detect**: Layer-1 — md không có `description:` frontmatter.
- **Severity**: warn

## P03 — Subagent thiếu explicit tools
- **NG**: `.claude/agents/x.md` không liệt kê tools → inherit toàn bộ (kể cả nguy hiểm).
- **OK**: `tools: [Read, Grep]` whitelist.
- **Why**: principle of least privilege; sandbox break.
- **Detect**: Layer-1 — agent md thiếu `tools:` field.
- **Severity**: error

## P04 — Hardcoded API secret / token
- **NG**: `ANTHROPIC_API_KEY="sk-..."` trong file plugin.
- **OK**: env var; document setup; never commit.
- **Why**: secret leak khi share/publish.
- **Detect**: Layer-1 `pack-claude-plugin-dev-hardcoded-secret` (new) — regex `sk-[a-zA-Z0-9]{20,}|api_key\s*=\s*["'][^"']+`.
- **Severity**: error

## P05 — Hook chạy đồng bộ block UI
- **NG**: `UserPromptSubmit` hook gọi network 10s → user đợi.
- **OK**: hook < 500ms; long task → background queue.
- **Why**: UX freeze.
- **Detect**: Layer-2 — hook code có sync HTTP / heavy compute.
- **Severity**: error

## P06 — Manifest không version
- **NG**: `plugin.json` không có `version`, hoặc giữ `0.0.1` mãi.
- **OK**: semver; bump mỗi release.
- **Why**: user không biết update; bug report không truy được.
- **Detect**: Layer-1 — manifest thiếu `version`.
- **Severity**: warn

## P07 — Slash command conflict tên built-in
- **NG**: tạo `/help`, `/init`, `/clear`.
- **OK**: namespace bằng prefix (e.g. `/myplugin-help`).
- **Why**: shadow command, user confused.
- **Detect**: Layer-1 — check tên trong reserved list.
- **Severity**: error

## P08 — Không document permission scope
- **NG**: plugin yêu cầu Bash + Write nhưng README không nói.
- **OK**: README có "Permissions: ...", install ask user accept.
- **Why**: trust break, install bị reject.
- **Detect**: Layer-2 — README có section Permissions.
- **Severity**: warn

## P09 — Không test path trên Windows
- **NG**: command dùng `/` slash, fail trên Windows.
- **OK**: dùng `pathlib`/`path.join`; test cross-OS.
- **Why**: 50% user Windows; bug report flood.
- **Detect**: Layer-2 — CI matrix có windows-latest.
- **Severity**: warn

## P10 — Không guard against null/missing input
- **NG**: hook đọc `$CLAUDE_INPUT` không check empty.
- **OK**: validate input, default + error message rõ.
- **Why**: silent fail, crash, bad UX.
- **Detect**: Layer-2 — hook script có input validation.
- **Severity**: warn

## Mapping to validator

| Pitfall | Layer-1 rule ID | Layer-2 self-check |
|---|---|---|
| P01 manifest | `pack-claude-plugin-dev-missing-manifest` (new) | ✓ |
| P02 desc | `pack-claude-plugin-dev-cmd-no-desc` (new) | ✓ |
| P03 tools | `pack-claude-plugin-dev-agent-no-tools` (new) | ✓ |
| P04 secret | `pack-claude-plugin-dev-hardcoded-secret` (new) | ✓ |
| P05 hook-block | — | ✓ |
| P06 version | `pack-claude-plugin-dev-manifest-no-version` (new) | ✓ |
| P07 conflict | — | ✓ |
| P08 perm-doc | — | ✓ |
| P09 windows | — | ✓ |
| P10 null-input | — | ✓ |
