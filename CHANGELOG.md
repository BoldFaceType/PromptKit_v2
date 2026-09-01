# Changelog

## [2.1.0] - 2026-08-30

### Skills
* **DevOps Guide — Consolidation + New Rules:** Merged the drifted working copy
  (`C:\Dev\DevOps Guide v2.0.7.md`) back into the canonical repo path. The guide is now
  fanned out by `scripts/sync_agents.py` instead of being hand-copied, so the four
  divergent copies collapse to one source of truth.
  * **Rule 1A (Prime Agent WSL2 exception)** and the **Codex bash-shim example** merged in
    from the working copy — both had been absent from the canonical file since 2026-06-26,
    meaning every agent following the Constitution's DevOps link read a ruleset unaware of
    the only sanctioned Rule 1 exception.
  * **New Rule 8 — Python CLIs via `uvx`:** the Rule 1 analogue for Python; `uv tool
    install` limited to daily-driver tools.
  * **New Rule 9 — Every install states its reversal:** reversal table per install method.
    An install with no known reversal is not approved.
  * **Rule 1 honesty fix:** removed the incorrect "no version drift" claim. Unpinned `npx`
    floats to `latest`; added `@x.y.z` pinning guidance for load-bearing tools.
  * **Rule 2 elevation exception:** narrow, three-condition escape hatch for software that
    genuinely cannot install unelevated.
  * **Rule 3:** cache table extended to pnpm, uv, and mise.
  * **Rule 4:** explicit `_bin` (commands, on PATH) vs `_cache\installers` (install inputs)
    boundary; partial downloads banned. Prompted by a 1,692 MB `_bin` holding ~1.6 GB of
    installers and one abandoned `.crdownload`.
  * **Rule 5:** documented the `$PROFILE`-function limitation that makes shims necessary.
  * **Verification block rewritten:** real PASS/FAIL per check plus a failure summary. The
    previous version applied `-ForegroundColor Green` unconditionally, so a missing tool
    rendered as a pass. Added a Zero-Global-Installs assertion.

### Sync
* **`sync_agents.py` is now multi-document.** Replaced the single `SOURCE`/`TARGETS` pair
  with a `DOCUMENTS` list of source→targets mappings. The DevOps Guide joins the
  Constitution as a synced document, fanning out to `C:\Dev\SKILL_DevOps_Guide.md` and
  `C:\Dev\projects\SKILL_DevOps_Guide.md`. Out-of-repo roots come from `$DEV_ROOT`
  (default `C:\Dev`).
* **Fixed: `.codex/config.toml` was silently invalid TOML from v2.0.5 (75e69dd) onward.**
  The sync injected an HTML comment header and Markdown prose into a TOML file, so it
  failed to parse at line 1. Removed from the target list — Codex reads `AGENTS.md` for
  instructions, which is already synced, and `config.toml` is for settings. No settings
  were lost; the file had never held any. It is now a valid comments-only TOML file.
* **Guard added:** `sync_agents.py` refuses any non-Markdown target rather than emitting
  a file the consuming tool cannot parse. This is the check that would have caught the
  `.codex/config.toml` corruption at the point it was introduced.
* **`--dry-run` flag** reports which targets would change without writing, and the script
  now exits non-zero on failure.

### Governance
* **Single canonical copy:** `promptkit/skills/devops/SKILL_DevOps_Guide.md` declared
  authoritative in the document header; the version-named `C:\Dev\DevOps Guide v2.0.7.md`
  retired to a redirect stub, since a version in a filename defeats SSoT.
* **Metadata block added:** version, supersedes, canonical path, owner, last-reviewed, and
  a quarterly review cadence.
* **Session metadata removed** from the normative ruleset; provenance lives here instead.
  Codex shim added and verified 2026-08-30 (session `01ELekPFaiX4sHFcpitBTunW`).

## [2.0.7] - 2026-06-14

### Skills
* **DevOps Guide — Two-Layer Split:** Restructured `SKILL_DevOps_Guide.md` into **Section 1 (General Install Rules, always apply)** and **Section 2 (Worked Examples, initial setup only)**. Clarifies that the guide is a general install ruleset; named software is illustrative, not scope.
  * Stated universal rules once: npx-for-Node-CLIs, user-space installs, default caches, `_bin` scope, reusable alias pattern, verify-after-install, prerequisites-first.
  * Removed framing that implied rules were tool-specific (e.g. "npx pattern" repeated per-tool, "Why User Installer?" buried under VS Code, cache location under Gemini, closed-roster decision tree/checklist).
  * Added `opencode` (`npx --yes opencode-ai`) to the alias examples.

### Governance
* **Compact Constitution:** Compressed `promptkit/AGENTS.md` around KISS, Rule of One, VCR, VSA, Q2 priorities, RepoReady, and current tool targets.
* **RepoReady:** Added Task Manifests and removed the broad `documented` requirement.
* **Tool Focus:** Removed Gemini CLI and OpenWebUI from the Optimize For list.

### Sync
* **Generated Agent Files:** Synced generated agent targets from `promptkit/AGENTS.md`.

## [2.0.6] - 2026-05-04

### Governance
* **Dirty Worktree SOP:** Added mandatory preflight, unattended-agent isolation, merge gate, and recovery rules to `AGENTS.md`.

## [2.0.5] - 2026-03-28

### Skills
* **DevOps Guide:** Added `SKILL_DevOps_Guide.md` (AI Development Tools Installation Guide for Windows 11, following DevOps Guide v2.0.2).
* **Reference Link:** Added lazy-load link in `AGENTS.md` Section 5.

### Sync
* **Global Claude Config:** Updated `sync_agents.py` to inject constitution into `~/.claude/CLAUDE.md` (Claude Code global context).

## [2.0.4] - 2026-02-05

### Session Shutdown
* **Memory Update:** Initialized `CHILL_LOOP_CANVAS.md` via Session Shutdown Protocol.
* **Agent Finalization:** Finalized roster (OpenCode, Codex, Theia, CoPilot) and verified deployment mechanics.

## [2.0.3] - 2026-02-05

### Automation
* **GitHub Action:** Added `sync_constitution.yml` to enable **Remote Governance**. The repo is now the SSoT; pushes to `main` auto-update agent config files.

### Documentation
* **FAQ & How-To:** Integrated core system documentation into `README.md` for better developer onboarding.

## [2.0.2] - 2026-02-05

### Governance
* **Session Shutdown Protocol:** Added Section 6 to `AGENTS.md`.
  * **Rule:** Agents MUST update `knowledge/active/*.md` and `CHANGELOG.md` when the user signals "finish" or "deploy".
  * **Benefit:** Ensures persistent memory is self-maintaining without external scripts.

## [2.0.1] - 2026-02-05

### Deployment
* **Injection Strategy:** Updated `sync_agents.py` to use **Content Injection** (Transclusion).
* **Lazy Loading:** Implemented Wiki-style Hyperlinks in `AGENTS.md`.

## [2.0.0] - 2026-01-31

### Architecture
* **Paradigm Shift:** Moved from OOP to Data-Oriented Design (SoA) for all Tier 1 Hot Paths.
* **Vercel Pivot:** Governance rules moved from `SKILLS.md` to `AGENTS.md` (Context-First).
