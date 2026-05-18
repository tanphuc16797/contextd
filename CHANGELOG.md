# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed — Rebrand `workspace-wiki` → `contextd`

This release rebrands the project. Project name and slash-command prefix change; the *content* layer (workspace knowledge base, still called "wiki") and several legacy filenames are kept for v0.x compatibility.

#### Project name & branding
- Display name `Workspace Wiki` → `contextd` in README, CLAUDE.md, onboarding HTML (VI + EN), GitHub Pages redirect title, and `/contextd-upgrade` / `/contextd-version` command docs.
- New tagline: *"A scoped context daemon for AI coding agents."*
- Added `## Project Identity` section to CLAUDE.md so agents read the new naming on every turn.
- GitHub repo URLs intentionally **unchanged** in this version — still `tanphuc16797/workspace-wiki`. Repo rename and release tagging under the new name are deferred to a follow-up.

#### Default workspace rename
- Folder `workspaces/wiki/` → `workspaces/default/` (full git rename — history preserved).
- `.claude/wiki.json` pointer field updated to `"workspace": "default"`.
- `workspaces/default/workspace.md` title updated.
- Evidence `manifest.yaml` + `source.yaml` `workspace` fields updated.
- `scripts/package-release.sh` staging filter updated to keep `workspaces/default/`.

#### Slash command rename (`/wiki-*` → `/contextd-*`)
All 14 engine slash commands now use the `/contextd-*` prefix:

| Old | New |
|---|---|
| `/wiki-setup` | `/contextd-setup` |
| `/wiki-detect` | `/contextd-detect` |
| `/wiki-eval` | `/contextd-eval` |
| `/wiki-trace` | `/contextd-trace` |
| `/wiki-viz` | `/contextd-viz` |
| `/wiki-report` | `/contextd-report` |
| `/wiki-explain` | `/contextd-explain` |
| `/wiki-backup` | `/contextd-backup` |
| `/wiki-restore` | `/contextd-restore` |
| `/wiki-upgrade` | `/contextd-upgrade` |
| `/wiki-version` | `/contextd-version` |
| `/use-wiki` | `/contextd-use` |
| `/update-wiki` | `/contextd-update` |
| `/rebase-wiki` | `/contextd-rebase` |

Command H1 titles rewritten to `# /contextd-{verb} — <descriptive>` so the skill listing no longer shows mismatched "Wiki Setup" / "Wiki Eval" labels.

#### Subagent rename
5 subagents in `.claude/agents/` renamed (file + YAML `name:` field + cross-references):

| Old | New |
|---|---|
| `wiki-planner` | `contextd-planner` |
| `wiki-context-selector` | `contextd-context-selector` |
| `wiki-plan-reviewer` | `contextd-plan-reviewer` |
| `wiki-curator` | `contextd-curator` |
| `wiki-reviewer` | `contextd-reviewer` |

#### Release artifacts (migration window)
`scripts/package-release.sh` and `.github/workflows/release.yml` now emit **both** naming conventions in parallel so existing installer URLs keep working:

- Canonical (new): `contextd-{ver}.zip`, `contextd-latest.zip`
- Legacy alias (same content): `wiki-template-{ver}.zip`, `wiki-template-latest.zip`

`install.sh` / `install.ps1` in releases download `contextd-latest.zip`. `SHA256SUMS.txt` includes both.

#### Installer migration
`scripts/install-to-claude.{sh,py}` automatically clean up legacy installs:

- Removes 14 legacy `~/.claude/commands/wiki-*.md` / `~/.claude/commands/{use,update,rebase}-wiki.md` files after syncing the new `contextd-*.md` equivalents.
- Removes 5 legacy `~/.claude/agents/wiki-*.md` subagent files.
- Prints a migration notice telling users to update any codebase `<cwd>/.claude/wiki.json` field `"workspace": "wiki"` → `"default"`.

#### Onboarding HTML
Download buttons in `onboarding/install.{html,en.html}` now point to `contextd-latest.zip`. Titles, headings, and footer branding switched to `contextd` (with `formerly Workspace Wiki` notes in source comments for traceability).

### Kept (deferred to v1.0)
Legacy filenames are intentionally **not** renamed in v0.x to avoid breaking existing user installs and pointer files:

- `<cwd>/.claude/wiki.json` (per-codebase pointer)
- `~/.claude/wiki-global.json` (global pointer)
- `~/.claude/wiki-install-meta.json` (install metadata)
- `wiki-template/` (zip root folder name inside release artifacts)
- `scripts/lint-wiki.py`, `scripts/check-patterns-index.py`
- The noun **"wiki"** as the term for *content* (contracts, patterns, domain docs under `workspaces/{ws}/`). `contextd` = engine; "wiki" = content. See CLAUDE.md `## Project Identity` for the boundary.

### Migration guide

Existing users upgrading to this version:

1. Pull the latest source (or download the new release artifact under either `contextd-latest.zip` or the legacy `wiki-template-latest.zip` — same file).
2. Re-run `bash scripts/install-to-claude.sh` (or `python scripts/install-to-claude.py`). The installer will:
   - Sync the new `contextd-*` slash commands and subagents into `~/.claude/`.
   - Remove the 14 legacy `wiki-*.md` / `*-wiki.md` command files and 5 legacy `wiki-*.md` subagent files.
   - Print a migration notice.
3. For each codebase whose `<cwd>/.claude/wiki.json` references the old default workspace name, update the field:
   ```diff
   - "workspace": "wiki"
   + "workspace": "default"
   ```
   Or re-run `/switch-workspace default` from inside that codebase.
4. Restart Claude Code so the new slash commands are picked up.

No data migration is required for evidence, contracts, patterns, decisions, or runbooks — the folder is renamed in place by git mv.

---

For history before this rebrand, see [git log](https://github.com/tanphuc16797/workspace-wiki/commits/main).
