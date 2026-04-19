# 🧩 Xposed / LSPosed Module Collection

Curated list of the best Xposed modules for Android 12–15. Requires **LSPosed** framework (via Magisk/KernelSU).

**LSPosed:** https://github.com/LSPosed/LSPosed

---

## Quick start

```bash
# 1. Install Magisk with Zygisk enabled
# 2. Install LSPosed via Magisk Modules
# 3. Reboot
# 4. LSPosed Manager shortcut appears
# 5. Install modules from within LSPosed
```

---

## ⭐ Tier-1 (Most popular & stable)

| Module | Scope | Purpose | Link |
|--------|-------|---------|------|
| **Shamiko** | System | Advanced root hiding (requires Zygisk) | [GitHub](https://github.com/LSPosed/Shamiko) |
| **Hide My AppList** | Apps | Hide installed apps from detection | [GitHub](https://github.com/Dr-TSNG/Hide-My-Applist) |
| **PlayIntegrityFix** | System | Pass Google Play Integrity API | [GitHub](https://github.com/chiteroman/PlayIntegrityFix) |
| **TrickyStore** | System | Hardware attestation spoofing | [GitHub](https://github.com/5ec1cff/TrickyStore) |

---

## 🔒 Privacy & Security (16 modules)

| Module | Scope | What it does |
|--------|-------|------------|
| XPrivacyLua | Apps | Restrict any permission beyond defaults |
| Location Privacy | Apps | Fake GPS per-app |
| Riru-LocationReporter | System | Block real location, spoof coordinates |
| CorePatch | System | Disable APK signature verification |
| BootloaderSpoofer | Apps | Report locked bootloader status |
| No Storage Restrict | System | Remove storage access restrictions |
| DisableFlagSecure | System | Allow screenshots in restricted apps |
| FakeWifi | System | Report connected WiFi to restricted apps |
| Clipboard Purger | System | Auto-clear clipboard periodically |
| UID Spoofer | Apps | Fake UID per-app |

---

## 🎨 UI & Customization (12 modules)

| Module | Scope | What it does |
|--------|-------|------------|
| Iconify | System | Full Android UI theming |
| GravityBox | System | Classic system tweaks (legacy) |
| QuickSwitch | System | Alt recent apps provider |
| Cemiuiler | System | MIUI tweaks (Xiaomi) |
| Statusbar Customizer | System | Control status bar icons & colors |
| Volume Steps | System | Increase volume button granularity |
| SystemUI Tuner | System | Unlock hidden system settings |

---

## 🚀 Performance & Optimization (8 modules)

| Module | Scope | What it does |
|--------|-------|------------|
| Cleaner | Apps | Auto app cache cleaner |
| Memory Booster | System | Memory optimization background |
| Battery Limiter | System | Stop charging at threshold |
| Network Limiter | Apps | Per-app bandwidth limits |

---

## 🔄 Installation & scoping

1. **Install module** in LSPosed Manager
2. **Set scope** = which apps it affects
3. **Reboot** (most system-scope modules require it)
4. Done

**Common scopes:**
- `android` = system-wide effect
- `com.example.app` = single app only
- Multiple packages = use commas

---

## ⚠️ Conflicts & tips

- **PlayIntegrityFix + TrickyStore** = TrickyStore does stronger attestation spoofing (use instead of PlayIntegrityFix for banking)
- **Shamiko + Hide My AppList** = use together for maximum root hiding
- **Iconify conflicts** with system UI changes — disable other theme mods if installing
- Always test modules one at a time — if bootloop, go to recovery and uninstall last module

---

*See also: [frida-scripts-android](https://github.com/OutrageousStorm/frida-scripts-android) for runtime hooking alternatives*
