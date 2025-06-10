# oLCa

`oLCa` is an experimental CLI assistant built with LangChain and LangGraph. It focuses on command line interactions, tracing, and human in the loop support. The project also ships utilities for managing Langfuse data and working with arXiv papers. Additional helpers from the `coaiapy` package can be used for audio tasks and storing snippets in Redis.

## Features
- Chat-style CLI using OpenAI or Ollama models
- Optional human-in-the-loop prompts
- Tracing via LangSmith and Langfuse
- `fusewill` wrapper for Langfuse traces, datasets and prompts
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
| `fusewill` | Manage Langfuse traces and datasets                         |
| `oiv`      | Query arXiv and generate summaries                          |
| `coaia`    | (optional) audio utilities and Redis `tash` helper          |

Examples:
```bash
olca -H -T
fusewill list_traces -L 5
oiv -I "quantum computing"
coaia transcribe sample.wav
coaia tash project::notes < README.md
```

## Environment Variables
- `OPENAI_API_KEY` for OpenAI models
- `LANGFUSE_PUBLIC_KEY`, `LANGFUSE_SECRET_KEY`, `LANGFUSE_HOST` for Langfuse
- `LANGCHAIN_API_KEY` for LangSmith tracing
- `KV_REST_API_URL`, `KV_REST_API_TOKEN` for `coaia tash`
Store them in a `.env` file or your shell profile.

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

## Integrations and roadmap
The project will migrate to LangGraph 0.4.x for streaming output and will adopt `coaiapy.fusewill` as the preferred implementation of the `fusewill` CLI. See `ROADMAP.md` for details.
