# DevOps Guide — Install Ruleset
**Windows 11 — Following DevOps Guide v2.0.2**

**Guide Version:** 2.0.0
**Prerequisites:** DevOps Guide v2.0.2 environment must be installed

> **How to read this document.**
> **Section 1 (General Install Rules)** is the authoritative ruleset and applies to **every** install — present and future.
> **Section 2 (Worked Examples)** is initial-setup scaffolding that *demonstrates* the rules on specific software. The named tools (VS Code, Gemini CLI, Jules, etc.) are **examples only, not a required or exhaustive roster**. When installing anything new, apply Section 1; reach for Section 2 only as a pattern reference.

---

# Section 1 — General Install Rules (always apply)

These rules govern all installs regardless of the software involved.

### Core Principles
- **Rule of One:** Each tool solves ONE problem with no overlap.
- **VCR (Value-Complexity Ratio):** High value, minimal complexity.
- **KISS:** The simplest solution is the default.
- **Zero Global Installs:** No `npm install -g`. No machine-wide mutation when a user-space option exists.

### Rule 1 — Node.js CLI tools run via `npx` (no global install)
Any Node.js command-line tool is run on-demand with `npx`; it is **never** installed globally. The package is downloaded once and cached automatically.

```powershell
# Canonical pattern — substitute any Node CLI package
npx --yes <package> [args]
```

- First run downloads + caches (30–60s). Subsequent runs are instant.
- No version drift, no global `node_modules`, nothing to uninstall.

