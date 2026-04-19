# Advanced LSPosed Techniques

## Creating custom scopes for modules

Most LSPosed modules let you choose which apps they target. Best practices:

### Per-app configuration
- **Youtube ReVanced:** scope to youtube only, not YouTube Music
- **LocationPrivacy:** scope to apps that don't need real location
- **Hide My AppList:** system scope for maximum hiding (affects all app queries)

### System scope (affects OS)
- Applies to Android framework itself
- Slower, higher risk of boot loops
- Use cautiously; can disable in LSPosed if problems occur

## Debugging module issues

If a module breaks something:

1. **Disable in LSPosed**, restart
2. **Check logcat** for module errors:
   ```bash
   adb logcat | grep -i "lsposed\|error\|crash"
   ```
3. **Uninstall module**, reboot
4. **Update module** to latest version

## Combining multiple modules safely

Safe combinations:
- Hide My AppList + TrickyStore
- PlayIntegrityFix + CorePatch
- LocationPrivacy + XPrivacyLua

Avoid:
- Multiple root-hiding modules together (conflict)
- Multiple Zygisk modules on old Android (stability issues)

## Building your own LSPosed module

Create a simple hook module (Kotlin):

```kotlin
// Hook example: always return false for isRooted()
override fun handleLoadPackage(lpparam: XC_LoadPackage.LoadPackageParam?) {
    lpparam?.let {
        if (it.packageName == "com.example.app") {
            val hookClass = XposedHelpers.findClass(
                "com.example.app.RootChecker", it.classLoader
            )
            XposedHelpers.findAndHookMethod(
                hookClass, "isRooted",
                object : XC_MethodReplacement() {
                    override fun replaceHooked(param: MethodHookParam?) {
                        param?.result = false
                    }
                }
            )
        }
    }
}
```

Full template: https://github.com/LSPosed/LSPosed/blob/main/README.md

---

*Learn more at: [LSPosed Wiki](https://lsposed.org)*
