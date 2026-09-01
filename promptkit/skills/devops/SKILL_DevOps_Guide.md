# DevOps Guide — Install Ruleset

**Version:** 2.1.2
**Supersedes:** 2.1.1
**Canonical path:** `promptkit/skills/devops/SKILL_DevOps_Guide.md` (PromptKit_v2)
**Platform:** Windows 11 + Ubuntu WSL2
**Applies to:** every software install on this machine, present and future
**Prerequisites:** the base toolchain in *Prerequisites Verification* below — run it first
**Owner:** jtisby · **Last reviewed:** 2026-09-01 · **Review cadence:** quarterly

> **This file is the single source of truth.** Generated copies, all produced by
> `python scripts/sync_agents.py` and carrying an AUTO-GENERATED header, live at:
> `C:\Dev\SKILL_DevOps_Guide.md`, `C:\Dev\projects\SKILL_DevOps_Guide.md`, and
> `C:\Users\<you>\AGENTS.md` (the tool-agnostic home-root copy — no coding-agent tool
> auto-scans this path yet, since no global `AGENTS.md` convention is ratified as of
> this writing, but it's a stable, literally-named location for whichever tools adopt
> one next). Edit here, then run the sync. Never fork.

> **How to read this document.**
> **Section 1 (General Install Rules)** is the authoritative ruleset and applies to
> **every** install — present and future.
> **Section 2 (Worked Examples)** demonstrates the rules on specific software. The named
> tools are **examples only, not a required or exhaustive roster**. When installing
> anything new, apply Section 1; reach for Section 2 only as a pattern reference.

---

# Section 1 — General Install Rules (always apply)

### Core Principles
- **Rule of One:** Each tool solves ONE problem with no overlap.
- **VCR (Value-Complexity Ratio):** High value, minimal complexity.
- **KISS:** The simplest solution is the default.
- **Zero Global Installs:** No `npm install -g`. No machine-wide mutation when a
  user-space option exists.

### Rule 1 — Node.js CLI tools run via `npx` (no global install)
Any Node.js command-line tool is run on-demand with `npx`; it is **never** installed
globally.

```powershell
# Canonical pattern
npx --yes <package> [args]

# Load-bearing tools: pin the version
npx --yes <package>@<x.y.z> [args]
```

- First run downloads + caches (30–60s). Subsequent runs are instant.
- Nothing to uninstall; no global `node_modules` to go stale.
- **Tradeoff, stated honestly:** unpinned `npx` re-resolves `latest` whenever the cache
  turns over — it *floats* where a global install *pins*. You are trading version
  stability for zero maintenance burden. **Pin with `@x.y.z` for anything load-bearing**
  (build tooling, anything in CI, anything an agent invokes unattended).

### Rule 1A — Prime Agent WSL2 vendor-managed exception
Prime Agent is installed and operated **only inside the Ubuntu WSL2 distribution**, not
through native Windows, PowerShell, or `npx`.

- Install and activate `mise` in Ubuntu; use `mise use --global node@22` so Node and npm
  remain user-owned.
- The official installer may use `npm install -g` **only when `npm prefix -g` resolves
  beneath `~/.local/share/mise/`**. This is an explicit exception to Rule 1 because the
  vendor-managed CLI and updater live inside an isolated, per-user WSL runtime without
  `sudo` or machine-wide mutation.
- Installer: `curl -fsSL https://app.primeintellect.ai/prime-agent/install.sh | sh`
- Prepare the IPython runtime during installation; do not defer to first use.
- Verify: `prime-agent --version`, `command -v prime-agent`, `npm prefix -g`.
- Update with `prime-agent update` from Ubuntu. Do not maintain a native-Windows wrapper
  or parallel installation.

**This is the only sanctioned exception to Zero Global Installs.** It is scoped to an
isolated, per-user WSL2 runtime with no `sudo`. Do not confuse it with the shim pattern
in Section 2 — a shim is **not** an exception to Rule 1; it is a Rule 1-compliant
workaround for tools whose own scripts shell out to a literal binary name. If a future
installer asks for `npm install -g` outside the WSL2/mise condition above, it **does not
qualify** — reach for a shim (Rule 4 + Rule 5) first.

### Rule 2 — Desktop apps and native binaries install to user space
GUI apps and standalone binaries install **per-user**, never machine-wide:
- Prefer a **user installer** (`winget` user scope) or a vendor installer targeting
  `%LOCALAPPDATA%`.
