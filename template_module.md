# Build Your Own LSPosed Module

Template walkthrough for creating LSPosed modules.

## Minimal module structure

```
MyModule/
├── module.prop
├── system/
│   └── priv-app/
│       └── MyModule/
│           └── MyModule.apk
└── service.sh
```

## module.prop
```properties
id=my_awesome_module
name=My Awesome Module
version=1.0
versionCode=1
author=YourName
description=What your module does
minApi=30
maxApi=34
```

## Building the APK (LSPosed hook)

### AndroidManifest.xml
```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.mymodule">
    <uses-sdk android:minSdkVersion="30"/>
    <application>
        <meta-data
            android:name="xposedmodule"
            android:value="true"/>
        <meta-data
            android:name="xposeddescription"
            android:value="Module description"/>
        <meta-data
            android:name="xposedminversion"
            android:value="54"/>
    </application>
</manifest>
```

### Hook entry point (Java)
```java
package com.example.mymodule;

import de.robv.android.xposed.IXposedHookLoadPackage;
import de.robv.android.xposed.XposedBridge;
import de.robv.android.xposed.callbacks.XC_LoadPackage;

public class Hook implements IXposedHookLoadPackage {
    @Override
    public void handleLoadPackage(XC_LoadPackage.LoadPackageParam lpparam) throws Throwable {
        if (lpparam.packageName.equals("target.package")) {
            // Hook into target.package
            XposedBridge.log("[MyModule] Hooked into " + lpparam.packageName);
            
            // Example: hook a method
            Class<?> targetClass = lpparam.classLoader.loadClass("com.example.Target");
            XposedBridge.hookMethod(targetClass.getMethod("doSomething"), 
                new XC_MethodHook() {
                    @Override
                    protected void afterHookedMethod(MethodHookParam param) throws Throwable {
                        XposedBridge.log("doSomething was called!");
                    }
                });
        }
    }
}
```

## Build & Package
```bash
gradle build
# Get APK from build/outputs/apk/release/
cp app/build/outputs/apk/release/app-release.apk MyModule/system/priv-app/MyModule/MyModule.apk
cd MyModule && zip -r MyModule.zip . && cd ..
```

## Install
LSPosed Manager → Modules → Install from storage → select MyModule.zip → reboot

## Popular hooks to build on
- Disable FLAG_SECURE (allow screenshots)
- SSL pinning bypass
- Root detection bypass
- Hide app list
- Spoof device properties
- Intercept network calls
