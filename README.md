# oLCa

🔊🌿⚙️📜🧠


`oLCa` is an experimental CLI assistant built with LangChain and LangGraph. It focuses on command line interactions, tracing, and human‑in‑the‑loop support. Utilities are provided for managing Langfuse data and summarising arXiv papers. Optional helpers from the `coaiapy` package handle audio transcription and note storage via Redis.

The `coaiapy` dependency is installed automatically with `olca`, but you can also install it manually:
```bash
pip install coaiapy
```

### Glyph Essence
The project glyph represents our transition from legacy scripts to streaming LangGraph workflows:
`🔊🌿⚙️📜🧠`
It appears in CLI output and documentation as a reminder of this evolving architecture.

## Features
- Chat-style CLI using OpenAI or Ollama models
- Optional human-in-the-loop prompts
- Tracing via LangSmith and Langfuse
- `olca fuse` delegates to `coaiapy`'s `fuse` commands for Langfuse traces and datasets
- The wrapper adds the `coaiapy` package directory to `sys.path` so `coaiamodule` loads correctly
- `oiv` command for searching and summarizing arXiv papers
- `oiv` timestamps results with `tlid` for easy cataloging
- Optional `coaia` tools for transcription and `tash` Redis storage
- Optional `coaia summarize` and `coaia p` helpers for quick summaries and tagging
- `olca coaia` exposes all `coaiapy` commands
- `--stream` flag enables multiple streaming output modes
- `--stategraph` flag experiments with typed-state graphs
- `--ws` to stream updates to a websocket URL
- Automated tests run via GitHub Actions CI (triggered on pull requests)
- Experimental typed-state helpers for upcoming `StateGraph` integration. The
  starter graph simply echoes its input (see
    [`examples/typed_state`](examples/typed_state))

## Installation
```bash
pip install olca
```

Optional extras install tracing support:
```bash
pip install 'olca[tracing]'
```

For Android devices using Termux, see [README.termux.md](README.termux.md) for
additional setup notes.

## Quick Start
```bash
olca init            # create olca.yml in the current directory
olca -T              # run with tracing enabled
olca --stream values # custom streaming output
```
Use `-H` to activate human mode or `--help` to see full options. When running
from a clone without installing, invoke the script with
`python olca/olcacli.py`.

## CLI commands
| Command    | Purpose                                                     |
|------------|-------------------------------------------------------------|
| `olca`     | Interactive agent using LangChain/LangGraph                 |
| `olca fuse` | Manage Langfuse traces via `coaiapy`                       |
| `oiv`      | Query arXiv and generate summaries                          |
| `coaia`    | (optional) audio utilities and Redis `tash` helper          |
| `olca coaia` | Run `coaiapy` commands through the `olca` wrapper         |

`olca fuse` forwards all arguments to `coaia fuse`, so you can reuse existing
FuseWill commands without changing your workflow.

### Command references
Run each command with `--help` to see full options:
```bash
olca --help
olca fuse --help
oiv --help
coaia --help
```

Examples:
```bash
olca -H -T                       # interactive run with tracing
olca fuse list_traces -L 5       # show recent traces
olca fuse datasets list          # list available datasets
olca fuse datasets create demo   # create a dataset for traces
olca fuse datasets add-run demo 1234  # attach run ID 1234
oiv -I "quantum computing"       # search arXiv
oiv -I "ai" -P result-           # prefix results with 'result-' timestamp
coaia transcribe sample.wav      # audio transcription
coaia tash project::notes < README.md  # stash notes to Redis
olca coaia transcribe sample.wav # same as above via olca wrapper
coaia p summarizer::demo < README.md   # tag process with custom label
coaia summarize README.md          # quick document summary
olca coaia p summarizer::demo < README.md
olca fuse --help           # detailed options for FuseWill
coaia fuse --help          # discover extra Langfuse utilities
oiv --help                 # view oiv arguments
olca --stategraph -T       # try the experimental typed StateGraph
olca --stream updates --ws ws://localhost:8000 # stream to websocket
```

`coaia transcribe` converts audio files to text, while `coaia summarize` can
quickly produce a condensed version of any document. The `coaia p` command lets
you tag an input message with a custom label—useful for tracking metrics or
annotating traces. All these commands are also accessible via `olca coaia`.

More scenarios are available in the [`examples/`](examples/) directory.

Example folders:
- `examples/quickstart` – minimal config for a first run
- `examples/dataset` – using `olca fuse` dataset helpers
- `examples/oiv_demo` – summarizing arXiv results
- `examples/typed_state` – work-in-progress typed state graph
  (see `examples/typed_state/olca.yml` for a sample config)
- `examples/langgraph_agent` – prototype fused LangGraph chat that streams
  responses while tracing to Langfuse
- `examples/websocket_demo` – run a simple server to receive streamed updates

## Environment Variables
- `OPENAI_API_KEY` for OpenAI models
- `LANGFUSE_PUBLIC_KEY`, `LANGFUSE_SECRET_KEY`, `LANGFUSE_HOST` for Langfuse
- `LANGCHAIN_API_KEY` for LangSmith tracing
- `KV_REST_API_URL`, `KV_REST_API_TOKEN` for `coaia tash`
Store them in a `.env` file or your shell profile. `coaia` commands rely on
Redis variables (`KV_REST_API_URL` and `KV_REST_API_TOKEN`) to stash text
snippets and metrics.
`oiv` stores search results in `./output` with a `tlid` timestamp, so runs
are easy to organize without extra configuration.

## Example `olca.yml`
```yaml
api_keyname: OPENAI_API_KEY
human: true
model_name: gpt-4o-mini
recursion_limit: 50
tracing: true
tracing_providers:
  - langsmith
  - langfuse
system_instructions: |
  You are a helpful terminal agent.
user_input: |
  Say hello then exit.
```

## Streaming modes
`olca` supports LangGraph 0.4 streaming APIs. Use the `--stream` flag to select
the output style: `updates`, `values`, `custom`, or `messages`. The default
mirrors the traditional behavior using `graph.stream` with updates written to
STDOUT.

Set `--ws ws://localhost:8000` to forward each update to a websocket in
addition to printing to the console.

An additional `--stategraph` flag enables an experimental typed-state graph
implementation. When this flag is provided, `olca` attempts to compile a
`StateGraph` from `olca.state_helpers` and falls back to the classic agent if
the graph isn't fully defined.

Example:
```bash
olca --stream updates
```
For a sample typed-state configuration, see
`examples/typed_state/olca.yml`.
The current demo graph simply echoes the conversation state and will be
expanded as LangGraph support matures.

## Integrations and roadmap
The project is migrating to LangGraph 0.4.x to support streaming via
`StateGraph` and asynchronous `graph.stream` calls. Local `fusewill`
helpers have been replaced by the `fuse` commands in `coaiapy` for a consistent Langfuse
experience. Upcoming releases will introduce typed-state helpers so
agents can declare structured inputs and outputs (see
[`olca/state_helpers.py`](olca/state_helpers.py)). See [`ROADMAP.md`](ROADMAP.md)
for full details. Dataset utilities for tagging or grouping traces are
available via `olca fuse datasets`, mirroring `coaia fuse`.
Typed-state examples and websocket helpers continue to evolve.
Future work explores checkpointing and subgraph reuse to support long-running
workflows.

The `llms.txt` file indexes these docs for language-model retrieval.


