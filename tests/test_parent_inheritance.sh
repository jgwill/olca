#!/usr/bin/env bash

SESSION_DIR="$HOME/.olca_sessions"
EXPORT_FILE="sessions_export.json"
mkdir -p parent/child
cd parent
echo "Initializing session in parent directory..."
olca
cd child
echo "Testing parent session inheritance..."
olca
cd ..
echo "Exporting sessions..."
olca export_sessions $EXPORT_FILE
[ -f "$EXPORT_FILE" ] && echo "Export successful: $EXPORT_FILE" || echo "Export failed"
