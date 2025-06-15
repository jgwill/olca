# Persistent Session Example

This example demonstrates how to keep conversation history across runs
using ``InMemoryStore`` and ``MemorySaver`` from LangGraph.

Run with a user identifier to persist memories:

```bash
python main.py --user bob "Hello there"
python main.py --user bob "Remember my name"
python main.py --user bob "What do you know about me?"
```