- No admin elevation. Auto-updates without admin. Cleaner PATH management.
- **Default location:** `%LOCALAPPDATA%\Programs\<App>` (or the vendor's user-space dir).

**Elevation exception.** Some software legitimately cannot run unelevated — kernel
drivers, virtualization, system-level networking (e.g. Docker Desktop's WSL2 backend).
Admin is permitted **only** when: (a) no user-scope or portable equivalent exists, (b) the
elevation is one-time at install, not per-run, and (c) the reason is recorded in the
CHANGELOG entry for that install. Convenience is not a reason.

### Rule 3 — Use default cache locations
Let package managers use their default caches; do not relocate without cause.

| Manager | Default cache |
|---|---|
| npx / npm | `%LOCALAPPDATA%\npm-cache` |
| pnpm | `%LOCALAPPDATA%\pnpm-store` |
| uv | `%LOCALAPPDATA%\uv\cache` |
| mise | `%LOCALAPPDATA%\mise` |

Universal rule — not specific to any one tool. Verify with the manager's own
`cache dir` / `config get cache` command rather than assuming.

### Rule 4 — `_bin` is for executables you invoke, nothing else
`C:\Dev\_bin\` holds **custom executables, shims, and compiled binaries** you invoke by
name (`.exe`, `.bat`, `.ps1`, extensionless bash shims). It is **on PATH** — everything in
it is a command.

**Not in `_bin`:**
- **Node.js packages** — Rule 1 (npx).
- **Downloaded installers** (`*Setup*.exe`, `*Installer*.exe`, `*.msi`) — these are
  *inputs* to an install, not commands. They belong in `C:\Dev\_cache\installers\` and
  should be deleted once the install is verified per Rule 6.
- **Partial/abandoned downloads** (`*.crdownload`, `*.part`) — delete on sight.

> **Why this is explicit:** `_bin` drifts into a downloads folder because the browser
> default and PATH convenience collide. A PATH directory holding hundreds of MB of dead
> installers is a hygiene and audit problem. Audit with:
>
> ```powershell
> Get-ChildItem C:\Dev\_bin -File | Sort-Object Length -Descending |
>     Select-Object -First 10 Name, @{n='MB'; e={[int]($_.Length / 1MB)}}
> ```

### Rule 5 — Optional alias wrappers (reusable pattern)
To drop the `npx` prefix, wrap any Node CLI in a PowerShell function in `$PROFILE`. A
**pattern**, not a fixed list — add an entry per tool you actually use:

```powershell
function <name> { npx --yes <package> $args }
```

Reload: `. $PROFILE`

**Limitation — read this before debugging a "not found" error.** A `$PROFILE` function
exists only inside your interactive PowerShell session. Any tool that spawns a child
process (`spawnSync`, `execFile`, a Git Bash subshell) will **not** see it. For those, use
the shim pattern (Section 2), which is PATH-resolvable and therefore visible everywhere.

### Rule 6 — Verify after every install
Every install ends with a verification step (`--version`, a smoke command, or launching
the app). An install is not "done" until verified.

- Verify the **dependent tool**, not just the artifact. If you added a shim so tool X can
  find binary Y, confirm **X's own readiness check passes** — not merely that Y runs.
- Verification that cannot report failure is not verification. See the block below.

### Rule 7 — Check prerequisites first
Confirm the base environment before installing anything. If a prerequisite is missing,
resolve it before proceeding.

### Rule 8 — Python CLI tools run via `uvx` (Rule 1 for Python)
The direct analogue of Rule 1. Python command-line tools are run on demand; they are
**never** installed into the system or user site-packages.

```powershell
uvx <package> [args]           # ephemeral, cached
uvx <package>@<x.y.z> [args]   # pinned — same guidance as Rule 1
```

- `uv tool install <pkg>` is permitted **only** for a tool you invoke daily, and it stays
  inside uv's own user-space tool dir — never `pip install` outside a project venv.
- Project dependencies use `uv add` in the project venv, never a global install.

### Rule 9 — Every install states its reversal
Before installing, know how to remove it. Record the reversal alongside the install.

| Install method | Reversal |
|---|---|
| `npx` / `uvx` (Rule 1, 8) | Nothing to remove; clear cache if needed |
| `winget` (Rule 2) | `winget uninstall <id>` |
| Vendor `.exe` (Rule 2) | Settings → Apps, or vendor uninstaller |
| Shim (Rule 4) | Delete the file from `_bin` |
| `$PROFILE` alias (Rule 5) | Remove the function; `. $PROFILE` |
| `mise use --global` | `mise unuse <tool>@<ver>` |

An install with no known reversal is not approved. This is what keeps Rule of One
enforceable — you cannot retire an overlapping tool you don't know how to remove.

### Package Management Responsibilities
Each tool owns ONE job — no overlap:

| Tool | Purpose | Use When |
|---|---|---|
| **mise** | Runtime version management | Different Node/Python versions per project |
| **uv** | Python packages + venvs | Installing Python packages |
| **uvx** | Ephemeral Python CLI execution | Running a Python CLI tool (Rule 8) |
| **pnpm** | Node.js project dependencies | Adding packages to a project |
| **npx** | Ephemeral Node CLI execution | Running a Node CLI tool (Rule 1) |

### Prerequisites Verification

```powershell
$script:failed = @()

function Test-Tool {
    param([string]$Name, [string]$VersionArg = '--version')
    $cmd = Get-Command $Name -ErrorAction SilentlyContinue
    if (-not $cmd) {
        Write-Host ("  FAIL  {0,-8} not on PATH" -f $Name) -ForegroundColor Red
        $script:failed += $Name; return
    }
    $ver = (& $Name $VersionArg 2>&1 | Select-Object -First 1)
    Write-Host ("  PASS  {0,-8} {1}" -f $Name, $ver) -ForegroundColor Green
}

function Test-Dir {
    param([string]$Path)
    if (Test-Path $Path) {
        Write-Host ("  PASS  {0}" -f $Path) -ForegroundColor Green
    } else {
        Write-Host ("  FAIL  {0} missing" -f $Path) -ForegroundColor Red
        $script:failed += $Path
    }
}

Write-Host "`n=== DevOps Environment Check ===" -ForegroundColor Cyan
'uv','mise','node','npm','pnpm','git','docker' | ForEach-Object { Test-Tool $_ }

Write-Host "`n=== Directory Structure ===" -ForegroundColor Cyan
'C:\Dev\projects','C:\Dev\_bin','C:\Dev\_templates','C:\Dev\_cache' |
    ForEach-Object { Test-Dir $_ }

Write-Host "`n=== Zero Global Installs (Rule 1) ===" -ForegroundColor Cyan
$globals = @(npm ls -g --depth=0 2>$null |
    Select-String -Pattern '^[+`\\]--\s*(.+)$' |
    ForEach-Object { $_.Matches[0].Groups[1].Value.Trim() } |
    Where-Object { $_ -notmatch '^(npm|corepack)@' })
if ($globals.Count) {
    Write-Host ("  FAIL  unexpected global packages: {0}" -f ($globals -join ', ')) -ForegroundColor Red
    $script:failed += 'zero-global-installs'
} else {
    Write-Host "  PASS  only npm + corepack present" -ForegroundColor Green
}

if ($script:failed.Count) {
    Write-Host ("`nFAILED ({0}): {1}" -f $script:failed.Count, ($script:failed -join ', ')) -ForegroundColor Red
    Write-Host "Resolve the above before installing anything." -ForegroundColor Red
} else {
    Write-Host "`nAll checks passed." -ForegroundColor Green
}
```

---

# Section 2 — Worked Examples

> **Examples that demonstrate Section 1 — not a required or exhaustive list.**

## Example: Node CLI via npx (Rule 1) — Gemini CLI / Jules / GenKit

```powershell
npx @google/gemini-cli --version   # interactive Gemini assistant
npx @google/jules --version        # async coding agent (Google + GitHub auth)
npx genkit --version               # AI app framework CLI
```

Authentication happens on first interactive run (browser flow). Project dependencies are
added per-project with `pnpm add`, never globally.

**Alias examples (Rule 5)** — add to `$PROFILE` only for tools you use:

```powershell
function gemini   { npx --yes @google/gemini-cli $args }
function jules    { npx --yes @google/jules $args }
function genkit   { npx --yes genkit $args }
function opencode { npx --yes opencode-ai $args }
```

## Example: Bash-resolvable shim for direct-invoking tools (Rule 1 + Rule 4) — Codex CLI

Some setup/check scripts shell out to a literal binary name via `spawnSync`/`spawn`
instead of going through your interactive shell — so they never see a `$PROFILE` alias
(Rule 5). On Windows, when the tool resolves its shell from `process.env.SHELL` and
`SHELL` points at Git Bash, the fix is a thin bash-resolvable shim, not a global install:

```bash
# C:\Dev\_bin\codex — no extension, executable, findable on PATH by name
#!/usr/bin/env bash
exec npx --yes @openai/codex "$@"
```

```bash
# Git Bash needs the exec bit set once:
chmod +x "/c/Dev/_bin/codex"
```

- **Not** an exception to Rule 1 — no global install; `npx` still does the ephemeral
  fetch/cache on every call.
- It is Rule 4 (`_bin` holds executables) applied to a shim rather than a `.ps1`/`.bat`,
  so both PowerShell-native tools (Rule 5 alias) and bash-spawning tools (this shim) find
  the same underlying command under the name they expect.
- Verify per Rule 6: `which codex` resolves **and** the dependent tool's readiness check
  reports success. Do not stop at "the shim runs."
- **Origin:** the OpenAI Codex Claude Code plugin (`/codex:setup`) shelled to
  `codex --version` directly and reported "not found" despite a working
  `npx --yes @openai/codex` alias.

## Example: Desktop app via user installer (Rule 2) — VS Code

```powershell
winget install Microsoft.VisualStudioCode
code --version
where.exe code    # resolves under %LOCALAPPDATA%\Programs\Microsoft VS Code\bin
```

Extensions: `code --install-extension <id>`.
Reversal: `winget uninstall Microsoft.VisualStudioCode` (Rule 9).

## Example: Desktop app via vendor installer (Rule 2) — Claude Desktop

Download the Windows `.exe` from https://claude.ai/download; installs to
`%LOCALAPPDATA%\Programs\Claude`. Per-user config at
`%APPDATA%\Claude\claude_desktop_config.json`. Move the downloaded installer to
`C:\Dev\_cache\installers\` and delete it after verification (Rule 4).

## Example: Infrastructure feature toggle — Docker MCP Toolkit

Some capabilities are toggles, not installs. Docker Desktop → Settings → Beta features →
enable **Docker MCP Toolkit** → Apply & Restart. Connect a client with
`docker mcp client connect <client> --global`; manage servers with
`docker mcp server add|list`.

---

## Troubleshooting

- **A CLI isn't found in your terminal:** the user-space `bin` dir isn't on PATH. Add it
  and re-test.
- **A CLI isn't found *by another tool*, but works in your shell:** you have a Rule 5
  alias where you need a Rule 4 shim. The other tool spawned a child process that never
  loaded `$PROFILE`. See the Codex example.
- **A shim works in one shell but not another:** PATH is not inherited uniformly by
  spawned/non-interactive shells. Confirm with `command -v <name>` *inside the failing
  context*, not your interactive prompt.
- **npx is slow on first run:** expected — Rule 1 caches on first use.
- **A tool's version changed unexpectedly:** unpinned `npx`/`uvx` re-resolved `latest`.
  Pin it (Rule 1 / Rule 8).
- **Auth/browser flow fails:** disable VPN split-tunneling, try another browser, confirm a
  personal (not workspace) account.
- **A tool needs admin:** check Rule 2's elevation exception. If it does not qualify, stop
  and find the user-scope, portable, or `npx`/`uvx` equivalent.

### Known gotchas — installer behavior that contradicts its own docs

Each of these cost real damage or a real near-miss. They are recorded because the tool's
documentation and the tool's actual behavior disagreed.

- **A "scope" flag can be silently overridden by a "select-everything" flag.** `npx skills
  add ... -a claude-code -a codex -a opencode --all` ignored **all three** `-a` flags and
  installed to every one of its 77 registered agents — creating ~55 unwanted directories
  for tools not on this machine. Removing `--all` made `-a` work correctly.
  **Rule: never combine a scoping flag with an `--all`-style flag.** Run the narrowest
  form, and verify the target list in the output *before* trusting it.
- **An installer's success report is not evidence.** That same CLI printed
  `copy → Codex` while writing **nothing** to `~/.codex/skills/` — it had written only to
  a shared store. This is Rule 6 in its sharpest form: **verify the destination on disk,
  never the installer's summary.** `ls` the target path.
- **Agent skill/instruction roots differ per tool, and some read several.** Verified
  2026-09-01: Claude Code → `~/.claude/skills/`; Codex → `~/.codex/skills/` only
  (`$CODEX_HOME/skills`; its `.agents/skills` lookup is *repository*-level, not global);
  OpenCode → reads **three** global roots (`~/.config/opencode/skills/`, `~/.claude/skills/`,
  `~/.agents/skills/`), so a single install can satisfy two tools at once. Confirm the
  specific tool's own docs before installing — do not generalize from one agent to another.
- **On Windows/NTFS, an in-place write propagates through hard links.** `cat > file`
  (and any truncate-in-place write) rewrites the shared inode, so **every** name pointing
  at that data changes — there is no "original" left. Claude Desktop hard-links uploaded
  files into its own session storage, so an unremarkable file in a working folder can have
  an invisible twin. **Before overwriting any file you did not create, check
  `stat -c %h` — a link count above 1 means another path shares those exact bytes.**
- **Before deleting in bulk, verify provenance per-item, not by sample.** A cleanup of
  51 "obviously new" directories was audited item-by-item and two turned out to be
  pre-existing with real user data. Gate every bulk delete on a per-item assertion
  (creation date, expected contents) that *refuses* anything unexpected, rather than
  trusting a spot-check of a few.

---

**Everything above resolves to Section 1.** When in doubt, the rules win; the examples are
only illustrations of them.
