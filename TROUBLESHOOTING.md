# LSPosed Troubleshooting

## Common issues

### "No LSPosed installed" in Manager
- LSPosed zip not installed as Magisk module
- **Fix:** Download from GitHub, flash via Magisk → Modules → install from storage
- Reboot after installation

### Module not being applied
1. Check scope — is the target app actually in the scope?
   - LSPosed Manager → [Module] → click to see scope
2. Force-stop the target app after enabling module
   - `adb shell am force-stop <package>`
3. Reboot device
4. Some modules require specific Android version — check

### App crashes after enabling module
- Module is incompatible with this app version or Android version
- **Fix:** 
  - Disable the module in LSPosed Manager
  - Uninstall and reinstall the app
  - Try a different module or module version

### "Accessing hidden methods" warning
- Some modules access @hide APIs (internal, not public)
- Android 12+ restricts this unless:
  - Module uses reflection properly
  - You're on a custom ROM that allows it
  - Use CorePatch module to bypass this check

### Module scope includes app but still not working
- The app might have multiple processes (main + services)
- LSPosed only hooks the scoped processes
- Check with: `adb shell ps | grep <package>`
- If multiple processes, hook all of them

### ZygiskNext not loading
- Zygisk not enabled in Magisk: Settings → Zygisk → toggle ON
- ZygiskNext version mismatches Magisk/Android version
- **Fix:** Download matching ZygiskNext from GitHub
- Reboot after install

### Shamiko (root hiding) conflicts with other modules
- Shamiko + Hide My AppList can conflict
- **Use one or the other**, not both
- For advanced hiding: use Shamiko alone + PlayIntegrityFix

### Module causes bootloop
1. Boot to recovery
2. In Magisk recovery UI: disable all modules
3. Reboot
4. Re-enable modules one by one to find culprit
5. Remove or update the problematic module

## Performance issues

- **Excessive battery drain:** Some modules (especially privacy-heavy ones) have overhead
  - Solution: disable modules you're not actively using
  - Use LSPosed's per-app performance settings

- **Slow app launch:** Too many Xposed hooks on startup
  - Check: do you have 5+ modules scoped to this app?
  - Reduce scope to only modules that need it

## Module not showing in LSPosed Manager

- Module is installed but not visible
- **Causes:**
  - Module APK is corrupted (re-download)
  - Module's target SDK doesn't match Android version
  - Module is for an older LSPosed version
  
- **Fix:**
  - Delete module from `/data/adb/modules/`
  - Reinstall clean version
  - Reboot

## Can't install LSPosed on KernelSU

- KernelSU module format is slightly different from Magisk
- Download LSPosed **KernelSU version** specifically
- Install in KernelSU Manager, not Magisk

## Ask for help

- Check [LSPosed GitHub Issues](https://github.com/LSPosed/LSPosed/issues)
- Include: Android version, device, LSPosed version, which modules, logcat output
- Use: `adb logcat > logcat.txt` to capture crash logs
