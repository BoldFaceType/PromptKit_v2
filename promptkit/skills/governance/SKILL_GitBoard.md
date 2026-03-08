# SKILL: Git-backed Board Governance

**Trigger:** Parallel agents, branch-per-slice workflows, or worktree orchestration.
**Context:** This skill defines the operational protocol for safe multi-agent concurrency.

## 1. Required Event Fields

Each JSONL event must include:

- `ts` (UTC ISO-8601)
- `agent`
- `branch`
- `slice`
- `event`
- `task`
- `status`

For `claim` and `takeover`, include:

- `lease_until`

## 2. Event Lifecycle

1. `claim`
2. `start`
3. `heartbeat` (every 5 minutes)
4. `block` (if blocked)
5. `handoff` (with commit/PR)
6. `merge` (integrator event)
7. `release`

## 3. Timing Defaults

- Lease: 15 minutes
- Heartbeat: 5 minutes
- Stale timeout: 10 minutes

## 4. Conflict Resolution

- One active owner per slice.
- Earliest active lease wins.
- Stale or expired work must be resumed with a `takeover` event.
- Any work without a lease is invalid and must be released.

## 5. Command Reference

```bash
# Validate board
node scripts/validate-board.mjs

# Append a claim with default lease policy
node scripts/board-event.mjs \
  --event claim \
  --agent agent-url-1 \
  --branch slice/url-state \
  --slice url-state \
  --task extract_url_state_module \
  --status in_progress

# Append heartbeat
node scripts/board-event.mjs \
  --event heartbeat \
  --agent agent-url-1 \
  --branch slice/url-state \
  --slice url-state \
  --task extract_url_state_module \
  --status in_progress \
  --details "parser extraction done"
```

## 6. CI Tripwires

Before merge to integration branch, the following must pass:

1. Board validation
2. Syntax checks
3. Formatting checks
