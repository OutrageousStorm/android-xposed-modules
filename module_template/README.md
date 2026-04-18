# LSPosed Module Template

Scaffold for building your own LSPosed modules.

## Structure
```
my_module/
├── module.prop          # Module metadata
├── common/
│   └── system.prop      # Props to inject
├── service.sh           # Service script (runs on boot)
└── hooks.js             # Frida-style hooks
```

## Build
```bash
# Package as ZIP for installation
zip -r my_module.zip *
# Install in LSPosed Manager
```
