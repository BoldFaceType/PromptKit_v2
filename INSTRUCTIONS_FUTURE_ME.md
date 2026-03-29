# Handoff: PromptKit v2.0.5

**To:** Jeremie (Future)
**From:** Jeremie (Past)
**Date:** 2026-02-05

## The Vercel Pivot (Why we changed everything)
We realized that storing "Rules" in `SKILLS.md` was a trap. The agents ignored them.
We moved the **"Negative Space"** and **"SoA"** rules into `AGENTS.md` (System Context).
**Result:** The model sees "FORBIDDEN: class" *before* it writes code.

## Critical Workflows

1. **New Project Init:**
   * Clone this repo.
   * Run `python scripts/sync_agents.py`.
   * This **Injects** the brain into Gemini/Claude files.

2. **The Tripwire:**
   * Don't trust yourself. Don't trust the AI.
   * Run `make quality_gate` before every push.
   * If `make bench` fails, you used an Object in a Hot Path. Fix it.

3. **Governance:**
   * Edit `promptkit/AGENTS.md` to change the rules.
   * Do NOT edit `GEMINI.md` directly. It will be overwritten by the sync script.

## Operational Constraints
* **Hardware:** Still the i9/4090. SoA optimizations are tuned for this L2 cache size.
* **Vetting:** If you add a feature without removing two others, you failed the Rule of One.

**Status:** RepoReady.
**Action:** Deploy.
