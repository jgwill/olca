# Roadmap

This document outlines upcoming improvements for oLCa.

## LangGraph Upgrade
- Update to `langgraph` 0.4.x to use new streaming modes such as `updates`, `values`, `custom`, and `messages`.
- Explore subgraph support and checkpointing.

## FuseWill Integration
- Replace local `fusewill_utils` with the implementation provided by the `coaiapy` package.
- Leverage `coaia fuse` subcommands for managing Langfuse data.

## Additional Tools
- Use `coaia tash` for stashing text into Redis.
- Incorporate `coaia transcribe` and `coaia summarize` for audio processing pipelines.

## Testing & CI
- Add tests for each CLI command and enable continuous integration.

