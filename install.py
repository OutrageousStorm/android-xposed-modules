#!/usr/bin/env python3
"""
install.py -- LSPosed module installer from list or search
Usage: python3 install.py [--module modulename] [--search keyword] [--install-all]
"""
import subprocess, json, sys, argparse

MODULES = {
    "PlayIntegrityFix": "https://github.com/chiteroman/PlayIntegrityFix",
    "Hide My AppList": "https://github.com/Dr-TSNG/Hide-My-Applist",
    "Shamiko": "https://github.com/LSPosed/Shamiko",
    "LSPosed": "https://github.com/LSPosed/LSPosed",
    "TrickyStore": "https://github.com/5ec1cff/TrickyStore",
    "Iconify": "https://github.com/Mahmud0808/Iconify",
    "GravityBox": "https://github.com/C3C0/GravityBox",
    "XPrivacyLua": "https://github.com/M66B/XPrivacyLua",
    "Cemiuiler": "https://github.com/MiuiItemSettings/Cemiuiler",
    "DisableFlagSecure": "https://github.com/LSPosed/DisableFlagSecure",
    "CorePatch": "https://github.com/LSPosed/CorePatch",
    "RikkaX": "https://github.com/RikkaApps/RikkaX",
}

def install_via_magisk(module_name):
    """Install module into Magisk"""
    cmd = f"adb shell su -c 'cd /data/adb/modules && wget -q {MODULES[module_name]}/releases/download/latest/module.zip -O {module_name}.zip && unzip {module_name}.zip'"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"✓ {module_name} installed. Reboot required.")
    else:
        print(f"✗ Failed to install {module_name}")

def search_modules(keyword):
    """Search available modules"""
    matches = [k for k in MODULES.keys() if keyword.lower() in k.lower()]
    if not matches:
        print(f"No modules found matching '{keyword}'")
        return
    print(f"
Found {len(matches)} module(s):
")
    for i, m in enumerate(matches, 1):
        print(f"  {i}. {m}")
        print(f"     {MODULES[m]}")

def list_all():
    """List all available modules"""
    print("
📦 Available LSPosed Modules:
")
    for name, url in sorted(MODULES.items()):
        print(f"  • {name}")
        print(f"    {url}
")

def main():
    parser = argparse.ArgumentParser(description="LSPosed Module Installer")
    parser.add_argument("--module", help="Module name to install")
    parser.add_argument("--search", help="Search modules by keyword")
    parser.add_argument("--list", action="store_true", help="List all modules")
    args = parser.parse_args()

    if args.search:
        search_modules(args.search)
    elif args.module:
        if args.module in MODULES:
            print(f"Installing {args.module}...")
            install_via_magisk(args.module)
        else:
            print(f"Unknown module: {args.module}")
            search_modules(args.module)
    else:
        list_all()

if __name__ == "__main__":
    main()
