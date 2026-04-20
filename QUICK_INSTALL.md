# Quick Install Guide — LSPosed Modules

**TL;DR version:** 3 minutes to modded Android.

## Prerequisites
- Device with Magisk + Zygisk enabled (see [Magisk setup](../android-rom-guide/guides/magisk-setup.md))
- 5 minutes

## Step-by-step

### 1. Install LSPosed (1 min)
```bash
# Assuming Magisk is already installed
# Download LSPosed from: https://github.com/LSPosed/LSPosed/releases
# (choose your Android version)

# In Magisk app → Modules → Install from storage
# Select LSPosed zip file
# Reboot
```

### 2. Install first module (1 min)
```bash
# Open LSPosed app (should be in your app drawer)
# Go to Modules → search for a module
# Install (this downloads + adds it to LSPosed)
# Go to Scope → select which apps this affects
# Reboot (or force-stop the app and restart it)
```

### 3. Verify it's working (1 min)
```bash
# For privacy modules: Settings → Privacy → Permission Manager
# Should show restrictive permissions now

# For UI modules: Launcher should show changes immediately
# For system modules: Full reboot required
```

## Recommended first 3 modules

1. **Shamiko** — Hide root from apps (go to banking app → should pass SafetyNet)
2. **Hide My AppList** — Apps can't see what you have installed
3. **PlayIntegrityFix** — Pass Google Play Integrity (needed for some apps)

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Module not showing in apps | Force-stop the app, wait 10s, restart |
| LSPosed crashes on boot | Disable all modules, reboot, re-enable one by one |
| Banking app still detects root | Ensure Shamiko is in scope + TrickyStore for newer banks |

## Next step: Add 2-3 more modules
See [main list](README.md) for module recommendations by category.

---
Want to go deeper? [LSPosed docs](https://lsposed.org)
