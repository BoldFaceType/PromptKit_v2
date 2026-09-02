# Session Log

Per-session decisions and technical debt (Shutdown Protocol, `AGENTS.md` §6).
Distinct from `CHANGELOG.md`, which records shipped code only.

## Session Shutdown - 2026-02-05 (PromptKit v2.0.2 Deployment)

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

---
*Updated via Session Shutdown Protocol.*

## Session Shutdown - 2026-06-27

### Decisions Made
1.  **Sync Script Verified:** Ran `scripts/sync_agents.py` twice; confirmed it correctly injects `promptkit/AGENTS.md` into all repo-local targets (no diffs, already in sync with HEAD).
2.  **Global Target Confirmed Intentional:** Confirmed the `~/.claude/CLAUDE.md` target (added in `75e69dd`, v2.0.5) is a deliberate feature, not drift or injection — verified via `git log -p`.

### Technical Debt Added
1.  **Cross-Project Scope Risk:** `sync_agents.py` unconditionally overwrites the user's *global* `~/.claude/CLAUDE.md` with this repo's constitution. On a persistent (non-sandboxed) machine, this clobbers any global Claude Code instructions and leaks PromptKit_v2's rules into every other project's sessions. No backup/merge step exists before the overwrite. Consider gating the global write behind a flag or diffing before overwrite.

---
*Updated via Session Shutdown Protocol.*

## Session Shutdown - 2026-08-30

