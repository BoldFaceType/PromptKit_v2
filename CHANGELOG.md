# Changelog

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
