# SKILL: Performance Profiling

**Trigger:** Tier 2 Flag (Complexity > 10) or Tier 1 Regression.
**Context:** This skill provides the *how*. The *why* is in `AGENTS.md`.

## 1. The Micro-Lens (Tier 2 Check)
Use this when logic is complex but not necessarily a loop hotspot.

```bash
# Run the wrapper (Auto-launches SnakeViz)
python promptkit/skills/performance/profile.py src/my_complex_logic.py
```

## 2. The Tripwire Check (Tier 1 Check)
Use this to verify you haven't broken the build.

```bash
# Must pass before commit
make bench
```
