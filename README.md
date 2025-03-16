# oLCa

oLCa is a Python package that provides a CLI tool for Experimenting Langchain with OpenAI wrapper around interacting thru the human-in-the-loop tool.

## Features

## Installation

To install the package, you can use pip:

```bash
pip install olca
```

## Quick Start

1. Install the package:
   ```bash
   pip install olca
   ```
2. Initialize configuration:
   ```bash
   olca init
   ```
3. Run the CLI with tracing:
   ```bash
   olca -T
   ```

## Environment Variables

Set LANGFUSE_PUBLIC_KEY, LANGFUSE_SECRET_KEY, and LANGFUSE_HOST for tracing with Langfuse.  
Set LANGCHAIN_API_KEY for LangSmith tracing.  
Optionally, set OPENAI_API_KEY for OpenAI usage.  

## Usage

### CLI Tool

#### Help

To see the available commands and options, use the `--help` flag:

```bash
olca2 --help
```

## fusewill

The `fusewill` command is a CLI tool that provides functionalities for interacting with Langfuse, including tracing, dataset management, and prompt operations.

### Help

To see the available commands and options for `fusewill`, use the `--help` flag:

----

IMPORTED README from olca1
----

### Olca

The olca.py script is designed to function as a command-line interface (CLI) agent. It performs various tasks based on given inputs and files present in the directory. The agent is capable of creating directories, producing reports, and writing instructions for self-learning. It operates within a GitHub repository environment and can commit and push changes if provided with an issue ID. The script ensures that it logs its internal actions and follows specific guidelines for handling tasks and reporting, without modifying certain configuration files or checking out branches unless explicitly instructed.

#### Tracing

Olca now supports tracing functionality to help monitor and debug its operations. You can enable tracing by using the `-T` or `--tracing` flag when running the script. Ensure that the `LANGCHAIN_API_KEY` environment variable is set for tracing to work.

#### Initialization

To initialize `olca`, you need to create a configuration file named `olca.yml`. This file contains various settings that `olca` will use to perform its tasks. Below is an example of the `olca.yml` file:

```yaml
api_keyname: OPENAI_API_KEY__o450olca241128
human: true
model_name: gpt-4o-mini #or bellow:
model_name: ollama://llama3.1:latest #or with host
model_name: ollama://llama3.1:latest@mymachine.mydomain.com:11434
recursion_limit: 300
system_instructions: You focus on interacting with human and do what they ask.  Make sure you dont quit the program.
temperature: 0.0
tracing: true
tracing_providers:
- langsmith
- langfuse
user_input: Look in the file 3act.md and in ./story, we have created a story point by point and we need you to generate the next iteration of the book in the folder ./book.  You use what you find in ./story to start the work.  Give me your plan to correct or accept.
```

#### Usage

To run `olca`, use the following command:

```shell
olca -T
```

This command will enable tracing and start the agent. You can also use the `--trace` flag to achieve the same result.

#### Configuration

The `olca.yml` file allows you to configure various aspects of `olca`, such as the API key (so you can know how much your experimetation cost you), model name, recursion limit, system instructions, temperature, and user input. You can customize these settings to suit your needs and preferences.

#### Command-Line Interface (CLI)

The `olca` script provides a user-friendly CLI that allows you to interact with the agent and perform various tasks. You can use flags and options to control the agent's behavior and provide input for its operations. The CLI also includes error handling mechanisms to notify you of any issues or missing configuration settings.

#### GitHub Integration

`olca` is designed to integrate seamlessly with GitHub workflows and issue management. You can provide an issue ID to the agent, and it will commit and push changes directly to the specified issue. This feature streamlines the development process and reduces the need for manual intervention. Additionally, `olca` maintains detailed logs of its actions and updates, ensuring transparency and traceability in its operations.

### Persistent Session Memory

The Persistent Session Memory feature allows OLCA to retain execution context across sessions and directory changes, ensuring seamless workflow continuation.

**Key Features:**
* Automatically saves session states to `~/.olca_sessions/`.
* Resumes the last execution state if OLCA is restarted in the same directory.
* Creates a new session if no prior session exists.

**Example Use Case:**
```sh
> cd ~/projects/story-triac  
> olca --session triac_outline  
> olca generate_structure  
```
* Session automatically saves to `~/.olca_sessions/triac_outline.json`
* Restarting OLCA in the same directory resumes from the last state

### Parent Directory Inheritance

The Parent Directory Inheritance feature allows OLCA to check parent directories for an active session if no session is found in the current directory.

**Key Features:**
* Configurable behavior controlled by `inherit_parent_session=true`.
* Recursively checks parent directories until it finds an active session.
* Starts a fresh session if no session is found and inheritance is disabled.

**Example Use Case:**
```sh
> cd ~/projects/story-triac/drafts  
> olca  
```
* If parent inheritance is enabled, OLCA loads `triac_outline` from `projects/story-triac/`.
* If disabled, OLCA starts a fresh session.

### Ephemeral Sessions (`--temp-session`)

The Ephemeral Sessions feature allows users to run OLCA in temporary mode, where execution state is stored only in memory and disappears after the process ends.

**Key Features:**
* Does not save state to disk.
* Session tracking occurs only while OLCA is running.

**Example Use Case:**
```sh
> olca --temp-session  
```
* Session exists in RAM only, disappears after process ends.

### Session Save Interval

The session save interval is configurable in `olca.yml` via the `session_save_interval` option.

### Custom Session Directory

The session directory is configurable in `olca.yml` via the `session_directory` option.

### Redis Upstash Integration

OLCA can store session data in Redis Upstash and access it via a REST API.

### List Active Sessions

Added a command to list all active sessions in `olca/olcacli.py`.

### Export Sessions

Added a command to export sessions in `olca/olcacli.py`.

### Shared Scratchpad

Added a command to share a scratchpad between OLCA and another agent using Redis memory.

### Nested Sessions

A session can be the child of a session managed in a Redis memory key.

### QStash Integration

OLCA can use QStash to trigger the start of a session, with a new command in `olca/olcacli.py` to listen for QStash messages and start sessions.

### `olca.yml` Configuration

`olca.yml` now includes all features, avoiding the need for CLI arguments.

### Session Management Commands

Added `list_sessions` and `get_session` commands in `olca/olcacli.py` to manage and retrieve session data.

### Contextual Continuity

Implemented `prepare_input` function in `olca/olcahelper.py` to prepare inputs considering past sessions' context.

### Significant Events

Updated `SYSTEM_PROMPT_APPEND` in `olca/prompts.py` to include instructions for marking significant events and their importance.

### Contextual Reintegration

`initialize_config_file` function in `olca/olcahelper.py` now sets up a configuration that supports contextual reintegration.

### Recursive Continuity

Added `SessionState`, `RedStone`, `EchoNode`, `MetaFramework`, and `FractalLibrary` classes to manage recursive continuity and dynamic adaptation.

## Persistent Sessions and QStash
- You can now save and load sessions using the new commands.
- Redis-based storage enables persistent state across runs.
- QStash message handling automates asynchronous triggers.
