package com.outrageousstorm.xposed.mymodule;

import de.robv.android.xposed.IXposedHookLoadPackage;
import de.robv.android.xposed.XposedBridge;
import de.robv.android.xposed.callbacks.XC_LoadPackage;

public class HookEntry implements IXposedHookLoadPackage {
    @Override
    public void handleLoadPackage(XC_LoadPackage.LoadPackageParam lpparam) throws Throwable {
        XposedBridge.log("Module loaded in: " + lpparam.packageName);
        
        // Hook example: intercept Settings.getString()
        if (lpparam.packageName.equals("com.android.settings")) {
            XposedBridge.hookMethod(
                Settings.class.getMethod("getString", Context.class, String.class),
                new XC_MethodHook() {
                    @Override
                    protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
                        String key = (String) param.args[1];
                        XposedBridge.log("GET: " + key);
                    }
                });
        }
    }
}
