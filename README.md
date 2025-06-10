# oLCa

`oLCa` is an experimental CLI assistant built with LangChain and LangGraph. It focuses on command line interactions, tracing, and human in the loop support. The project also ships utilities for managing Langfuse data and working with arXiv papers. Additional helpers from the `coaiapy` package can be used for audio tasks and storing snippets in Redis.

## Features
- Chat-style CLI using OpenAI or Ollama models
- Optional human-in-the-loop prompts
- Tracing via LangSmith and Langfuse
- `olca fuse` wraps `coaiapy.fusewill` for Langfuse traces and datasets
- `oiv` command for searching and summarizing arXiv papers
- Optional `coaia` tools for transcription and `tash` Redis storage

## Installation
```bash
pip install olca
```

## Quick Start
```bash
olca init            # create olca.yml in the current directory
olca -T              # run with tracing enabled
```
Use `-H` to activate human mode or `--help` to see full options.

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
oiv -I "quantum computing"       # search arXiv
coaia transcribe sample.wav      # audio transcription
coaia tash project::notes < README.md  # stash notes to Redis
olca coaia transcribe sample.wav # same as above via olca wrapper
olca fuse --help           # detailed options for FuseWill
coaia fuse --help          # discover extra Langfuse utilities
oiv --help                 # view oiv arguments
```

## Environment Variables
- `OPENAI_API_KEY` for OpenAI models
- `LANGFUSE_PUBLIC_KEY`, `LANGFUSE_SECRET_KEY`, `LANGFUSE_HOST` for Langfuse
- `LANGCHAIN_API_KEY` for LangSmith tracing
- `KV_REST_API_URL`, `KV_REST_API_TOKEN` for `coaia tash`
Store them in a `.env` file or your shell profile. `coaia` commands rely on
Redis variables (`KV_REST_API_URL` and `KV_REST_API_TOKEN`) to stash text
snippets and metrics.

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
`olca` will adopt LangGraph 0.4 streaming APIs. A forthcoming `--stream` flag
lets you choose between output types:
`updates`, `values`, `custom`, or `messages`. The default mirrors current
behavior using `graph.stream` with updates written to STDOUT.

Example:
```bash
olca --stream updates
```

## Integrations and roadmap
The project is migrating to LangGraph 0.4.x to support streaming via
`StateGraph` and asynchronous `graph.stream` calls. Local `fusewill`
helpers will be replaced by `coaiapy.fusewill` for a consistent Langfuse
experience. See [`ROADMAP.md`](ROADMAP.md) for full details.
