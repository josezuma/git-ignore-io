#!/usr/bin/env python3
"""CLI: git-ignore-io"""
import sys, json, argparse
from datetime import datetime
def main():
    parser = argparse.ArgumentParser(description="Git Ignore Io")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    r = {"tool": "git-ignore-io", "v": "1.0.0", "author": "Jose Zuma"}
    print(json.dumps(r, indent=2) if args.json else f"{name} v1.0.0")
if __name__ == "__main__": main()