### Rule 2 — Desktop apps and native binaries install to user space
GUI apps and standalone binaries install **per-user**, never machine-wide:
- Prefer a **user installer** (e.g. `winget` user scope) or a vendor installer that targets `%LOCALAPPDATA%`.
- No admin elevation. Auto-updates without admin. Cleaner PATH management.
- **Default location:** `%LOCALAPPDATA%\Programs\<App>` (or the vendor's user-space dir, e.g. `~\.<tool>\bin`).

### Rule 3 — Use default cache locations
Let package managers use their default caches; do not relocate them without cause.
- npx / npm cache: `%LOCALAPPDATA%\npm-cache`
- This rule is universal — it is **not** specific to any one tool.

### Rule 4 — `_bin` is for executables, not packages
`C:\Dev\_bin\` holds custom executables and compiled binaries (`.exe`, `.bat`, `.ps1`) — **never** Node.js packages. Node CLIs use Rule 1 (npx).

### Rule 5 — Optional alias wrappers (reusable pattern)
To drop the `npx` prefix, wrap any Node CLI in a PowerShell function in `$PROFILE`. This is a **pattern**, not a fixed list — add an entry for each tool you actually use:

```powershell
# General alias pattern — one line per Node CLI you use
function <name> { npx --yes <package> $args }
```

Reload after editing: `. $PROFILE`

### Rule 6 — Verify after every install
Every install ends with a verification step (`--version`, a smoke command, or launching the app). An install is not "done" until verified.

### Rule 7 — Check prerequisites first
Before installing anything, confirm the base environment is present (see checklist below). If a prerequisite is missing, resolve it before proceeding.

### Package Management Responsibilities
Each tool owns ONE job — no overlap:

| Tool | Purpose | Use When |
|---|---|---|
| **mise** | Runtime version management | Need different Node/Python versions per project |
| **uv** | Python package management | Installing Python packages |
| **pnpm** | Node.js project dependencies | Adding packages to a project |
| **npx** | Ephemeral CLI execution | Running a Node CLI tool (Rule 1) |

### Prerequisites Verification
```powershell
Write-Host "`n=== DevOps Environment Check ===" -ForegroundColor Cyan
Write-Host "uv: $(uv --version)" -ForegroundColor Green
Write-Host "mise: $(mise --version)" -ForegroundColor Green
Write-Host "node: $(node --version)" -ForegroundColor Green
Write-Host "npm: $(npm --version)" -ForegroundColor Green
Write-Host "pnpm: $(pnpm --version)" -ForegroundColor Green
Write-Host "git: $(git --version)" -ForegroundColor Green
Write-Host "docker: $(docker --version)" -ForegroundColor Green

# Directory structure
Test-Path C:\Dev\projects
Test-Path C:\Dev\_bin
Test-Path C:\Dev\_templates
```

All checks should succeed before any install. If any fail, complete DevOps Guide v2.0.2 setup first.

---

# Section 2 — Worked Examples (initial setup only)

> **These are examples that demonstrate Section 1 — not a required or exhaustive list.** They reflect the initial-setup roster; treat them as patterns to copy when installing comparable software.

## Example: Node CLI via npx (Rule 1) — Gemini CLI / Jules / GenKit

All three are Node CLI tools, so all three follow Rule 1 identically — there is nothing tool-specific about the pattern:

```powershell
# No install. Run on-demand; cached automatically.
npx @google/gemini-cli --version      # interactive Gemini assistant
npx @google/jules --version           # async coding agent (auth via Google + GitHub)
npx genkit --version                  # AI app framework CLI
```

Authentication, where required, happens on first interactive run (browser flow). Project dependencies (e.g. `genkit`, `@genkit-ai/google-genai`) are added per-project with `pnpm add`, not globally.

**Alias examples (Rule 5)** — add to `$PROFILE` only for tools you use:
```powershell
function gemini   { npx --yes @google/gemini-cli $args }
function jules    { npx --yes @google/jules $args }
function genkit   { npx --yes genkit $args }
function opencode { npx --yes opencode-ai $args }
```

## Example: Desktop app via user installer (Rule 2) — VS Code

```powershell
# winget user scope — no admin, auto-updates
winget install Microsoft.VisualStudioCode
code --version
where.exe code      # resolves under %LOCALAPPDATA%\Programs\Microsoft VS Code\bin
```

Installs to `%LOCALAPPDATA%\Programs\Microsoft VS Code` per Rule 2. Extensions are installed with `code --install-extension <id>` as needed.

## Example: Desktop app via vendor installer (Rule 2) — Claude Desktop

Download the Windows `.exe` from https://claude.ai/download and run it; it installs to `%LOCALAPPDATA%\Programs\Claude` (user space, Rule 2). Per-user config lives at `%APPDATA%\Claude\claude_desktop_config.json`.

## Example: Infrastructure feature toggle — Docker MCP Toolkit

Some capabilities are feature toggles rather than installs. Docker Desktop → Settings → Beta features → enable **Docker MCP Toolkit** → Apply & Restart. Connect a client with `docker mcp client connect <client> --global` and manage servers with `docker mcp server add|list`.

---

## Verification (example checklist)

> Adjust to whatever you actually installed — this is illustrative, not a definition of "complete."

```powershell
Write-Host "`n=== Install Verification (example) ===" -ForegroundColor Cyan
# Node CLIs (Rule 1) — only check the ones you use
try { Write-Host "Gemini: $(npx --yes @google/gemini-cli --version 2>&1)" } catch {}
# Desktop apps (Rule 2)
try { Write-Host "VS Code: $(code --version | Select-Object -First 1)" } catch {}
```

## Troubleshooting (general)

- **A `code`/CLI command isn't found:** the user-space `bin` dir isn't on PATH. Add it (e.g. `$env:PATH = "$env:LOCALAPPDATA\Programs\Microsoft VS Code\bin;$env:PATH"`) and re-test.
- **npx is slow on first run:** expected — Rule 1 caches on first use; later runs are instant.
- **Auth/browser flow fails:** disable VPN split-tunneling, try another browser, confirm a personal (not workspace) account.
- **A tool needs admin:** stop — it violates Rule 2. Find the user-scope installer or a portable/`npx` equivalent.

---

**Everything above resolves to Section 1.** When in doubt, the rules win; the examples are only illustrations of them.
