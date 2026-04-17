package com.example.xposed

import de.robv.android.xposed.IXposedHookLoadPackage
import de.robv.android.xposed.IXposedHookZygoteInit
import de.robv.android.xposed.XC_MethodHook
import de.robv.android.xposed.XposedBridge
import de.robv.android.xposed.callbacks.XC_LoadPackage

class XposedInit : IXposedHookZygoteInit {
    override fun initZygote(startupParam: StartupParam?) {
        XposedBridge.log("[MyModule] Zygote init")
    }
}

class XposedHook : IXposedHookLoadPackage {
    override fun handleLoadPackage(lpparam: XC_LoadPackage.LoadPackageParam) {
        if (lpparam.packageName != "com.example.targetapp") return

        XposedBridge.log("[MyModule] Hooking ${lpparam.packageName}")

        // Example: hook a method
        try {
            val targetClass = lpparam.classLoader.loadClass("com.example.targetapp.SomeClass")
            val targetMethod = targetClass.getMethod("someMethod", String::class.java)

            XposedBridge.hookMethod(targetMethod, object : XC_MethodHook() {
                override fun beforeHookedMethod(param: MethodHookParam) {
                    val arg = param.args[0] as String
                    XposedBridge.log("[MyModule] someMethod called with: $arg")
                    // Modify behavior
                    param.args[0] = "modified_value"
                }

                override fun afterHookedMethod(param: MethodHookParam) {
                    val result = param.result
                    XposedBridge.log("[MyModule] someMethod returned: $result")
                }
            })
        } catch (e: Exception) {
            XposedBridge.log("[MyModule] Error: ${e.message}")
        }
    }
}
