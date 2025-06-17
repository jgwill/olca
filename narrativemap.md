# Narrative Map

This branch refactors oLCa to rely on the coaiapy package and upgrades to LangGraph 0.4.8. Streaming via websockets is now documented and the CLI exposes new helpers such as `olca coaia`. Examples illustrate dataset management, typed-state graphs, and a prototype LangGraph chat agent.

## Commit Timeline
- e2dc954: consolidated docs, introduced coaiapy wrappers, and added example folders
- bce8540: clarified LangGraph example references, introduced the project glyph, and recorded docs index
- 7b50f1e: refactored fusewill wrapper, improved README, and added typed-state helpers
- 7646734: added websocket streaming docs, CI workflow, and llms index
- 1563243: websocket demo example and checkpointing notes
- c182195: CI workflow refined and help tests added
- 1240fa6: added Termux installation guide and stripped grpc dependencies
- f9a4ee4: ledger documenting Termux support
- 0259abcd: optional dependencies for tracing and graceful Langfuse import
- 7a88c45: extras instructions and ledger for Termux support
- 0a3cc5b: guarded CLI imports and clarified installation docs
- a889152: added dotenv dependency and guards for Termux CLI stability
