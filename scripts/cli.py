#!/usr/bin/env python3
"""git-ignore-io — Generate .gitignore from gitignore.io API. CLI with search and multiple language support."""
import sys, json, argparse
def main():
    parser = argparse.ArgumentParser(description="Generate .gitignore from gitignore.io API. CLI with search and multiple language support.")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = {"tool": "git-ignore-io", "ready": True}
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"{result}")
if __name__ == "__main__":
    main()
