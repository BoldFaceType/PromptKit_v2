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

## The "Negative Space" Rule
We do not optimize by adding code. We optimize by removing barriers.
*   **Forbidden in Tier 1 Loops:** class, `__init__`, try/except, logging, I/O.
*   **Mandatory:** Structure of Arrays (SoA).
