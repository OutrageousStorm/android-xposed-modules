#!/usr/bin/env python3
"""
module-finder.py -- Search and install Xposed/LSPosed modules
Queries module repository and shows installation instructions.
Usage: python3 module-finder.py [search_query]
"""
import subprocess, json, sys, urllib.request

REPO_URL = "https://modules.lsposed.org/api"

def fetch_modules():
    try:
        with urllib.request.urlopen(f"{REPO_URL}/modules") as r:
            return json.loads(r.read().decode())
    except Exception as e:
        print(f"Error fetching repo: {e}")
        return []

def search_modules(query):
    modules = fetch_modules()
    query_lower = query.lower()
    return [m for m in modules if 
            query_lower in m.get('name', '').lower() or 
            query_lower in m.get('description', '').lower()]

def display_module(m):
    print(f"\n📦 {m.get('name')}")
    print(f"   Author: {m.get('author')}")
    print(f"   Desc:   {m.get('description')}")
    print(f"   Rating: {m.get('stars', 0)}⭐")
    print(f"   Status: {m.get('status', 'active')}")
    print(f"   URL:    {m.get('project_page', 'N/A')}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 module-finder.py <search_term>")
        print("Examples:")
        print("  python3 module-finder.py ssl")
        print("  python3 module-finder.py location")
        print("  python3 module-finder.py privacy")
        return

    query = " ".join(sys.argv[1:])
    print(f"🔍 Searching for: {query}")
    
    results = search_modules(query)
    if not results:
        print("No modules found.")
        return

    print(f"\nFound {len(results)} modules:\n")
    for m in results[:10]:
        display_module(m)

    print("\n💡 Install modules via LSPosed app: Modules → search → enable")

if __name__ == "__main__":
    main()
