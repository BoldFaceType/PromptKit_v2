#!/usr/bin/env python3
"""
SYNC AGENTS (Content Injection Mode)
------------------------------------
Reads the Master Constitution (promptkit/AGENTS.md) and INJECTS it
directly into tool-specific config files.

Why Injection?
- Guarantees SSoT (Single Source of Truth) even if tools don't support imports.
- Forces the "Negative Space" rules into the immediate context window.
"""
import os
import shutil

# Configuration
SOURCE = "promptkit/AGENTS.md"
TARGETS = [
    ".gemini/GEMINI.md",              # Gemini CLI
    "CLAUDE.md",                      # Claude Projects/Desktop
    "AGENTS.md",                      # OpenCode (Project-specific SSoT)
    ".codex/config.toml",             # Codex CLI
    ".prompts/instructions.md",       # Theia AI
    ".github/copilot-instructions.md", # GitHub CoPilot CLI
    "~/.claude/CLAUDE.md",            # Claude Code global config
]

HEADER = """<!--
⚠️ AUTO-GENERATED: DO NOT EDIT DIRECTLY
SOURCE: promptkit/AGENTS.md
SYNC COMMAND: python scripts/sync_agents.py
-->

"""

def sync():
    # 1. Validate Source
    if not os.path.exists(SOURCE):
        print(f"❌ Critical: Source '{SOURCE}' not found. Are you in the repo root?")
        return

    # 2. Read Constitution
    print(f"📖 Reading Constitution from {SOURCE}...")
    with open(SOURCE, "r", encoding="utf-8") as f:
        constitution_content = f.read()

    # 3. Inject into Targets
    for target in TARGETS:
        target_path = os.path.expanduser(target)
        target_dir = os.path.dirname(target_path)

        # Ensure target dir exists (e.g., .gemini/, ~/.claude/)
        if target_dir and not os.path.exists(target_dir):
            os.makedirs(target_dir)
            print(f"📂 Created directory: {target_dir}")

        # Write Content
        try:
            with open(target_path, "w", encoding="utf-8") as f:
                f.write(HEADER)
                f.write(constitution_content)
                print(f"✅ Injected -> {target_path}")
        except Exception as e:
            print(f"⚠️ Failed to write {target_path}: {e}")

if __name__ == "__main__":
    sync()
