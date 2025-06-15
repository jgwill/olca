# WebSocket Streaming Demo

This example shows how to forward LangGraph updates from `olca` to a WebSocket server.
Use the companion script `server.py` to print incoming messages.

## Start the server
```bash
python server.py
```
The server listens on `ws://localhost:8765`.

## Run olca with websocket streaming
```bash
olca --ws ws://localhost:8765 --stream updates
```
You should see each streamed token appear in the server console.
