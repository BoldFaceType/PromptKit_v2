# PromptKit v2.0.2 (Data-Oriented Edition)

**Role:** Clinical AI Engineering Core
**Philosophy:** Rule of One | KISS | VCR
**Architecture:** Structure of Arrays (SoA) | Negative Space Programming

## The Vercel Pivot
We have shifted from "Skill-Based" governance to "Context-Based" governance.
* **Old Way:** Agents looked up skills to see if they should optimize. (53% Failure Rate).
* **New Way:** The "Rules of Physics" (SoA, Negative Space) are in `AGENTS.md`.
Compliance is mandatory and zero-shot.

## Quick Start

```bash
# 1. Install Dependencies
pip install -e .[dev]

# 2. Deploy Intelligence (Inject AGENTS.md content into Tools)
python scripts/sync_agents.py

# 3. Validate Quality (Lint + Complexity)
make check

# 4. Validate Performance (Tripwire)
make bench
```

## How-To Instructions

### Adding or Modifying Prompts
You modify the "Master Constitution" at **`promptkit/AGENTS.md`**.
*   **To Edit:** Open `AGENTS.md` and update the laws (Architecture, Decision Matrix, or Operational Context).
*   **To Add Skills:** Create a new Markdown file in `promptkit/skills/` and add a "Lazy Load" link to it in the `Reference Links` section of `AGENTS.md`.

### Manual Syncing
If you are working locally and want to push your Constitution changes to your local AI tools immediately:
```bash
python scripts/sync_agents.py
```

### Remote Governance (GitHub SSoT)
1. Edit `promptkit/AGENTS.md` on GitHub or push a local change.
2. The **GitHub Action** will automatically run the sync script and commit the updated `.gemini/GEMINI.md`, `CLAUDE.md`, and `.cursorrules` files.
3. Perform a `git pull` locally to update your local agent's "brain."

## FAQ

### What is PromptKit?
PromptKit is a "Constitution-as-Code" framework designed to enforce a **Data-Oriented Architecture (SoA)** and **Context-First Governance** across your AI development environment. It treats the **System Prompt** as a managed deployment artifact.

### Why is it called PromptKit?
It represents a **Toolkit** for managing **Prompts**. It provides the infrastructure to "kit" your prompts into portable, versioned artifacts that include the "Rules of Physics" for your codebase.

### How does it work?
The system utilizes "Enforcer" tools in the `Makefile` to reject complex code and regressive performance. It then uses the `sync_agents.py` script to **inject** the rules directly into the context window of your AI tools (Gemini, Claude, Cursor), ensuring they cannot hallucinate slow or complex patterns.

### How is versioning handled?
Versioning is managed via standard Git workflows and the **Session Shutdown Protocol**. Every change to the Constitution is benchmarked against "Tripwires" before it is considered RepoReady.

## The "Negative Space" Rule
We do not optimize by adding code. We optimize by removing barriers.
*   **Forbidden in Tier 1 Loops:** class, `__init__`, try/except, logging, I/O.
*   **Mandatory:** Structure of Arrays (SoA).