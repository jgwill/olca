# Narrative Map

This branch refactors oLCa to rely on the coaiapy package and upgrades to LangGraph 0.4.8. Streaming via websockets is now documented and the CLI exposes new helpers such as `olca coaia`. Examples illustrate dataset management, typed-state graphs, and a prototype LangGraph chat agent.

## Commit Timeline
- e2dc954: consolidated docs, introduced coaiapy wrappers, and added example folders
- bce8540: clarified LangGraph example references, introduced the project glyph, and recorded docs index
- 7b50f1e: refactored fusewill wrapper, improved README, and added typed-state helpers
- 7646734: added websocket streaming docs, CI workflow, and llms index
- 1563243: websocket demo example and checkpointing notes
- c182195: CI workflow refined and help tests added
- 9169c89: documented screenshot narrative generation using OLCA Vision
- 2b6ef4e: implemented narrative generation from screenshots with Vision AI
- b8e2c2e: merged main into work, bringing tests and typed-state support
- f9d5f2a: added kid-friendly tutorial and ledger reference in README
- a669f0a: packaged helper utilities under codecs_package for easy installation
- 19eb124: fix olca CLI import path and add help test
- 3e03b33: documented publishing steps and logged failed TestPyPI attempt
