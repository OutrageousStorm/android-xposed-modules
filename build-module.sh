#!/bin/bash
# build-module.sh -- Template for building LSPosed modules
# Usage: ./build-module.sh module_name
# Creates a starter module structure with all necessary files

set -e

MODULE_NAME="${1:?Usage: $0 module_name}"
MODULE_ID=$(echo "$MODULE_NAME" | tr '[:upper:]' '[:lower:]' | tr ' ' '_')
PACKAGE="com.example.$MODULE_ID"

echo "Creating LSPosed module: $MODULE_NAME"
mkdir -p "$MODULE_ID"
cd "$MODULE_ID"

# module.prop
cat > module.prop << EOF
id=$MODULE_ID
name=$MODULE_NAME
version=1.0
versionCode=1
author=OutrageousStorm
description=LSPosed module for $MODULE_NAME
updateJson=
EOF

# post-fs-data.sh
cat > post-fs-data.sh << 'HOOK'
#!/system/bin/sh
# Called in post-fs-data mode
# Can be used for initialization
MODDIR=${0%/*}
HOOK

# service.sh
cat > service.sh << 'HOOK'
#!/system/bin/sh
# Called in late_start service mode
# Good place for background tasks
MODDIR=${0%/*}
HOOK

# system.prop
cat > system.prop << 'EOF'
# System properties for this module
EOF

# hooks.sh (for Zygisk/LSPosed integration)
cat > hooks.sh << 'HOOK'
#!/bin/bash
# Zygisk hooks configuration
# This file is sourced by the build system

# Define what you want to modify:
# - HOOKS=(class_name method_name replacement)
# - Or provide a .jar with bytecode patches

HOOKS=()
HOOK

# README
cat > README.md << 'EOF'
# $MODULE_NAME

An LSPosed module for Android.

## Features
- Feature 1
- Feature 2

## Requirements
- Android 11+
- LSPosed Framework
- Zygisk (preferred) or Riru

## Installation
1. Install LSPosed via Magisk
2. Install this module from LSPosed Manager
3. Reboot

## Configuration
Check LSPosed Manager for scope and settings.
EOF

chmod +x post-fs-data.sh service.sh hooks.sh

echo ""
echo "✅ Module created: $MODULE_ID"
echo "   Files:"
ls -lh
echo ""
echo "Next steps:"
echo "  1. Edit module.prop with your details"
echo "  2. Modify hooks.sh with your patches"
echo "  3. Test via LSPosed Manager"
