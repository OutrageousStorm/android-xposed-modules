# LSPosed Installation & Setup

Complete step-by-step for getting LSPosed + modules working on Android 12–15.

## Prerequisites
- Device with Magisk installed + Zygisk enabled
- ~2 minutes setup time

## Installation

### Step 1: Enable Zygisk
1. Open Magisk app
2. Settings → Zygisk → toggle ON
3. Reboot

### Step 2: Install LSPosed
1. Download LSPosed from: https://github.com/LSPosed/LSPosed/releases
2. In Magisk: Modules → Install from storage → select LSPosed zip
3. Reboot

### Step 3: Verify
1. Should see LSPosed shortcut in app drawer (or in Magisk Manager app → Open LSPosed)
2. You're ready to install modules

## Installing a Module

1. Open LSPosed Manager app
2. Go to **Modules** tab
3. Press + button or click **Install**
4. Navigate to downloaded module zip file → select
5. Reboot
6. Go back to LSPosed → find the module in list
7. Enable checkbox next to module name
8. **Scope** the module (choose which apps it applies to)
9. **Force-stop** target app or reboot

## Common Issues

| Problem | Fix |
|---------|-----|
| "LSPosed not active" | Ensure Zygisk is ON in Magisk, then reboot |
| Module loads but doesn't work | Check the Scope — make sure target app is scoped |
| Force-crashes after installing module | Disable module in LSPosed, reboot, try another module |
| "Cannot find LSPosed" after install | Module installed to inactive slot — reboot and check again |

## Recommended First Modules
1. **Hide My AppList** — prevent apps detecting your installed apps
2. **PlayIntegrityFix** — pass Google's hardware attestation check
3. **TrickyStore** — hardware-level attestation spoofing for banking apps

## Module Scoping Tips
- **System** scope = affects all apps (be careful)
- **App-specific** scope = only affects checked apps (safer)
- If an app crashes after scoping, uncheck it and try again

## Testing
```bash
# Check LSPosed is active via ADB
adb shell getprop dalvik.vm.enable_apex_image
# Should output: true
```
