#!/usr/bin/env bash

SESSION_ID="test_session"
SESSION_DIR="$HOME/.olca_sessions"

echo "Testing Persistent Sessions"
echo $SESSION_ID > OLCA_SESSION_ID
mkdir -p $SESSION_DIR

# Clean any existing session
rm -f $SESSION_DIR/$SESSION_ID.json 2>/dev/null

echo "Testing temporary session..."
olca --temp-session
[ -f "$SESSION_DIR/$SESSION_ID.json" ] && echo "ERROR: Session persisted despite temp flag!" || echo "PASS: Temp session not persisted"

echo "Creating new persistent session..."
echo "test data" > .olca/test_data.txt
olca <<< "exit"

if [ -f "$SESSION_DIR/$SESSION_ID.json" ]; then
    echo "PASS: Persistent session created successfully"
    grep -q "test_data" "$SESSION_DIR/$SESSION_ID.json" && echo "PASS: Session contains expected data" || echo "FAIL: Session missing expected data"
else
    echo "FAIL: Failed to create persistent session"
fi

# Clean up
rm -f OLCA_SESSION_ID
