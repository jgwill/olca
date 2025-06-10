# Roadmap

Upcoming improvements for `oLCa`.

## LangGraph 0.4 Migration
- Upgrade dependency to `langgraph>=0.4.8`.
- Refactor graph creation to use the `StateGraph` APIs.
- Leverage streaming modes (`updates`, `values`, `custom`, `messages`).
- Add examples for `graph.stream` with asynchronous iteration.
- Investigate checkpointing and subgraph reuse for complex workflows.
- Update CLI to expose a `--stream` flag and document streaming modes.
- Explore typed state definitions for safer graphs.

## FuseWill from `coaiapy`
- Remove local `fusewill_utils` in favour of `coaiapy.fusewill`.
- Import `fusewill` CLI entry point from the package.
- Ensure backward compatibility with existing commands.
- Document new options provided by `coaia fuse`.
- Sync README examples with `coaiapy` fusewill usage.
- Provide wrappers so `olca fuse` calls directly into `coaiapy`.

## Extra Utilities
- Support `coaia tash` for storing text notes in Redis.
- Expose `coaia transcribe` and `coaia summarize` via `olca` scripts.
- Evaluate `coaia p` for process tagging and metrics.
- Document required Redis variables for `coaia` helpers.

## Testing and CI
- Add unit tests for all CLI commands.
- Configure CI to run `pytest` and style checks.
