# Chill Loop Canvas (Active Project)

## Project: PromptKit v2.0.2 Deployment
**Status:** Completed (2026-02-05)

### Decisions Made
1.  **Deployment Path:** Isolated version 2.0.2 in `C:\Dev\projects\PromptKit_v2` to preserve version 0.1.0.
2.  **SSoT Strategy:** Implemented "Remote Governance" via GitHub Actions. The repo is now the master source; `git pull` updates the local "brains."
3.  **Agent Roster:** Swapped **Cursor** for **OpenCode**, **Codex CLI**, **Theia AI**, and **GitHub Copilot CLI** based on verified configuration paths.
4.  **Sync Mechanism:** Verified that the local `sync_agents.py` correctly scaffolds directories and injects rules.
5.  **Reference Memory:** DevOps Guide v2.0.2 location saved as `C:\Dev\notes\DevOps Guide v2.0.2.md`.

### Technical Debt Added
1.  **Binary Bloat:** Committing auto-generated agent config files (`CLAUDE.md`, etc.) to the repository. This is intentional for SSoT but may cause minor noise in Git diffs.
2.  **Path Dependencies:** Agent paths are assumed to be project-relative. If tools require global paths, the sync script will need expansion.
3.  **Python Requirement:** Syncing requires a local Python 3.12+ environment.

---
*Updated via Session Shutdown Protocol.*

## Session Shutdown - 2026-06-13

### Decisions Made
1.  **Compact Constitution:** Rewrote `promptkit/AGENTS.md` into a compact operating constitution around KISS, Rule of One, VCR, VSA, Q2 priorities, RepoReady, and current tool targets.
2.  **RepoReady Scope:** Added Task Manifests and removed the broad `documented` requirement from the compact RepoReady definition.
3.  **Tool Focus:** Dropped Gemini CLI and OpenWebUI from the Optimize For list; retained Claude Code, Codex, LM Studio/Ollama, GitHub, Linear, Google Workspace, local inference, automation, APIs/CLIs, and AI-103 blocks.
4.  **Generated Sync:** Ran `scripts/sync_agents.py` so generated agent files match the source constitution.

### Technical Debt Added
1.  **Generated Diff Noise:** Sync updated multiple generated agent config files and produced CRLF-to-LF normalization warnings.
2.  **Sync Script Drift:** `sync_agents.py` still targets `.gemini/GEMINI.md` even though Gemini CLI was removed from the Optimize For list.
3.  **README Drift:** README still contains older positioning around Gemini/Cursor-era tooling and may need a compact refresh.
