# TODO

## Documentation Improvements
- [ ] Expand README with command summaries (done in this PR).
- [ ] Provide usage examples for each CLI tool (`olca`, `fusewill`, `oiv`).
- [ ] Document required environment variables in more detail.

## Code Enhancements
- [ ] Add package dependency for `tlid` or remove requirement from `oiv` to avoid import errors.
- [ ] Review CLI argument parsing for `oiv` and provide `--help` output.
- [ ] Implement missing TODO functions in `fusewill_utils.py` (upload_url, get_media, get_daily_metrics).

## LangGraph Upgrade
- [ ] Verify compatibility with LangGraph `0.4.8` which introduces streaming modes (`updates`, `values`, `custom`, `messages`).
- [ ] Refactor `olcacli.py` to leverage newer `StateGraph` APIs if beneficial.
- [ ] Add tests covering graph execution and streaming behaviors.

## Testing
- [ ] Integrate automated tests under `tests/` to exercise CLI commands.
- [ ] Set up CI workflow for linting and pytest.

