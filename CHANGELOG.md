# Changelog

## [2.1.5] - 2026-09-02

### Governance
* **`CHILL_LOOP_CANVAS.md` renamed to `SESSION_LOG.md`.** The Shutdown
  Protocol's "Active Project" target had drifted into a pure decisions/debt
  ledger for PromptKit tooling work — five sessions' worth (2026-02-05 through
  2026-09-01), none of it actually about the Chill/Hybrid-Loop v2 project the
  file was named for — making it both a misnomer and hard to find. `git mv`
  preserves history; no redirect stub needed since the whole file body already
  was the decisions/debt log. Constitution §5/§6 (`promptkit/AGENTS.md`)
  repointed to `SESSION_LOG.md` and re-synced to all targets.
* **New Rule 12 — Sub-Agents:** `promptkit/AGENTS.md` now directs using
  sub-agents where appropriate for parallelizable research, exploration, or
  independent implementation slices, following the existing §7 safe
  concurrency pattern (main checkout for the primary task, worktrees for
  parallel implementation, read-only for research/review).

## [2.1.4] - 2026-09-01

### Skills
* **DevOps Guide v2.1.2 — new "Known gotchas" subsection under Troubleshooting.**
  Records installer behavior that contradicted its own documentation, each entry
  earned from real damage or a real near-miss:
  * **A scoping flag can be silently overridden by an `--all`-style flag.** `npx skills
    add -a claude-code -a codex -a opencode --all` ignored all three `-a` flags and
    installed to 77 agents, creating ~55 unwanted directories. Removing `--all` made
    `-a` work.
  * **An installer's success report is not evidence.** The same CLI printed
    `copy → Codex` while writing nothing to `~/.codex/skills/`. Rule 6 sharpened:
    verify the destination on disk, never the summary.
  * **Agent skill roots differ per tool**, and OpenCode reads three of them — so one
    install can satisfy two tools, and assumptions cannot transfer between agents.
    Paths verified 2026-09-01 against each tool's own docs.
  * **On Windows/NTFS an in-place write propagates through hard links** — Claude
    Desktop hard-links uploads into its session storage, so files can have invisible
    twins. Check `stat -c %h` before overwriting a file you did not create.
  * **Verify provenance per-item before bulk deletion, not by sample.** An audit of 51
    "obviously new" directories found two pre-existing with real user data.
  Placed under the existing `## Troubleshooting` rather than in a new parallel
  section — Troubleshooting already serves this role (Rule of One).

## [2.1.3] - 2026-09-01

### Governance
* **New Rule 11 — Documentation Verification:** `promptkit/AGENTS.md` now instructs
  always checking the Context7 tool against assumptions first, when available —
  formalizing the discipline already applied throughout the OpenCode/Prime Agent/
  Marimo sync-target research (confirming exact paths via Context7 + primary docs
  rather than asserting from training data, which is exactly what caught the
  `sst/opencode` → `anomalyco/opencode` org move).

## [2.1.2] - 2026-09-01

### Sync
* **Canonical sync targets now include OpenCode and Prime Agent.** Constitution
  document gains two new global targets: `~/.config/opencode/AGENTS.md` and
  `~/.prime/agent/AGENTS.md`. Both confirmed via Context7 + primary-source docs
  before adding — OpenCode's own docs (`opencode.ai/docs/rules/`) and Prime
  Agent's own repo (`github.com/PrimeIntellect-ai/prime-agent`) both explicitly
  document these exact paths as their native global instruction file.
* **`~/.config/opencode/AGENTS.md` pre-existing content replaced, not lost.** It
  held a manually-copied fragment of the Context7 rule (identical to
  `~/.claude/rules/context7.md`) — no unique content, since that source still
  exists unchanged. OpenCode's *behavior* does change: it now gets the full
  Constitution instead of just the Context7 instruction. Checked before writing,
  per the standing practice from the `~/.gemini/GEMINI.md` incident.
* **Noted, not implemented: OpenCode already had an undocumented-to-us fallback**
  to `~/.claude/CLAUDE.md` when no OpenCode-specific AGENTS.md exists (per its own
  source, `instruction-context.ts`). Added the explicit target anyway rather than
  depend on another tool's internal fallback chain as our sync mechanism.
* **Marimo researched, deliberately not added.** Its AI assistant has no
  AGENTS.md-equivalent — custom instructions live in `marimo.toml`'s `[ai].rules`
  string (TOML), alongside real settings a blind overwrite would destroy (same
  failure class as the `.codex/config.toml` corruption this guide already fixed
  once). Documented inline in `sync_agents.py`; would need a TOML-aware merge
  (e.g. via `tomlkit`) to do safely — a different, bigger feature than this
  script provides today.
* **AGENTS.md governance update:** the spec is now stewarded by the Agentic AI
  Foundation (AAIF) under the Linux Foundation as of 2026 (founding members
  include Anthropic, OpenAI, Google, Microsoft, AWS). Comment in
  `sync_agents.py` updated to reflect this — but the *technical* scope is
  unchanged: still no ratified global/user-home file location in the spec
  itself, project-root + nested-monorepo discovery only. The `~/AGENTS.md`
  home-root target from 2.1.1 is unaffected either way.

## [2.1.1] - 2026-09-01

### Sync
* **New global target: `~/AGENTS.md`.** The DevOps Guide document now also fans out to
  a home-root, tool-agnostic copy at `C:\Users\<you>\AGENTS.md` — literally named
  `AGENTS.md`, not tucked inside a Claude- or Codex-specific config directory. No
  coding-agent tool auto-scans a bare home-root `AGENTS.md` today (there is no
  ratified global `AGENTS.md` convention — see [agentsmd/agents.md#91](https://github.com/agentsmd/agents.md/issues/91),
  an open, unresolved proposal for `~/.config/agents/AGENTS.md`), so this is a
  deliberate, stable claim for whichever tools adopt one next, not a claim of
  guaranteed pickup today.
* **`~/.gemini/GEMINI.md` deliberately excluded, not overlooked.** Unlike every other
  global target, that path is Gemini CLI's own auto-accumulated memory log
  (`## Gemini Added Memories`) — Gemini appends to it itself; it is not a static
  instructions file. Adding it as a sync target would silently overwrite real session
  memory (44 KB of it, present) on every run. If Gemini needs the DevOps Guide
  pointer, it goes in through Gemini's own memory mechanism, not this script.
* **Confirmed, not new:** `~/.codex/AGENTS.md` (Codex's own global instructions file)
  already carried the install-governance pointer identically to `~/.claude/CLAUDE.md`
  — both are Constitution sync targets since 2.1.0. The gap this release closes is
  the DevOps Guide's own *content* reaching a tool-agnostic path directly, not a
  missing pointer.

### Skills
* **DevOps Guide v2.1.1:** header callout updated to enumerate all three generated
  copies (`C:\Dev\SKILL_DevOps_Guide.md`, `C:\Dev\projects\SKILL_DevOps_Guide.md`,
  `~/AGENTS.md`), so the document's own self-description stays accurate.

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
* **Install Governance:** Required agents to read `C:\Dev\DevOps Guide v2.0.7.md` and follow Section 1 before installing software.
* **GitHub Operations:** Required agents to use the authenticated `gh` CLI first for every GitHub operation.

### Sync
* **Generated Agent Files:** Synced generated agent targets from `promptkit/AGENTS.md`.
* **Global Codex Config:** Added `~/.codex/AGENTS.md` to the generated instruction targets.

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
