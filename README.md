# 🧩 Xposed / LSPosed Module Collection

Curated list of the best Xposed modules for Android 12–15. Requires **LSPosed** framework (via Magisk/KernelSU).

**LSPosed:** https://github.com/LSPosed/LSPosed

---

## Install LSPosed first

```bash
# 1. Install Magisk (see android-rom-guide)
# 2. Enable Zygisk in Magisk settings
# 3. Flash LSPosed zip via Magisk → Modules → install from storage
#    Download: https://github.com/LSPosed/LSPosed/releases
# 4. Reboot
# 5. Open LSPosed from notification or via Manager shortcut
```

---

## Privacy & Security

| Module | Description | Scope | Link |
|--------|-------------|-------|------|
| **Hide My AppList** | Prevent apps from detecting which other apps are installed | System + target apps | [GitHub](https://github.com/Dr-TSNG/Hide-My-Applist) |
| **Location Privacy** | Fake GPS location per-app | Target apps | [GitHub](https://github.com/Mygod/location-privacy) |
| **XPrivacyLua** | Restrict any permission beyond Android defaults | Target apps | [GitHub](https://github.com/M66B/XPrivacyLua) |
| **BootloaderSpoofer** | Spoof locked bootloader status to specific apps | Target apps | [GitHub](https://github.com/chiteroman/BootloaderSpoofer) |
| **TrickyStore** | Hardware-level attestation spoofing for banking apps | System | [GitHub](https://github.com/5ec1cff/TrickyStore) |
| **Riru-LocationReporter** | Report fake coordinates, block real ones | System | Search XDA |

---

## UI & Customization

| Module | Description | Scope | Link |
|--------|-------------|-------|------|
| **Iconify** | Full UI theming — icons, colors, shapes, status bar | System | [GitHub](https://github.com/Mahmud0808/Iconify) |
| **QuickSwitch** | Use third-party launchers as recents provider | System | [GitHub](https://github.com/skittles9823/QuickSwitch) |
| **GravityBox** | Swiss-army knife of UI tweaks (classic) | System | [GitHub](https://github.com/C3C0/GravityBox) |
| **Cemiuiler** | MIUI system tweaks (Xiaomi only) | System | [GitHub](https://github.com/MiuiItemSettings/Cemiuiler) |
| **SystemUI Tuner** | Unlock hidden system UI settings | System | [Play Store](https://play.google.com/store/apps/details?id=com.zacharee1.systemuituner) |

---

## App Mods

| Module | Description | Scope | Link |
|--------|-------------|-------|------|
| **ReVanced Extended** | YouTube ad blocking, background play, SponsorBlock | YouTube | [GitHub](https://github.com/inotia00/ReVanced_Extended) |
| **InstaXposed** | Instagram ad removal, download enabled | Instagram | XDA search |
| **TikTok Filter** | TikTok ad blocking | TikTok | XDA search |
| **WA Tweaks** | WhatsApp extra features — anti-delete, download status | WhatsApp | XDA search |
| **Twitter Blue Bypass** | Unlock Twitter Blue features for free | Twitter/X | XDA search |

---

## System & Performance

| Module | Description | Scope | Link |
|--------|-------------|-------|------|
| **CorePatch** | Disable APK signature verification (install modified APKs) | System | [GitHub](https://github.com/LSPosed/CorePatch) |
| **XAutoDaily** | Auto sign-in for various Chinese apps | Various | XDA |
| **FakeWifi** | Report Wi-Fi connected to apps that restrict mobile data | System | GitHub |
| **DisableFlagSecure** | Allow screenshots in apps that disable them | System | [GitHub](https://github.com/LSPosed/DisableFlagSecure) |
| **No Storage Restrict** | Remove storage access restrictions | System | [GitHub](https://github.com/Xposed-Modules-Repo/me.kismy.nostoragerestrict) |

---

## How to use LSPosed

1. Enable module in **LSPosed Manager**
2. Set the **scope** — which apps the module applies to
3. Reboot (usually required for system-scope modules)
4. For app-scope modules: force-stop the target app

**Important:** Scope matters. A module scoped to `com.example.app` only affects that app. Scope to `android` for system-wide effect.

---

## Module repositories

- **LSPosed Module Repo:** https://modules.lsposed.org
- **XDA Xposed section:** https://forum.xda-developers.com/c/xposed-framework.2317/
- **GitHub:** search `xposed` or `lsposed`
