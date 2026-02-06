#!/usr/bin/env python3
"""
SKILL: Micro-Lens Profiler
USAGE: python profile.py <target_script.py>
"""
import pstats
import sys
import subprocess
import os

def profile_target(script_path):
    if not os.path.exists(script_path):
        print(f"❌ Error: Script '{script_path}' not found.")
        sys.exit(1)

    print(f"🔬 Profiling {script_path}...")
    output_file = "profile_results.prof"
    command = [sys.executable, "-m", "cProfile", "-o", output_file, script_path]

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        print("❌ Error: Execution failed.")
        sys.exit(1)

    stats = pstats.Stats(output_file)
    stats.strip_dirs()
    stats.sort_stats('cumulative')

    print("
--- 📊 Top 5 Bottlenecks ---")
    stats.print_stats(5)

    print("
--- 🐍 Launching SnakeViz ---")
    try:
        subprocess.run(["snakeviz", output_file])
    except KeyboardInterrupt:
        print("
✅ Done.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python profile.py <script.py>")
        sys.exit(1)
    profile_target(sys.argv[1])
