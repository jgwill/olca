#!/usr/bin/env bash

CONFIG_FILE="olca.yml"
SESSION_DIR="$HOME/.olca_sessions"
SESSION_ID="interval_test_session"

# Create a test config with custom save interval (5 seconds)
cat > $CONFIG_FILE << EOF
api_keyname: OPENAI_API_KEY
model_name: gpt-4o-mini
recursion_limit: 12
temperature: 0
human: true
tracing: true
system_instructions: You are a helpful assistant.
user_input: Help me test session saving.
session_save_interval: 5
session_directory: $SESSION_DIR
EOF

echo $SESSION_ID > OLCA_SESSION_ID

# Run OLCA for 10 seconds to trigger at least one save
echo "Running OLCA with 5 second save interval..."
timeout 10s olca &
PID=$!

echo "Waiting for session saves..."
sleep 12

# Kill OLCA if still running
if ps -p $PID > /dev/null; then
    kill $PID
fi

# Check if session file exists and was updated recently
if [ -f "$SESSION_DIR/$SESSION_ID.json" ]; then
    MODIFIED=$(stat -c %Y "$SESSION_DIR/$SESSION_ID.json")
    NOW=$(date +%s)
    AGE=$((NOW - MODIFIED))
    
    if [ $AGE -lt 15 ]; then
        echo "SUCCESS: Session was saved recently (${AGE}s ago)"
    else
        echo "FAIL: Session file exists but wasn't updated recently (${AGE}s ago)"
    fi
else
    echo "FAIL: Session file wasn't created"
fi

# Clean up
rm -f OLCA_SESSION_ID
rm -f $CONFIG_FILE
