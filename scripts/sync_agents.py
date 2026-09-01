#!/usr/bin/env python3
"""
SYNC AGENTS (Content Injection Mode)
------------------------------------
Reads each source document and INJECTS it directly into its target files.

Why Injection?
- Guarantees SSoT (Single Source of Truth) even if tools don't support imports.
- Forces the "Negative Space" rules into the immediate context window.

One source of truth per document; edit the source, run this, everything follows.

Usage:
    python scripts/sync_agents.py             # write targets
    python scripts/sync_agents.py --dry-run   # report what would change, write nothing
"""
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

# Machine-local root for copies that live outside the repo.
DEV_ROOT = os.environ.get("DEV_ROOT", r"C:\Dev")

# Each document has ONE source and many targets.
DOCUMENTS = [
    {
        "name": "Constitution",
        "source": "promptkit/AGENTS.md",
        "targets": [
            ".gemini/GEMINI.md",                # Gemini CLI
            "CLAUDE.md",                        # Claude Projects/Desktop
            "AGENTS.md",                        # OpenCode + Codex CLI (project SSoT)
            ".prompts/instructions.md",         # Theia AI
            ".github/copilot-instructions.md",  # GitHub CoPilot CLI
            "~/.codex/AGENTS.md",               # Codex global instructions
            "~/.claude/CLAUDE.md",              # Claude Code global config
        ],
    },
    {
        "name": "DevOps Guide",
        "source": "promptkit/skills/devops/SKILL_DevOps_Guide.md",
        "targets": [
            os.path.join(DEV_ROOT, "SKILL_DevOps_Guide.md"),
            os.path.join(DEV_ROOT, "projects", "SKILL_DevOps_Guide.md"),
            "~/AGENTS.md",  # Home-root, tool-agnostic copy. No tool auto-scans this
                             # path today (there is no ratified global AGENTS.md
                             # convention yet) -- this stakes a stable, literally-
                             # named claim for whichever tools adopt one next,
                             # and gives humans/scripts one unambiguous place to
                             # look regardless of which agent they're using.
        ],
    },
]

# NOT a target: ~/.gemini/GEMINI.md. Unlike the files above, that path is Gemini
# CLI's own auto-accumulated memory log ("## Gemini Added Memories"), not a static
# instructions file -- Gemini appends to it itself. Injecting here would silently
# overwrite real session memory on every sync run. If Gemini needs the DevOps
# Guide pointer, it has to go in via Gemini's own memory mechanism, not this
# unconditional-overwrite script.

HEADER = """<!--
⚠️ AUTO-GENERATED: DO NOT EDIT DIRECTLY
SOURCE: {source}
SYNC COMMAND: python scripts/sync_agents.py
-->

"""

# Injection emits Markdown. Writing it into a config file produces a file the
# tool cannot parse -- .codex/config.toml was silently invalid TOML from v2.0.5
# to v2.1.0 for exactly this reason. Fail loudly instead of corrupting quietly.
MARKDOWN_SUFFIXES = (".md", ".markdown")


def check_target(target):
    """Reject targets that Markdown injection cannot produce valid output for."""
    if not target.lower().endswith(MARKDOWN_SUFFIXES):
        ext = os.path.splitext(target)[1] or "(no extension)"
        raise ValueError(
            f"Refusing to inject Markdown into '{target}' [{ext}].\n"
            "    Injection only yields valid output for Markdown targets. A TOML/JSON/"
            "YAML\n    config needs a real writer for its own format -- not this script."
        )


def sync(dry_run=False):
    failures = 0
    written = 0

    for doc in DOCUMENTS:
        source = doc["source"]
        if not os.path.exists(source):
            print(f"❌ Critical: source '{source}' not found. Are you in the repo root?")
            failures += 1
            continue

        print(f"\n📖 {doc['name']} — reading {source}")
        with open(source, encoding="utf-8") as f:
            content = f.read()
        payload = HEADER.format(source=source) + content

        for target in doc["targets"]:
            target_path = os.path.expanduser(target)
            try:
                check_target(target_path)
            except ValueError as e:
                print(f"⛔ {e}")
                failures += 1
                continue

            target_dir = os.path.dirname(target_path)
            if target_dir and not os.path.exists(target_dir):
                if dry_run:
                    print(f"📂 would create directory: {target_dir}")
                else:
                    os.makedirs(target_dir)
                    print(f"📂 Created directory: {target_dir}")

            if dry_run:
                current = None
                if os.path.exists(target_path):
                    with open(target_path, encoding="utf-8") as f:
                        current = f.read()
                state = "unchanged" if current == payload else "WOULD CHANGE"
                print(f"🔍 {state:<12} {target_path}")
                written += 1
                continue

            try:
                with open(target_path, "w", encoding="utf-8") as f:
                    f.write(payload)
                print(f"✅ Injected -> {target_path}")
                written += 1
            except Exception as e:
                print(f"⚠️ Failed to write {target_path}: {e}")
                failures += 1

    verb = "checked" if dry_run else "written"
    print(f"\n{'—' * 60}")
    print(f"{len(DOCUMENTS)} document(s), {written} target(s) {verb}, {failures} failure(s).")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(sync(dry_run="--dry-run" in sys.argv))
