#!/usr/bin/env bash

# Setup test environment
CONFIG_FILE="olca_qstash_test.yml"
SESSION_ID="qstash_test_session"
SESSION_DIR="$HOME/.olca_sessions"
TEST_TOPIC="olca-test-topic"

# Check if real token is available, otherwise use dummy
if [ -z "$QSTASH_TOKEN" ]; then
    echo "No QSTASH_TOKEN found in environment, using dummy token"
    export QSTASH_TOKEN="dummy_qstash_token"
fi

# Create test config
cat > $CONFIG_FILE << EOF
api_keyname: OPENAI_API_KEY
model_name: gpt-4o-mini
recursion_limit: 12
temperature: 0
system_instructions: You are a helpful assistant for QStash testing.
user_input: Process QStash messages.
qstash:
  enabled: true
  topic: $TEST_TOPIC
redis_upstash:
  enabled: true
  url: redis://localhost:6379
EOF

# Set session ID
echo $SESSION_ID > OLCA_SESSION_ID

# Clean any existing session file
rm -f "$SESSION_DIR/$SESSION_ID.json" 2>/dev/null

# Test sending a message to QStash
echo "Testing sending message to QStash..."
if [ "$QSTASH_TOKEN" != "dummy_qstash_token" ]; then
    # Only attempt real API call if we have a real token
    RESPONSE=$(curl -s -X POST "https://qstash.upstash.io/v1/publish/topic/$TEST_TOPIC" \
        -H "Authorization: Bearer $QSTASH_TOKEN" \
        -H "Content-Type: application/json" \
        -d "{\"session_id\": \"$SESSION_ID\", \"message\": \"Test message\", \"timestamp\": \"$(date +%s)\"}")
    
    if echo "$RESPONSE" | grep -q "messageId"; then
        echo "PASS: Successfully sent message to QStash topic: $TEST_TOPIC"
        MESSAGE_ID=$(echo "$RESPONSE" | grep -o '"messageId":"[^"]*"' | cut -d'"' -f4)
        echo "Message ID: $MESSAGE_ID"
    else
        echo "FAIL: Failed to send message to QStash"
        echo "Response: $RESPONSE"
    fi
else
    echo "SKIP: Using dummy token, not sending actual message"
fi

# Test receiving messages
echo "Testing receiving messages from QStash..."
mv olca.yml olca.yml.bak 2>/dev/null
cp $CONFIG_FILE olca.yml

# Run OLCA which should process QStash messages
if [ "$QSTASH_TOKEN" != "dummy_qstash_token" ]; then
    timeout 10s olca &
    PID=$!
    
    # Give it time to process messages
    sleep 5
    
    # Check if it processed the message
    if [ -f "$SESSION_DIR/$SESSION_ID.json" ]; then
        echo "PASS: Session file was created from QStash message"
    else
        echo "FAIL: Session file was not created from QStash message"
    fi
    
    # Kill OLCA if still running
    if ps -p $PID > /dev/null; then
        kill $PID
    fi
else
    echo "Simulating QStash message reception with dummy data..."
    # Create a dummy session file to simulate receiving a message
    mkdir -p "$SESSION_DIR"
    echo "{\"last_message\": \"Test QStash message\", \"timestamp\": \"$(date +%s)\"}" > "$SESSION_DIR/$SESSION_ID.json"
    
    # Run OLCA briefly to test processing
    timeout 5s olca &
    PID=$!
    sleep 3
    
    if ps -p $PID > /dev/null; then
        kill $PID
    fi
    
    echo "SIMULATED: QStash message reception"
fi

# Clean up
rm -f OLCA_SESSION_ID
rm -f $CONFIG_FILE
[ -f olca.yml.bak ] && mv olca.yml.bak olca.yml || rm -f olca.yml
echo "QStash integration test completed"
