# oLCa

oLCa is a Python package that provides a CLI tool for Experimenting Langchain with OpenAI wrapper around interacting thru the human-in-the-loop tool.

## Features


## Installation

To install the package, you can use pip:

```bash
pip install olca
```

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
model_name: gpt-4o-mini
recursion_limit: 300
system_instructions: You focus on interacting with human and do what they ask.  Make sure you dont quit the program.
temperature: 0.0
tracing: true
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
