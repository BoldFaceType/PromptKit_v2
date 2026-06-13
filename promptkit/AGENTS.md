# AGENTS.md Compact Constitution

## 1. Doctrine
KISS, Rule of One, VCR, and smallest viable slices. Ship deterministic, reusable, continuous work. Reject scope creep, extra tools/frameworks, over-engineering, context bloat, token-maxxing, and AI hype. New tools need replacement-level justification. Compress complexity, challenge assumptions, limit WIP. Health, sleep, CPAP, finances, and family are first-class dependencies.

## 2. 2026Q2 Priorities
Stabilize finances, improve sleep, pass AI-103 by 2026-06-30, finish P520/3090, PAOS/Obsidian-Claude PKB, and Chill/Hybrid-Loop v2. Treat as one system for behavior change, local-first AI ops, and Applied/Clinical AI Engineering.

## 3. RepoReady
Repos are reproducible, versioned, dated, agent-compatible, and handoff-ready: README, CHANGELOG, PRD, TDD, ADRs, Task Manifests, install/run docs, VSA boundaries, branch rules, ASCII/ASIC flow diagrams.

## 4. Optimize For
Marimo, Claude Code, Codex, LM Studio/Ollama, GitHub, Linear, Google Workspace, local inference, automation, APIs/CLIs, reusable infra, verification loops, learn-by-doing, long tasks, cron, AI-103 blocks.

## 5. Reference Links
* Active Project: [Chill Loop Canvas](...)
* Profiling: [Manual](promptkit/skills/performance/SKILL_Profiling.md)
* Git Board: [Manual](promptkit/skills/governance/SKILL_GitBoard.md)
* DevOps: [Guide](promptkit/skills/devops/SKILL_DevOps_Guide.md)

## 6. Shutdown
Trigger: "Done", "Wrap up", "Finish", or "Deploy". Before exit: append decisions/debt to Active Project; update CHANGELOG.md if code shipped; create conventional commit message.

## 7. Multi-Agent Board
For multiple agents or branches/worktrees, use `AGENT_BOARD.jsonl` and `manifest_slices.md`. Lifecycle: claim, start, heartbeat, block, handoff, merge, release. Defaults: 15m lease, 5m heartbeat, stale after 10m. One owner per slice; earliest lease wins; stale leases need `takeover`; no lease means invalid work. Before merge, pass board validation, syntax, and formatting.

## 8. Dirty Worktree SOP
Before unattended agents, branches/worktrees, or merge requests, run `git status --short`. If dirty: commit owned WIP to a temp branch, isolate user/unknown WIP, and remove generated noise only when safely reproducible. Unattended agents require a clean branch/worktree, one narrow task, expected test, and allowed file scope. Merge gate: status, checks run, changed files/risks, conventional commit or PR title. If diffs are broad/unclear, preserve branch and stop; recover by cherry-picking verified files into a clean branch.
