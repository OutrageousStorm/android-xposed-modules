/**
 * lsposed-detector-bypass.js
 * Bypass apps that detect LSPosed/Xposed framework
 * Usage: frida -U -f com.example.app -l lsposed-detector-bypass.js --no-pause
 */

setTimeout(function() {
    Java.perform(function() {
        console.log("[LSPosed Bypass] Starting...");

        // Hide Magisk
        var System = Java.use("java.lang.System");
        var getProperty = System.getProperty;
        System.getProperty = function(key) {
            var val = getProperty.call(this, key);
            if (key === "ro.build.tags") return "release-keys";
            if (key === "ro.boot.verifiedbootstate") return "green";
            if (key === "ro.build.version.incremental") return "NotAMagiskBuild";
            return val;
        };

        // Block access to /system/framework/XposedBridge.jar
        var File = Java.use("java.io.File");
        File.exists.implementation = function() {
            var path = this.getAbsolutePath();
            if (path.includes("XposedBridge") || 
                path.includes("LSPosed") || 
                path.includes("/data/adb")) {
                console.log("[LSPosed] Hiding: " + path);
                return false;
            }
            return this.exists.call(this);
        };

        // Hide XposedBridge class loading
        var ClassLoader = Java.use("java.lang.ClassLoader");
        var loadClass = ClassLoader.loadClass.bind(ClassLoader);
        ClassLoader.loadClass = function(name, resolve) {
            if (name.includes("XposedBridge") || name.includes("LSPosed")) {
                console.log("[LSPosed] Blocking class load: " + name);
                throw Java.use("java.lang.ClassNotFoundException").$new(name);
            }
            return loadClass(name, resolve);
        };

        // Check for XposedBridge in memory
        try {
            var ProcessBuilder = Java.use("java.lang.ProcessBuilder");
            var start = ProcessBuilder.start;
            ProcessBuilder.start.implementation = function() {
                var cmd = this.command().toString();
                if (cmd.includes("grep") && cmd.includes("Xposed")) {
                    console.log("[LSPosed] Blocking Xposed grep check");
                    throw Java.use("java.io.IOException").$new("Command blocked");
                }
                return start.call(this);
            };
        } catch (e) {}

        console.log("[LSPosed Bypass] Hooks installed");
    });
}, 0);
