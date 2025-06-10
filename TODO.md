# TODO

## Documentation Improvements
- [x] Expand README with command summaries and examples
- [x] Document required environment variables
- [x] Describe LangGraph streaming modes
- [x] Include `fusewill --help` and `coaia fuse` examples in docs
- [x] Document `oiv --help` usage

## Code Enhancements
- [x] Integrate `coaiapy` utilities and remove local `fusewill_utils`
- [x] Replace local `fusewill_cli` with wrapper around `coaia fuse`
- [ ] Allow invoking `coaia` commands from `olca`
- [ ] Provide typed-state helpers for `StateGraph`
- [ ] Add dependency on `tlid` or drop its usage in `oiv`
- [ ] Review argument parsing for `oiv` and update `--help`
- [ ] Expose `coaia` audio helpers within the package

## LangGraph Upgrade
- [x] Upgrade to `langgraph>=0.4.8`
- [ ] Refactor `olcacli.py` with `StateGraph`
- [ ] Add examples for `graph.stream` usage
- [ ] Implement `--stream` CLI option with typed state support
- [ ] Write tests for graph streaming

## Testing
- [ ] Add unit tests under `tests/`
- [ ] Set up CI workflow for linting and `pytest`
