#!/usr/bin/env python3
"""
find_modules.py -- Find LSPosed modules by function/category
Usage: python3 find_modules.py --search "ssl" --category privacy
"""
import subprocess, re, json, argparse

MODULES_DB = [
    {
        "name": "PlayIntegrityFix",
        "repo": "chiteroman/PlayIntegrityFix",
        "categories": ["security", "banking"],
        "functions": ["spoof device integrity", "pass hardware attestation"],
    },
    {
        "name": "TrickyStore",
        "repo": "5ec1cff/TrickyStore",
        "categories": ["security", "banking"],
        "functions": ["hardware attestation", "banking app bypass"],
    },
    {
        "name": "Hide My AppList",
        "repo": "Dr-TSNG/Hide-My-Applist",
        "categories": ["privacy"],
        "functions": ["hide installed apps", "privacy"],
    },
    {
        "name": "DisableFlagSecure",
        "repo": "LSPosed/DisableFlagSecure",
        "categories": ["screenshot", "ui"],
        "functions": ["screenshot blocked apps", "screenshot"],
    },
    {
        "name": "CorePatch",
        "repo": "LSPosed/CorePatch",
        "categories": ["security"],
        "functions": ["disable signature verification", "install unsigned apks"],
    },
    {
        "name": "Iconify",
        "repo": "Mahmud0808/Iconify",
        "categories": ["ui", "customization"],
        "functions": ["theme icons", "ui customization", "colors"],
    },
]

def find(search=None, category=None):
    results = MODULES_DB
    if search:
        search = search.lower()
        results = [m for m in results if search in m['name'].lower() or
                   any(search in f for f in m.get('functions', []))]
    if category:
        results = [m for m in results if category in m.get('categories', [])]
    return results

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--search", help="Search by name or function")
    parser.add_argument("--category", help="Filter by category (privacy, security, ui, banking)")
    parser.add_argument("--list-categories", action="store_true")
    args = parser.parse_args()

    if args.list_categories:
        cats = set()
        for m in MODULES_DB:
            cats.update(m.get('categories', []))
        print("\nAvailable categories:")
        for c in sorted(cats):
            print(f"  {c}")
        return

    results = find(args.search, args.category)
    if not results:
        print("No modules found.")
        return

    print(f"\nFound {len(results)} module(s)\n")
    for m in results:
        print(f"📦 {m['name']}")
        print(f"   GitHub: {m['repo']}")
        print(f"   Functions: {', '.join(m.get('functions', []))}")
        print(f"   Categories: {', '.join(m.get('categories', []))}")
        print()

if __name__ == "__main__":
    main()
