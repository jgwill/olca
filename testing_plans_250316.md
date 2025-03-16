# OLCA Testing Plans 🚀

## What is OLCA?

OLCA (Orpheus Langchain CLI Assistant) is an AI assistant that works in your terminal. It can remember conversations even after you close it!

## What We're Testing

We're testing if OLCA can:
- Save your conversations ✅
- Load old conversations when you start it again ✅
- Share conversations between different folders ✅
- Send and receive messages using QStash ✅

## Test Scripts

Here are the test scripts and what they do:

### 1. Test Persistent Sessions

This test checks if OLCA can save and load your conversations.

```bash
cd /usr/local/src/20-olca-add-persistent-session-memory
./tests/test_persistent_sessions.sh
```

What happens:
1. Creates a test session ID
2. Runs OLCA with `--temp-session` (should NOT save anything)
3. Runs OLCA normally (should save conversations)
4. Checks if the conversation was saved correctly

### 2. Test Parent Inheritance

This test checks if OLCA can use a parent folder's conversation.

```bash
cd /usr/local/src/20-olca-add-persistent-session-memory
./tests/test_parent_inheritance.sh
```

What happens:
1. Creates a parent folder with an OLCA session
2. Creates a child folder inside it
3. Runs OLCA in the child folder
4. Checks if it used the parent's session

### 3. Test Session Save Interval

This test checks if OLCA saves conversations at regular intervals.

```bash
cd /usr/local/src/20-olca-add-persistent-session-memory
./tests/test_session_save_interval.sh
```

What happens:
1. Creates a test configuration with 5-second save interval
2. Runs OLCA for 10 seconds
3. Checks if it saved the session automatically

### 4. Test QStash Integration

This test checks if OLCA can send and receive messages using QStash.

```bash
cd /usr/local/src/20-olca-add-persistent-session-memory
./tests/test_qstash.sh
```

What happens:
1. Sets up a test environment for QStash
2. Sends a test message to QStash
3. Runs OLCA to see if it can receive the message
4. Checks if it processed the message correctly

## How to Run All Tests

Run this command to test everything at once:

```bash
cd /usr/local/src/20-olca-add-persistent-session-memory
for test in tests/test_*.sh; do
  echo "========== Running $test =========="
  bash "$test"
  echo
done
```

## What Success Looks Like

When tests pass, you'll see messages like:
- "PASS: Temp session not persisted"
- "PASS: Persistent session created successfully"
- "PASS: Successfully sent message to QStash"

If something fails, you'll see messages starting with "FAIL:"

## Advanced: Making Your Own Tests

Want to create your own tests? It's easy!

1. Create a new file in the `tests` folder (name it `test_something.sh`)
2. Make it executable: `chmod +x test_something.sh`
3. Write your test commands
4. Run it: `./tests/test_something.sh`

Have fun testing! 🎮
