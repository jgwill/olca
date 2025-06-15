# QStash Integration Demo

This example shows how to trigger `olca` sessions using [Upstash QStash](https://upstash.com/docs/qstash).

## Configuration
Copy the sample configuration and edit the topic name:

```bash
cp olca.yml.sample olca.yml  # or `olca init` then edit
```
Add these entries to `olca.yml`:

```yaml
qstash:
  enabled: true
  topic: YOUR_TOPIC_NAME
redis_upstash:
  enabled: true
  url: redis://localhost:6379
```

Set the `QSTASH_TOKEN` environment variable with your Upstash token.

## Send a message
Publish a message referencing a session ID:

```bash
curl -X POST "https://qstash.upstash.io/v1/publish/topic/YOUR_TOPIC_NAME" \
  -H "Authorization: Bearer $QSTASH_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"session_id": "demo_session", "message": "start"}'
```

## Run olca
Run the CLI and it will fetch the message and load the session state from Redis:

```bash
olca
```

If a session state exists under `demo_session`, olca will resume with that state.
