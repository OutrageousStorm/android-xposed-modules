# LSPosed Module Installation

## Prerequisites
1. Magisk installed + Zygisk enabled
2. LSPosed module installed via Magisk
3. Device rebooted

## Install Steps

1. Open LSPosed Manager
2. Go to Modules tab
3. Tap + to install module
4. Select module APK from storage or repo
5. Tap "Install" and wait
6. Enable the module (toggle ON)
7. Tap module to set scope (which apps it affects)
8. **REBOOT** device

## Scope Configuration

**System scope** (all apps):
- Tap Scope
- Enable "android"
- Module affects everything

**App-specific** (single app):
- Tap Scope
- Find and enable specific app package
- Module only runs in that app

## Troubleshooting

**Module not showing**
- Installation failed, try again
- Zygisk not enabled, enable in Magisk
- Android version not supported

**Module enabled but doesn't work**
- App not added to scope
- Device not rebooted
- Conflicting with other modules

**App crashes after enabling**
- Uninstall conflicting modules
- Clear app data: Settings → Apps → [app] → Clear Storage

**App not in scope list**
- Tap refresh icon at top right
- Long-press to search by name
