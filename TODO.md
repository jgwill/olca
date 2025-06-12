# TODO

## Documentation Improvements
- [x] Expand README with command summaries and examples
- [x] Document required environment variables
- [x] Describe LangGraph streaming modes
- [x] Include `fusewill --help` and `coaia fuse` examples in docs
- [x] Document `oiv --help` usage
- [x] Document dataset commands via `olca fuse`
- [x] Expand README with example folders under `examples/`
- [x] Add websocket usage example in README
- [x] Publish llms.txt index for documentation
- [x] Document `examples/langgraph_agent` demo
- [x] Provide websocket demo under `examples/websocket_demo`

## Code Enhancements
- [x] Integrate `coaiapy` utilities and remove local `fusewill_utils`
- [x] Replace local `fusewill_cli` with wrapper around `coaia fuse`
- [x] Allow invoking `coaia` commands from `olca` (via `olca coaia`)
- [x] Provide typed-state helpers for `StateGraph` (see `olca/state_helpers.py`)
- [x] Add dependency on `tlid` or drop its usage in `oiv`
- [x] Review argument parsing for `oiv` and update `--help`
- [x] Expose `coaia` audio helpers within the package
- [x] Document usage of `coaia p` for tagging traces
- [x] Document `coaia summarize` and `transcribe` usage
- [x] Fix `olca` CLI imports so the script runs directly from the repo
- [x] Remove legacy FuseWill build steps
- [x] Add test ensuring `coaiamodule` loads via wrapper
 - [*] Investigate checkpointing and subgraph reuse for complex workflows

## LangGraph Upgrade
- [x] Upgrade to `langgraph>=0.4.8`
 - [x] Refactor `olcacli.py` with `StateGraph`
- [x] Add examples for `graph.stream` usage
- [x] Implement `--stream` CLI option with typed state support
- [x] Write tests for graph streaming
 - [x] Document websocket streaming examples
- [x] Integrate typed-state helpers into `olcacli.py`
- [x] Provide sample configs for typed-state streaming

## Testing
- [*] Add unit tests under `tests/`
- [x] Set up CI workflow for linting and `pytest`
