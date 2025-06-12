# Roadmap

Upcoming improvements for `oLCa`.

## LangGraph 0.4 Migration
- [x] Upgrade dependency to `langgraph>=0.4.8` and audit breaking changes.
 - [x] Refactor graph creation to use the `StateGraph` APIs.
- [x] Leverage streaming modes (`updates`, `values`, `custom`, `messages`).
- [x] Add examples for `graph.stream` with asynchronous iteration and callbacks.
- [ ] Investigate checkpointing and subgraph reuse for complex workflows.
- [x] CLI now exposes a `--stream` flag for custom streaming modes.
- [x] Provide typed state helpers so handlers can declare input/output types.
  A new module (`olca/state_helpers.py`) introduces a skeleton `ConversationState`
  and `create_state_graph` function as a starting point.
 - [x] Offer utilities for streaming output to STDOUT or websockets.
 - [x] Prepare example notebooks demonstrating 0.4 features and typed states.
 - [x] Provide sample configs under `examples/` for streaming with `StateGraph`.
 - [x] Integrate typed-state helpers into `olcacli.py` for safer graph transitions.
 - [x] Document websocket streaming utilities once LangGraph 0.4 features stabilize.

## FuseWill from `coaiapy`
- [x] Replace local `fusewill_utils` with `coaiapy.fusewill`.
- [x] Import the `fusewill` CLI entry point from that package.
- [x] Keep backward compatibility with existing commands.
- [x] Document new options provided by `coaia fuse` and dataset helpers.
- [x] Replace `fusewill_cli.py` with thin wrappers around `coaiapy.cofuse`.
- [x] Sync README examples with `coaiapy` fusewill usage.
- [x] Add wrappers so `olca fuse` calls directly into `coaiapy` modules.
- [x] Provide an `olca coaia` subcommand to invoke any `coaiapy` CLI action.
- [x] Outline dataset utilities available through `coaia fuse --help`.
- [x] Provide example scripts in `examples/` showing `olca fuse` with datasets.
- [x] Consider additional helpers like `coaia p` for tagging traces.
- [x] Remove legacy build steps that copied FuseWill sources.

## Extra Utilities
- [x] Support `coaia tash` for storing text notes in Redis.
- [x] Expose `coaia transcribe` and `coaia summarize` via `olca` scripts.
- [x] Evaluate `coaia p` for process tagging and metrics.
- [x] Document required Redis variables for `coaia` helpers.
- [x] Document how `oiv` uses `tlid` timestamps to organize output files.
- [x] Ensure `olcacli.py` imports work when run directly from source.

## Testing and CI
- [ ] Add unit tests for all CLI commands.
- [ ] Configure CI to run `pytest` and style checks.
