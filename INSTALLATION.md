# LSPosed Module Installation Guide

## Prerequisites

```bash
# Device must have:
# 1. Magisk installed (see android-rom-guide)
# 2. Zygisk enabled in Magisk settings
# 3. LSPosed framework installed via Magisk module
```

## Install LSPosed

1. Download LSPosed release: https://github.com/LSPosed/LSPosed/releases
   - Pick `LSPosed-v<version>-<android_version>-arm64-release.zip`
2. Flash in Magisk:
   - Magisk app → Modules → Install from storage → select zip
3. Reboot device
4. LSPosed icon appears in notification area or Settings

## Install a Module

```bash
# Via LSPosed app:
1. Open LSPosed app
2. Modules tab → tap + icon
3. Search for module (e.g., "Hide My AppList")
4. Install
5. Enable the module
6. Set scope (which apps it applies to) — CRITICAL!
7. Reboot device (usually required)
```

## Module Scoping

Scope determines which apps a module affects:

- **System scope** → Module applies system-wide (affects ALL apps)
  - Use for: system tweaks, theme changes
- **App scope** → Module only affects specific apps
  - Use for: per-app privacy controls, app-specific mods

Example: "Hide My AppList" should be scoped to the apps that try to detect what you have installed.

## Troubleshooting

**Module causes bootloop:**
1. Boot to recovery (hold Vol Down + Power at boot)
2. Settings → Magisk → Modules
3. Disable problem module
4. Reboot

**Module doesn't seem to work:**
- Force-stop target app: `adb shell am force-stop com.example.app`
- Make sure scope is correct (check LSPosed → Modules → app name)
- Reboot device

**LSPosed won't install:**
- Ensure Zygisk is enabled in Magisk settings
- Rebuild Magisk by reinstalling boot.img patch
