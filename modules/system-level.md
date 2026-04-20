# System-Level LSPosed Modules

Advanced modules that modify core Android behavior.

| Module | Description | Risk | Link |
|--------|-------------|------|------|
| **CorePatch** | Disable APK signature verification (install unsigned APKs) | ⚠️ High | [GitHub](https://github.com/LSPosed/CorePatch) |
| **Riru (deprecated)** | System integration framework (most modules now use Zygisk) | ⚠️ High | Historic |
| **Zygisk-Assistant** | Helper framework for Zygisk module development | ✅ Low | [GitHub](https://github.com/topjohnwu/Zygisk-Assistant) |
| **SystemUI Animator** | Custom system animation curves | ✅ Low | XDA |
| **Unified Notification Style** | System-wide notification customization | ✅ Low | XDA |
| **Custom Device Name** | Spoof device model/brand to apps | ⚠️ Medium | Search XDA |

## Installation notes

System-level modules **require full reboot** to take effect. After installation:
```
LSPosed Manager → Modules → [module] → Install/Enable
→ Reboot device
```

---
[← Back to Module Index](README.md)
