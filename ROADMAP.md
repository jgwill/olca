# Roadmap

Upcoming improvements for `oLCa`.

## LangGraph 0.4 Migration
- Upgrade dependency to `langgraph>=0.4.8` and audit breaking changes.
- Refactor graph creation to use the `StateGraph` APIs.
- Leverage streaming modes (`updates`, `values`, `custom`, `messages`).
- Add examples for `graph.stream` with asynchronous iteration and callbacks.
- Investigate checkpointing and subgraph reuse for complex workflows.
- Update CLI to expose a `--stream` flag and document streaming modes.
- Provide typed state helpers so handlers can declare input/output types.
- Offer utilities for streaming output to STDOUT or websockets.
- Prepare example notebooks demonstrating 0.4 features and typed states.
- Integrate typed-state helpers into `olcacli.py` for safer graph transitions.

## FuseWill from `coaiapy`
- Replace local `fusewill_utils` with `coaiapy.fusewill`.
- Import the `fusewill` CLI entry point from that package.
- Keep backward compatibility with existing commands.
- Document new options provided by `coaia fuse` and dataset helpers.
- Replace `fusewill_cli.py` with thin wrappers around `coaiapy.cofuse` (done).
- Sync README examples with `coaiapy` fusewill usage.
- Add wrappers so `olca fuse` calls directly into `coaiapy` modules.
- Provide an `olca coaia` subcommand to invoke any `coaiapy` CLI action.
- Outline dataset utilities available through `coaia fuse --help`.
- Consider additional helpers like `coaia p` for tagging traces.

## Extra Utilities
- Support `coaia tash` for storing text notes in Redis.
- Expose `coaia transcribe` and `coaia summarize` via `olca` scripts.
- Evaluate `coaia p` for process tagging and metrics.
- Document required Redis variables for `coaia` helpers.
- Document how `oiv` uses `tlid` timestamps to organize output files.

## Testing and CI
- Add unit tests for all CLI commands.
- Configure CI to run `pytest` and style checks.
