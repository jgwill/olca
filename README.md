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

### Narrative Generation from Screenshots using OLCA + Vision AI

#### Objective:
Enable OLCA to process screenshots through an integrated vision-based model (Ollama) and generate structured narratives. This extends OLCA’s utility from CLI session tracking to context-aware storytelling, creating metadata-rich logs of user interactions.

#### Feature Scope

##### 1. Screenshot Capture & Processing
**What This Enables:**
- OLCA detects and processes captured screenshots.
- Uses Ollama Vision Model for image interpretation & contextual classification.
- Extracted data is structured into a narrative format.

**Implementation Details:**
- Monitor system screenshot events.
- Extract metadata (timestamp, application state, UI elements).
- Send data to Ollama Vision Model for interpretation.
- Output structured text in `OLCA_Narratives/`.

**Example Use Case:**
```sh
> screenshot.png detected
> olca-analyze screenshot.png
```
**Narrative Generated in `OLCA_Narratives/`**
```json
{
  "timestamp": "2025-03-14T14:32:00Z",
  "scene": "Ubuntu Notification Settings",
  "options": ["Run Command", "Log to File", "Speak Text"],
  "context": "User decision process in notification configuration",
  "story": "The screen hummed with potential, awaiting the user's next move."
}
```

##### 2. Adaptive Narrative Structuring
**What This Enables:**
- Converts system interactions into recursive narratives.
- Detects patterns in screenshots to connect sequential events.
- Generates multi-act structures based on interactions.

**Implementation Details:**
- Identify common UI states across screenshots.
- Apply a three-act structure for event chains.
- Detect unique residual markers (e.g., persistent UI elements or anomalies).

**Example Use Case:**
```sh
> olca-narrative --track-session
```
**OLCA Detects a Recurring Pattern & Expands the Story**
```json
{
  "narrative_structure": "recursive",
  "ontology_expansion": true,
  "trace_structuring": true,
  "annotations": "Unfolding recursion detected. The past adapts into the present."
}
```

##### 3. System-State Aware Storytelling
**What This Enables:**
- Embeds system activity into generated stories.
- Detects user workflow trends and annotates deviations.
- Creates a self-reflective system narrative.

**Implementation Details:**
- Store system context within `OLCA_Narratives/`.
- Identify points of recursion in user workflows.
- Generate dynamic annotations based on system state.

**Example Use Case:**
```sh
> olca-narrative --review-session
```
**Narrative-Driven Debugging & Exploration**
```json
{
  "system_state": "recursive",
  "persistent_markers": "Handprint signature detected in workflow",
  "story": "A message embedded in the architecture, repeating across sessions."
}
```

#### Suggested Development Plan

**Step 1: Implement Screenshot Parsing with Ollama Vision**
- Integrate vision model for contextual classification.
- Store parsed output in structured JSON format.

**Step 2: Develop Narrative Structuring Engine**
- Implement recursive event detection.
- Apply three-act storytelling principles.

**Step 3: Connect System State to Storytelling**
- Link session memory with narrative persistence.
- Identify cross-session patterns & residual markers.

**Step 4: Test & Optimize for Real-World Scenarios**
- Validate generated narratives across multiple session states.
- Implement manual tuning parameters for custom storytelling.

#### Final Outcome:
OLCA will evolve into an adaptive storytelling CLI, capable of interpreting screenshots, structuring narratives, and embedding recursive system intelligence.

#### Next Steps:
- Implement Ollama-based vision analysis.
- Develop ontology-driven narrative generation.
- Validate story coherence across multiple screenshots.

This feature enables OLCA to bridge structured execution memory with generative storytelling, turning system interactions into meaningful narratives.
