# Roadmap

This document outlines upcoming improvements for oLCa.

## LangGraph Upgrade
- Update to `langgraph` 0.4.x to use new streaming modes such as `updates`, `values`, `custom`, and `messages`.
- Explore subgraph support and checkpointing.
- Document the expected migration path from the current graph usage.
- Provide examples that showcase streaming output with `graph.stream`.

## FuseWill Integration
- Replace local `fusewill_utils` with the implementation provided by the `coaiapy` package.
- Leverage `coaia fuse` subcommands for managing Langfuse data.
- Pull helper functions from `coaiapy.fusewill` to reduce maintenance.
- Add compatibility shims to keep old commands working.

## Additional Tools
- Use `coaia tash` for stashing text into Redis.
- Incorporate `coaia transcribe` and `coaia summarize` for audio processing pipelines.
- Evaluate `coaia p` for custom process tags.
- Document required Redis variables like `KV_REST_API_URL` and `KV_REST_API_TOKEN`.

## Testing & CI
- Add tests for each CLI command and enable continuous integration.

