# Creating LSPosed Modules

Guide to building your own Xposed/LSPosed modules.

---

## Project Setup

```bash
# Clone template
git clone https://github.com/LSPosed/LSPosed.git

# Or use Android Studio:
# File → New → Project → use module template from LSPosed
```

## Minimal Module Structure

```
MyModule/
├── app/
│   ├── build.gradle
│   └── src/main/
│       ├── AndroidManifest.xml
│       ├── resources/
│       └── java/
│           └── com/example/MyModule.kt
├── template/
│   └── system.prop
└── build.gradle
```

## Hook Example (Kotlin)

```kotlin
package com.example.mymodule

import de.robv.android.xposed.IXposedHookLoadPackage
import de.robv.android.xposed.XC_MethodHook
import de.robv.android.xposed.XposedBridge
import de.robv.android.xposed.callbacks.XC_LoadPackage

class Hook : IXposedHookLoadPackage {
    override fun handleLoadPackage(lpparam: XC_LoadPackage.LoadPackageParam) {
        if (lpparam.packageName != "com.target.app") return

        // Hook a method
        val targetClass = lpparam.classLoader.loadClass("com.target.app.MainActivity")
        XposedBridge.hookAllMethods(targetClass, "onCreate", object : XC_MethodHook() {
            override fun beforeHookedMethod(param: MethodHookParam) {
                XposedBridge.log("onCreate called!")
            }

            override fun afterHookedMethod(param: MethodHookParam) {
                // Modify the result if needed
                param.result = null
            }
        })
    }
}
```

## Building & Installing

```bash
# Build
./gradlew build

# Output APK: app/build/outputs/apk/release/app-release.apk

# Install (must have Magisk + Zygisk + LSPosed)
adb install app/build/outputs/apk/release/app-release.apk

# Enable in LSPosed Manager
# Restart target app
```

---

## Common Hooks

### System Settings
```kotlin
val settingsClass = lpparam.classLoader.loadClass("android.provider.Settings")
XposedBridge.hookMethod(settingsClass.getMethod("getString", ...)) { hook ->
    // Intercept settings
}
```

### Permissions
```kotlin
val pmClass = lpparam.classLoader.loadClass("android.app.ApplicationPackageManager")
XposedBridge.hookMethod(pmClass.getMethod("checkPermission", ...)) { hook ->
    hook.result = android.content.pm.PackageManager.PERMISSION_GRANTED
}
```

### Network
```kotlin
val urlClass = lpparam.classLoader.loadClass("java.net.URL")
XposedBridge.hookMethod(urlClass.getMethod("openConnection")) { hook ->
    // Intercept network calls
}
```

---

## Publishing

1. Build release APK
2. Upload to XDA or LSPosed Module Repo
3. Users install through LSPosed Manager → Modules
4. Select app scope, reboot, done

---

**Resources:**
- [LSPosed docs](https://github.com/LSPosed/LSPosed)
- [Xposed Framework wiki](https://github.com/rovo89/XposedBridge/wiki)
