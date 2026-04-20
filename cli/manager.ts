/**
 * manager.ts -- LSPosed module manager CLI
 * Compile: npx tsc manager.ts
 * Usage: node manager.js list
 *        node manager.js search Hide
 *        node manager.js enable com.example.module
 *        node manager.js disable com.example.module
 */

import { exec } from "child_process";
import { promisify } from "util";

const execAsync = promisify(exec);

interface Module {
    name: string;
    pkg: string;
    version: string;
    enabled: boolean;
    scope: string[];
}

async function adb(cmd: string): Promise<string> {
    try {
        const { stdout } = await execAsync(`adb shell ${cmd}`);
        return stdout.trim();
    } catch (e) {
        return "";
    }
}

async function listModules(): Promise<Module[]> {
    const output = await adb("pm list packages");
    const packages = output.split("\n").map(l => l.replace("package:", ""));
    
    // Filter to known Xposed-related packages
    const xposedPkgs = packages.filter(p => 
        p.includes("xposed") || p.includes("lsposed") || p.includes("module") ||
        p === "com.example.hide_my_applist" || p === "org.lsposed" ||
        p === "com.github.kyuubiran.ezxposed"
    );

    return xposedPkgs.map(pkg => ({
        name: pkg.split(".").pop() || pkg,
        pkg,
        version: "unknown",
        enabled: true,
        scope: [],
    }));
}

async function searchModules(keyword: string): Promise<Module[]> {
    const all = await listModules();
    return all.filter(m => m.name.toLowerCase().includes(keyword.toLowerCase()));
}

async function enableModule(pkg: string): Promise<void> {
    await adb(`pm enable ${pkg}`);
    console.log(`✅ Enabled: ${pkg}`);
}

async function disableModule(pkg: string): Promise<void> {
    await adb(`pm disable ${pkg}`);
    console.log(`✅ Disabled: ${pkg}`);
}

async function main() {
    const args = process.argv.slice(2);
    const cmd = args[0];
    const arg = args[1];

    switch (cmd) {
        case "list":
            const modules = await listModules();
            console.log(`Found ${modules.length} modules:\n`);
            modules.forEach(m => {
                console.log(`  ${m.enabled ? "✓" : "✗"} ${m.name} (${m.pkg})`);
            });
            break;
        
        case "search":
            const results = await searchModules(arg || "");
            console.log(`Search results for "${arg}":\n`);
            results.forEach(m => {
                console.log(`  ${m.name} (${m.pkg})`);
            });
            break;
        
        case "enable":
            await enableModule(arg || "");
            break;
        
        case "disable":
            await disableModule(arg || "");
            break;
        
        default:
            console.log("Usage:");
            console.log("  manager list          -- List all installed modules");
            console.log("  manager search <kw>   -- Search modules");
            console.log("  manager enable <pkg>  -- Enable module");
            console.log("  manager disable <pkg> -- Disable module");
    }
}

main().catch(console.error);