### Decisions Made
1.  **Codex Plugin Installed:** Installed the OpenAI Codex Claude Code plugin (`openai/codex-plugin-cc`) via `/plugin marketplace add` → `/plugin install` → `/reload-plugins` → `/codex:setup`.
2.  **Bash Shim, Not Global Install:** The plugin's setup script shells out to a literal `codex` binary and didn't see the existing `npx`-based `$PROFILE` alias. Fixed with a bash shim at `C:\Dev\_bin\codex` (`exec npx --yes @openai/codex "$@"`), preserving the DevOps Guide's Zero Global Installs rule instead of `npm install -g`.
3.  **DevOps Guide Updated:** Documented the shim pattern in `DevOps Guide v2.0.7.md` as a new Section 2 worked example, plus a clarifying note in the Rule 1A exceptions section (the shim is Rule-1-compliant, not an exception — kept distinct from the Prime Agent/WSL2 exception).
4.  **Full Command Verification:** Tested all 8 plugin commands (`setup`, `review`, `adversarial-review`, `status`, `result`, `cancel`, `transfer`, `rescue`) against real PromptKit_v2 working-tree state, read-only (no edits made to this repo).
5.  **Upstream Bugs Confirmed, Not Duplicated:** Found two real Windows/Git-Bash bugs (`cancel`'s `taskkill /PID` mangled by MSYS path conversion; `transfer`'s no-arg transcript auto-detection, plus Claude Code's own permission classifier blocking the `--source` workaround). Both already deeply tracked upstream — added confirming-repro comments to existing issues ([#525](https://github.com/openai/codex-plugin-cc/issues/525), [#514](https://github.com/openai/codex-plugin-cc/issues/514)) instead of filing duplicates.
6.  **Memory Saved:** Recorded the shim pattern, both bugs, and upstream links in `codex-plugin-setup.md` so future sessions don't rediscover them.

### Technical Debt Added
1.  **Cancel/Transfer Still Broken:** Both remain broken on Windows/Git Bash pending upstream fixes (#525, #469/#514) — not patched locally since it's plugin-owned code that would be overwritten on update.
2.  **Untrusted Project:** PromptKit_v2 is not yet a trusted project in `~/.codex/config.toml`, so project-local Codex hooks/exec policies stay disabled here.
3.  **Guide/Shim Outside Git:** `C:\Dev\DevOps Guide v2.0.7.md` and the new `C:\Dev\_bin\codex` shim live outside any git repository — this session's edits there have no commit/diff history.

---
*Updated via Session Shutdown Protocol.*

## Session Shutdown - 2026-09-01

Five PRs merged (#3–#7). DevOps Guide v2.0.7 → v2.1.2; sync fan-out 7 → 12 targets.

### Decisions Made
1.  **DevOps Guide consolidated to a single SSoT.** Found the guide forked four ways on disk — and the copy the Constitution's own DevOps link pointed at was 3,407 bytes stale, missing Rule 1A and the Codex shim example entirely, so every agent following that link read a ruleset unaware of the only sanctioned Rule 1 exception. Canonical is now `promptkit/skills/devops/SKILL_DevOps_Guide.md`; strays became redirect stubs or generated copies. **Resolves last session's debt item #3** (guide now lives in git; the `_bin\codex` shim still does not).
2.  **Fixed `.codex/config.toml` — silently invalid TOML since v2.0.5 (75e69dd).** `sync_agents.py` had been injecting an HTML comment header plus Markdown prose into a TOML file, so it failed to parse at line 1 for ~5 months. Removed from targets (Codex reads `AGENTS.md` for instructions anyway); added a `check_target()` guard that refuses any non-Markdown target, so this class of corruption can't recur silently.
3.  **`sync_agents.py` generalized to multi-document.** Single `SOURCE`/`TARGETS` pair → a `DOCUMENTS` list of source→targets mappings, plus `--dry-run`, non-zero exit on failure, and `@args` forwarding in the `.ps1` wrapper (which had been silently ignoring `--dry-run` and doing real writes).
4.  **Canonical sync targets set to Claude, Codex, OpenCode, Prime Agent.** Each wired to its own verified native global path (`~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md`, `~/.config/opencode/AGENTS.md`, `~/.prime/agent/AGENTS.md`), plus a tool-agnostic `~/AGENTS.md` home-root copy. All paths confirmed via Context7 + primary-source docs before adding — which is what caught OpenCode's move from `sst/opencode` to `anomalyco/opencode`.
5.  **New Constitution Rule 11 — Documentation Verification.** Formalizes the discipline the above depended on: check Context7 against assumptions first, when available.
6.  **Guide hardened with new rules.** Rule 8 (`uvx` for Python CLIs), Rule 9 (every install states its reversal), Rule 2 elevation exception, honest `npx` version-drift framing, `_bin` vs `_cache` boundary, and a verification block that can actually fail — the previous one printed green unconditionally, so a missing tool rendered as a pass.
7.  **`marimo-team/skills` installed** to Claude Code, Codex, and OpenCode (10 skills). Codex pickup confirmed working by user at session end.
8.  **Session gotchas recorded durably.** Five installer gotchas into the guide's Troubleshooting; four environment/workflow ones into `windows-agent-workflow-gotchas.md` memory — split by scope so the Install Ruleset stays about installs.

### Technical Debt Added
1.  **Marimo sync gap (deliberate).** Marimo's AI assistant has no AGENTS.md equivalent — instructions live in `marimo.toml`'s `[ai].rules` string, alongside real settings a blind overwrite would destroy. Syncing it needs a TOML-aware merge (`tomlkit`, not currently a dependency). Documented inline in `sync_agents.py`; not implemented.
2.  **Gemini CLI gap (deliberate).** `~/.gemini/GEMINI.md` is Gemini's own auto-accumulated memory log (44 KB of real session history), not a static instructions file — excluded from sync so it isn't clobbered. Gemini only receives the Constitution at project level via `.gemini/GEMINI.md`.
3.  **Data loss: `C:\Dev\notes\DevOps Guide v2.0.3.md`.** Overwritten in place with a redirect stub before checking its hard-link count; it shared an inode with a Claude Desktop upload cache file, so the original v2.0.3 content is gone from both names and is not recoverable. Superseded content, low consequence — but the cause is now Rule-documented under Troubleshooting.
4.  **`~/.qwen/skills/` left empty.** Pre-existing directory (2026-07-04) that a botched skills install polluted; the 10 unwanted folders were removed surgically, leaving the directory itself empty rather than restored to a prior state.
5.  **`~/.agents/.skill-lock.json` inconsistency (pre-existing).** Lists a `microsoft-foundry` skill that isn't present on disk. Not caused this session and not touched, since editing it risked the real `superpowers` entry alongside it.
6.  **CRLF churn on every sync.** Each `sync_agents.py` run dirties five generated Constitution targets with CRLF-only diffs that carry no content change, adding noise to every commit. A `.gitattributes` `eol` rule would settle it.
7.  **`_bin` hygiene not actioned.** Rule 4 now explicitly bans installers and partial downloads in `C:\Dev\_bin`, but the directory still holds ~1.6 GB of them plus one abandoned `.crdownload` — the rule was written, the cleanup wasn't done.
8.  **Global-config overwrite risk (carried forward from 2026-06-27, now larger).** That session flagged `sync_agents.py` unconditionally overwriting the user's global `~/.claude/CLAUDE.md` with no backup or merge step. Still true, and the blast radius grew this session: the script now also overwrites `~/.codex/AGENTS.md`, `~/.config/opencode/AGENTS.md`, `~/.prime/agent/AGENTS.md`, and `~/AGENTS.md`. One of those (`~/.config/opencode/AGENTS.md`) did in fact replace pre-existing hand-written content this session. Mitigations exist but are partial — `--dry-run` shows what would change, and `check_target()` blocks non-Markdown targets — neither backs anything up. Gating global writes behind a flag, or diffing before overwrite, remains unimplemented.
