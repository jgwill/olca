#!/usr/bin/env bash

SESSION_ID="test_session"
SESSION_DIR="$HOME/.olca_sessions"

echo "Testing Persistent Sessions"
rm -f $SESSION_DIR/$SESSION_ID.json 2>/dev/null
olca --temp-session
[ -f "$SESSION_DIR/$SESSION_ID.json" ] && echo "Session found unexpectedly!" || echo "Temp session removed as expected"

echo "Creating new persistent session..."
olca
[ -f "$SESSION_DIR/$SESSION_ID.json" ] && echo "Persistent session created successfully" || echo "Failed to create persistent session"
