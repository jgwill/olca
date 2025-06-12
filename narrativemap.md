# Narrative Map

This repository contains `oLCa`, a CLI assistant built on LangChain and LangGraph.
It focuses on tracing, dataset management, and optional audio helpers from
`coaiapy`. The project is migrating toward LangGraph 0.4 with typed-state support.

## Key Components
- **olca**: main CLI for conversational runs, with `--stream` to display graph output.
- **olca fuse**: wrapper around `coaiapy.fusewill` for Langfuse traces and datasets.
- **olca coaia**: exposes all `coaiapy` commands such as `transcribe`, `summarize`,
  `tash` for Redis snippets, and `p` for process tagging.
- **oiv**: utility for searching and summarizing arXiv papers. Outputs are timestamped
  with `tlid`.
- **state_helpers.py**: placeholder module showing how typed states will be defined
  once the assistant migrates to `StateGraph`.

## Current Direction
The roadmap targets full adoption of LangGraph 0.4, replacing legacy fusewill
modules with `coaiapy` wrappers. Streaming output will expand beyond STDOUT to
websocket or custom handlers. Example notebooks and sample configs will help
users adopt these features. Testing coverage and a minimal CI pipeline are still
pending.

- 2025-06-12: Added `examples/langgraph_agent` demonstrating a minimal
  `StateGraph` chat. Updated the fusewill wrapper to load `coaiamodule`
  automatically and clarified this behavior in the README.

- **llms.txt**: index file guiding LLMs to key docs for retrieval.
