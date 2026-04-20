# Testing LSPosed Modules

## Setup
1. Install Magisk + Zygisk enabled
2. Install LSPosed via Magisk
3. Reboot
4. Open LSPosed Manager

## Test your module

```bash
# Install from zip via Magisk:
adb push your_module.zip /sdcard/
# Then Magisk → Modules → Install from storage

# Or use LSPosed Manager to enable/disable and adjust scope
```

## Debugging

### Check LSPosed logs
```bash
adb logcat | grep -i "lsposed\|xposed"
```

### Verify module loaded
```bash
adb shell dumpsys activity | grep -i "lsposed"
```

### Check for errors in scope
LSPosed Manager → Your Module → (check if enabled and scope is correct)

### Common issues

| Issue | Fix |
|-------|-----|
| Module not showing in LSPosed Manager | Restart LSPosed: Manager → ... → Restart Manager |
| Module crashes app | Check logcat, verify class names are correct |
| Changes not taking effect | Clear app cache: Settings → Apps → [app] → Storage → Clear Cache |
| Module won't install | Check module.prop syntax, ensure all required files present |

## Performance testing

```bash
# Monitor CPU/memory impact
adb shell "while true; do dumpsys meminfo | grep TOTAL; sleep 1; done"
```

## Module submission

1. Test thoroughly on at least 2 devices
2. Write clear README
3. Publish to GitHub
4. Submit to LSPosed Module Repo: https://modules.lsposed.org
