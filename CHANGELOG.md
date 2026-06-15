# Changelog

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
