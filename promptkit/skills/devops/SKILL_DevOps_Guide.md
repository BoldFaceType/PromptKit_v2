# AI Development Tools Installation Guide
**Windows 11 — Following DevOps Guide v2.0.2**

**Date:** October 13, 2025
**Guide Version:** 1.0.0
**Prerequisites:** DevOps Guide v2.0.2 environment must be installed

---

## Table of Contents

1. [Prerequisites Verification](#prerequisites-verification)
2. [VS Code Installation](#vs-code-installation)
3. [Claude Desktop Installation](#claude-desktop-installation)
4. [Docker MCP Toolkit Setup](#docker-mcp-toolkit-setup)
5. [Gemini CLI Setup](#gemini-cli-setup)
6. [GenKit Setup](#genkit-setup)
7. [Jules Tools Setup](#jules-tools-setup)
8. [PowerShell Aliases Configuration](#powershell-aliases-configuration)
9. [Complete Verification](#complete-verification)

---

## Prerequisites Verification

Before installing AI tools, verify your DevOps Guide v2.0.2 environment is ready.

### Run Environment Check

Open PowerShell and run:

```powershell
Write-Host "`n=== DevOps Environment Check ===" -ForegroundColor Cyan
Write-Host "uv: $(uv --version)" -ForegroundColor Green
Write-Host "mise: $(mise --version)" -ForegroundColor Green
Write-Host "node: $(node --version)" -ForegroundColor Green
Write-Host "npm: $(npm --version)" -ForegroundColor Green
Write-Host "pnpm: $(pnpm --version)" -ForegroundColor Green
Write-Host "git: $(git --version)" -ForegroundColor Green
Write-Host "docker: $(docker --version)" -ForegroundColor Green
```

**Expected Output:**

```
=== DevOps Environment Check ===
uv: uv 0.9.2 (141369ce7 2025-10-10)
mise: 2025.10.7 windows-x64 (2025-10-10)
node: v22.20.0
npm: 10.9.3
pnpm: 10.18.2
git: git version 2.51.0.windows.2
docker: Docker version XX.XX.X, build XXXXXXX
```

### Verify Directory Structure

```powershell
Test-Path C:\Dev\projects
Test-Path C:\Dev\_bin
Test-Path C:\Dev\_templates
```

All should return `True`.

**If any checks fail, complete DevOps Guide v2.0.2 setup before proceeding.**

---

## VS Code Installation

### What It Is

Visual Studio Code — Modern code editor with AI assistant integration capabilities.

### Installation Method: Winget (Recommended)

```powershell
# Install VS Code User Installer (auto-updates without admin)
winget install Microsoft.VisualStudioCode

# Verify installation
code --version
where code
```

**Expected Output:**

```
1.XX.X
<commit hash>
x64
C:\Users\jerem\AppData\Local\Programs\Microsoft VS Code\bin\code
```

### Why User Installer?

- Auto-updates without admin privileges
- Cleaner PATH management
- Follows DevOps Guide principle (tools in user space)

**Installation Location:** `%LOCALAPPDATA%\Programs\Microsoft VS Code`

### Essential Extensions

```powershell
# Python development
code --install-extension ms-python.python

# GitHub Copilot (requires subscription)
code --install-extension GitHub.copilot

# WSL integration
code --install-extension ms-vscode-remote.remote-wsl

# Docker support
code --install-extension ms-azuretools.vscode-docker
```

### Verification

```powershell
cd C:\Dev\projects
mkdir vscode-test
cd vscode-test
code .
```

VS Code should open in your test directory.

---

## Claude Desktop Installation

### What It Is

Desktop application for Claude AI — connects to MCP servers for enhanced capabilities.

### Download and Install

1. Visit: https://claude.ai/download
2. Click "Windows" button, download the `.exe` installer
3. Run the installer, follow wizard (default settings)
4. Launch Claude Desktop when complete

**Installation Location:** `%LOCALAPPDATA%\Programs\Claude`

### Configuration Directory Setup

```powershell
# Create config directory if it doesn't exist
New-Item -ItemType Directory -Path "$env:APPDATA\Claude" -Force

# Verify creation
Test-Path "$env:APPDATA\Claude"
```

**Expected Output:** `True`

**Config File Location:** `%APPDATA%\Claude\claude_desktop_config.json`

*Note: Configure MCP servers after Docker MCP Toolkit setup.*

### Verification

1. Launch Claude Desktop from Start Menu
2. Sign in with your Anthropic account
3. Verify Claude responds to: "Hello, Claude!"

---

## Docker MCP Toolkit Setup

### What It Is

Docker Desktop feature that manages MCP servers in containers — provides secure, isolated tool execution for AI assistants.

### Prerequisites Check

```powershell
docker --version
docker ps
```

**Expected:** Docker version displays, `docker ps` shows running containers (or empty table).

### Enable MCP Toolkit

1. Open Docker Desktop
2. Settings (gear icon) → Beta features
3. Find "Enable Docker MCP Toolkit" → Toggle ON
4. Click "Apply & Restart"
5. Wait 30–60 seconds for restart

### Verify MCP Toolkit

After restart, look for "MCP Toolkit" tab in Docker Desktop left sidebar. You should see tabs: **Catalog**, **Servers**, **Clients**, **OAuth**.

### Connect Claude Desktop to Docker MCP Toolkit

```powershell
# Connect Claude Desktop as an MCP client
docker mcp client connect claude-desktop --global

# Verify connection was created
Get-Content "$env:APPDATA\Claude\claude_desktop_config.json"
```

**Expected Output:**

```json
{
  "mcpServers": {
    "docker-mcp-gateway": {
      "command": "docker",
      "args": ["mcp", "gateway", "run"],
      "env": {}
    }
  }
}
```

### Install Example MCP Servers

**Via Docker Desktop UI:**

1. Docker Desktop → MCP Toolkit → Catalog tab
2. Search for "GitHub Official" → Click `+`
3. Configuration tab → Select "OAuth" → Click "Authorize"
4. Repeat for other servers (Playwright, Filesystem, etc.)

**Via CLI:**

```powershell
docker mcp catalog list
docker mcp server add github-official
docker mcp server list
```

### Test MCP Connection

1. Fully quit Claude Desktop (right-click taskbar icon → Quit)
2. Restart Claude Desktop
3. Look for hammer icon (🔨) in bottom-left of chat input
4. Click hammer icon → should show installed servers

---

## Gemini CLI Setup

### What It Is

Google's AI assistant for terminal — fast, interactive access to Gemini models from the command line.

### Installation Pattern: npx (Per DevOps Guide v2.0.2)

**No installation required.** Gemini CLI uses the npx pattern — runs on-demand, cached automatically.

### First Use

```powershell
# First run — downloads and caches the tool
npx @google/gemini-cli --version
```

Type `y` when prompted to install.

### Authentication Setup

```powershell
npx @google/gemini-cli
```

1. Select your preferred theme
2. Select "Login with Google" (free tier)
   - Gemini 2.5 Pro (1M token context)
   - 60 requests/minute, 1000 requests/day
3. Browser opens — sign in with personal Google account, grant permissions

### Test Commands

```powershell
cd C:\Dev\projects
npx @google/gemini-cli "What is the KISS principle in software development?"
npx @google/gemini-cli --help
```

### Cache Location

Automatically managed at: `%LOCALAPPDATA%\npm-cache`

---

## GenKit Setup

### What It Is

Google's open-source framework for building AI-powered applications — provides flows, prompts, and production monitoring.

### Installation Pattern: npx (Per DevOps Guide v2.0.2)

No global installation required. GenKit uses the npx pattern for CLI; project dependencies via pnpm.

### API Key Setup (One-Time)

Get your Gemini API key from: https://aistudio.google.com/app/apikey

```powershell
# Set for current session
$env:GEMINI_API_KEY = "your-api-key-here"

# Make permanent (User level)
[Environment]::SetEnvironmentVariable('GEMINI_API_KEY', 'your-api-key-here', 'User')

# Verify
echo $env:GEMINI_API_KEY
```

### Create Test Project

```powershell
cd C:\Dev\projects
mkdir genkit-test && cd genkit-test
pnpm init
pnpm add genkit @genkit-ai/google-genai
New-Item -ItemType File -Path server.js
```

**server.js:**

```js
const { genkit } = require('genkit');
const { googleAI, gemini20Flash } = require('@genkit-ai/google-genai');

const ai = genkit({ plugins: [googleAI()], model: gemini20Flash });

const greetFlow = ai.defineFlow(
  { name: 'greetFlow', inputSchema: { name: String }, outputSchema: String },
  async (input) => {
    const { text } = await ai.generate(`Say hello to ${input.name} in a creative way!`);
    return text;
  }
);

module.exports = { greetFlow };
```

### Test GenKit

```powershell
npx genkit start -- node server.js
```

Open browser to: http://localhost:4000 — click "greetFlow", run with `{ "name": "Jeremie" }`.

Press `Ctrl+C` to stop.

---

## Jules Tools Setup

### What It Is

Google's asynchronous coding agent CLI — delegates complex, multi-step coding tasks that run in cloud VMs.

### Installation Pattern: npx (Per DevOps Guide v2.0.2)

No installation required.

### First Use and Authentication

```powershell
npx @google/jules --version
```

Type `y` when prompted. Browser opens for Google + GitHub authentication.

### Test Commands

```powershell
npx @google/jules auth status
npx @google/jules --help

cd C:\Dev\projects
mkdir jules-test && cd jules-test
git init
npx @google/jules remote list --repo .
```

### Gemini CLI vs Jules Tools

| | Gemini CLI | Jules Tools |
|---|---|---|
| **Speed** | Real-time, interactive | Asynchronous, background |
| **Use for** | Quick questions, code review | Complex refactors, multi-step tasks |
| **Output** | Chat response | Pull Request |

---

## PowerShell Aliases Configuration

### Setup Instructions

**1. Open PowerShell Profile:**

```powershell
notepad $PROFILE
```

**2. Add Aliases (at end of file, after existing PATH config):**

```powershell
# CLI Tool Aliases (optional but recommended)
function gemini { npx --yes @google/gemini-cli $args }
function jules  { npx --yes @google/jules $args }
function genkit { npx --yes genkit $args }
```

**3. Reload Profile:**

```powershell
. $PROFILE
```

### Your Complete PowerShell Profile

```powershell
# Add mise shims to PATH
$env:PATH = "$env:LOCALAPPDATA\mise\shims;$env:PATH"

# Add Node.js bin directory to PATH
$nodePath = "$env:LOCALAPPDATA\mise\installs\node\22.20.0"
$env:PATH = "$nodePath;$env:PATH"

# CLI Tool Aliases (optional but recommended)
function gemini { npx --yes @google/gemini-cli $args }
function jules  { npx --yes @google/jules $args }
function genkit { npx --yes genkit $args }
```

---

## Complete Verification

### Full Environment Check

```powershell
Write-Host "`n=== Complete AI Tools Verification ===" -ForegroundColor Cyan

Write-Host "`nDesktop Applications:" -ForegroundColor Yellow
Write-Host "VS Code: $(code --version | Select-Object -First 1)" -ForegroundColor Green
Write-Host "Docker Desktop: $(docker --version)" -ForegroundColor Green

Write-Host "`nCLI Tools (via npx):" -ForegroundColor Yellow
try { Write-Host "Gemini CLI: $(gemini --version 2>&1)" -ForegroundColor Green }
catch { Write-Host "Gemini CLI: Use 'npx @google/gemini-cli' or configure aliases" -ForegroundColor Yellow }

try { Write-Host "Jules Tools: $(jules --version 2>&1)" -ForegroundColor Green }
catch { Write-Host "Jules Tools: Use 'npx @google/jules' or configure aliases" -ForegroundColor Yellow }

try { Write-Host "GenKit: $(genkit --version 2>&1)" -ForegroundColor Green }
catch { Write-Host "GenKit: Use 'npx genkit' or configure aliases" -ForegroundColor Yellow }

Write-Host "`nDocker MCP Toolkit:" -ForegroundColor Yellow
docker mcp catalog list | Select-Object -First 3
```

### Manual Verification Checklist

- [ ] VS Code launches successfully
- [ ] Claude Desktop responds to chat messages
- [ ] Claude Desktop shows hammer icon (🔨) after connecting to Docker MCP
- [ ] Docker Desktop shows "MCP Toolkit" tab
- [ ] Gemini CLI responds to prompts
- [ ] Jules Tools authenticates with GitHub
- [ ] GenKit Developer UI launches at localhost:4000
- [ ] PowerShell aliases work (if configured)

---

## Troubleshooting

### VS Code: Command Not Found

```powershell
$vscodePath = "$env:LOCALAPPDATA\Programs\Microsoft VS Code\bin"
$env:PATH = "$vscodePath;$env:PATH"
code --version
```

### Claude Desktop: No Hammer Icon

```powershell
Get-Content "$env:APPDATA\Claude\claude_desktop_config.json"
# Fully quit Claude Desktop (right-click taskbar → Quit), then restart
```

### Gemini CLI: Authentication Failed

1. Disable VPN split-tunneling (use global mode)
2. Try different browser
3. Clear browser cache and retry
4. Verify personal Google account (not workspace)

### Jules Tools: GitHub Authorization Failed

```powershell
gh auth status
gh auth login        # re-authenticate if needed
npx @google/jules auth status
```

### GenKit: API Key Not Found

```powershell
echo $env:GEMINI_API_KEY
[Environment]::SetEnvironmentVariable('GEMINI_API_KEY', 'your-api-key', 'User')
# Restart PowerShell and test
```

### Docker MCP Toolkit: Not Visible

1. Verify Docker Desktop version: Must be 4.42.0+
2. Settings → Beta features → Enable "Docker MCP Toolkit"
3. Apply & Restart, wait 1–2 minutes

### npx Commands Slow on First Run

**This is expected.** First run downloads and caches the package (30–60 seconds). Subsequent runs are instant.

---

## Tool Selection Decision Tree

```
Need an answer RIGHT NOW?
  → Gemini CLI (instant response)

Need to delegate a multi-step coding task?
  → Jules Tools (async, creates PR)

Need to build AI features INTO your app?
  → GenKit (framework for AI apps)

Need AI to access local files/GitHub/databases?
  → Claude Desktop + Docker MCP Toolkit

Need to write code yourself with AI help?
  → VS Code + GitHub Copilot
```

---

## Summary

| Category | Tool | Status |
|---|---|---|
| Desktop | VS Code | winget install |
| Desktop | Claude Desktop | .exe installer |
| CLI | Gemini CLI | npx (no install) |
| CLI | Jules Tools | npx (no install) |
| CLI | GenKit | npx (no install) |
| Infrastructure | Docker MCP Toolkit | Beta feature toggle |
| Convenience | PowerShell aliases | Optional |

**All following DevOps Guide principles: no global npm installs, npx pattern, KISS compliant.**
