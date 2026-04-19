# Complete LSPosed + Module Installation Guide

## Step 1: Install Magisk (if not already done)

```bash
# Download Magisk APK from: https://github.com/topjohnwu/Magisk/releases
adb install Magisk-v27.0.apk

# In Magisk app: Install → Select and Patch a File → pick boot.img
# Flash the patched boot.img via fastboot
adb reboot bootloader
fastboot flash boot magisk_patched_xxx.img
fastboot reboot
```

## Step 2: Enable Zygisk

In Magisk app:
- Settings → Zygisk → **On**
- Reboot device

## Step 3: Install LSPosed

1. Download LSPosed for your Android version: https://github.com/LSPosed/LSPosed/releases
2. In Magisk app: **Modules** → Install from storage → select LSPosed zip
3. **Reboot**
4. Open LSPosed Manager (should appear in notification after reboot)

## Step 4: Install Modules

In LSPosed Manager:

1. **Hide My AppList** — prevent apps from detecting other installed apps
   - Scope: System + all apps
   - Reboot
   - Verify: open any app that checks app list — it won't see your hidden apps

2. **TrickyStore** — pass Play Integrity check for banking apps
   - Scope: System (apply to whole device)
   - Reboot
   - Test with Play Store → My Apps & games → should pass

3. **PlayIntegrityFix** (if TrickyStore alone doesn't work)
   - Scope: System
   - Reboot

## Step 5: Configure DenyList (Root Hiding)

If you want to hide root from an app:

1. In Magisk app: Settings → **Configure DenyList**
2. Check the apps that should NOT see root
3. Reboot

This works best with **Shamiko** module installed (automatic with Zygisk).

## Troubleshooting

| Problem | Fix |
|---------|-----|
| LSPosed Manager won't open | LSPosed not properly installed. Reinstall from Magisk → Modules |
| Module not applying | Module not scoped to correct app. Re-check scope in LSPosed. |
| App detects root despite DenyList | Install Shamiko module in Magisk |
| Banking app crashes | Install TrickyStore + PlayIntegrityFix, make sure both scoped to System |
| System unstable after module | Uninstall module in LSPosed Manager, clear cache |

---

**Module recommendations by use case:**
- **Privacy** — Hide My AppList, TrickyStore, XPrivacyLua
- **UI** — Iconify, GravityBox, QuickSwitch
- **Banking** — TrickyStore, PlayIntegrityFix, BootloaderSpoofer
- **Games** — CorePatch (no APK sig check), disable app detection modules in games

