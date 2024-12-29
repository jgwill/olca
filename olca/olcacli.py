#%%
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import dotenv
from langchain import hub
import argparse
import yaml
from olca.utils import load_environment, initialize_langfuse
from olca.tracing import TracingManager
from olca.olcahelper import setup_required_directories, initialize_config_file
from prompts import SYSTEM_PROMPT_APPEND, HUMAN_APPEND_PROMPT

#jgwill/olca1
#olca1_prompt = hub.pull("jgwill/olca1") #Future use
#https://smith.langchain.com/hub/jgwill/olca1

def get_input() -> str:
    print("----------------------")
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line == "q":
            break
        contents.append(line)
    return "\n".join(contents)


#try loaging .env and see if a key is there for OLCA_SYSTEM_PROMPT_APPEND
#If it is there, use it instead of the default
try:
    OLCA_SYSTEM_PROMPT_APPEND = os.getenv("OLCA_SYSTEM_PROMPT_APPEND")
    if OLCA_SYSTEM_PROMPT_APPEND is not None:
        SYSTEM_PROMPT_APPEND = OLCA_SYSTEM_PROMPT_APPEND
except:
    pass

def load_config(config_file):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config


#%%

dotenv.load_dotenv()

#%%
#from dotenv in ./.env , load key

#%%

# First we initialize the model we want to use.
from json import load
from langchain_openai import ChatOpenAI,OpenAI
from langchain.agents import AgentExecutor, create_react_agent

from langchain_community.agent_toolkits.load_tools import load_tools

import warnings
#

# Suppress the specific UserWarning
warnings.filterwarnings("ignore", category=UserWarning, message="The shell tool has no safeguards by default. Use at your own risk.")

from langchain_community.tools.shell import ShellTool

from typing import Literal

from langchain_core.tools import tool

from langgraph.prebuilt import create_react_agent
from langgraph.errors import GraphRecursionError

@tool
def get_weather(city: Literal["nyc", "sf"]):
    """Use this to get weather information."""
    if city == "nyc":
        return "It might be cloudy in nyc"
    elif city == "sf":
        return "It's always sunny in sf"
    else:
        raise AssertionError("Unknown city")

def ensure_directories_exist(extra_directories:str=None):
    directories = ['./reports', './log', './.olca']
    if extra_directories:
        directories += extra_directories
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            
def extract_extra_directories_from_olca_config_system_and_user_input(system_instructions, user_input):
    extra_directories = []
    #parse thru the 2 inputs and search for patterns such as ./story/ (or any other directory)
    for input in [system_instructions, user_input]:
        if input:
            for word in input.split():
                if word.startswith("./") and word.endswith("/"):
                    extra_directories.append(word)
    return extra_directories


def print_stream(stream):
    for s in stream:
        try:
            # Skip Langfuse internal state messages and size limit warnings
            if isinstance(s, dict) and ('keep_alive' in s or 'states' in s):
                continue
            if isinstance(s, str) and ('Item exceeds size limit' in s or 'pending_switch_proposals' in s):
                continue
                
            # Handle different response formats
            if isinstance(s, dict) and "messages" in s:
                message = s["messages"][-1]
            else:
                message = s
                
            if isinstance(message, tuple):
                print(message)
            elif hasattr(message, 'content'):
                print(message.content)
            else:
                print(s)
        except Exception as e:
            print(s)

def prepare_input(user_input, system_instructions,append_prompt=True, human=False):
    appended_prompt = system_instructions + SYSTEM_PROMPT_APPEND if append_prompt else system_instructions
    appended_prompt = appended_prompt + HUMAN_APPEND_PROMPT if human else appended_prompt
    
    inputs = {"messages": [
    ("system",
     appended_prompt),
    ("user", user_input     )
    ]}
        
    return inputs,system_instructions,user_input

OLCA_DESCRIPTION = "OlCA (Orpheus Langchain CLI Assistant) (very Experimental and dangerous)"
OLCA_EPILOG = "For more information: https://github.com/jgwill/orpheuspypractice/wiki/olca"
OLCA_USAGE="olca [-D] [-H] [-M] [-T] [init] [-y]"
def _parse_args():
    parser = argparse.ArgumentParser(description=OLCA_DESCRIPTION, epilog=OLCA_EPILOG,usage=OLCA_USAGE)
    parser.add_argument("-D", "--disable-system-append", action="store_true", help="Disable prompt appended to system instructions")
    parser.add_argument("-H", "--human", action="store_true", help="Human in the loop mode")
    parser.add_argument("-M", "--math", action="store_true", help="Enable math tool")
    parser.add_argument("-T", "--tracing", action="store_true", help="Enable tracing")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("init", nargs='?', help="Initialize olca interactive mode")
    parser.add_argument("-y", "--yes", action="store_true", help="Accept the new file olca.yml")
    return parser.parse_args()

def parse_model_uri(uri: str):
    # Example: "ollama://llama2@localhost"
    if "://" not in uri:
        return "openai", uri, None  # default provider is openai
    provider, rest = uri.split("://", 1)
    host = None
    if "@" in rest:
        base_model, host = rest.split("@", 1)
    else:
        base_model = rest
    return provider, base_model, host

def main():
    args = _parse_args()
    olca_config_file = 'olca.yml'
    
    # Load environment variables first
    load_environment()
    
    # Initialize Langfuse if needed
    langfuse = initialize_langfuse(debug=True if args.debug else False)
    
    if args.init:
        if os.path.exists(olca_config_file):
            print("Error: Configuration file already exists. Cannot run 'olca init'.")
            return
        if args.yes:
            pass
        else:
            initialize_config_file()
            return
    
    if not os.path.exists(olca_config_file):
        initialize_config_file()
        return

    config = load_config(olca_config_file)
    
    # Initialize tracing
    tracing_manager = TracingManager(config)
    callbacks = tracing_manager.get_callbacks()
    
    # Remove old tracing setup
    tracing_enabled = config.get('tracing', False) or args.tracing
    if tracing_enabled and not callbacks:
        print("Warning: Tracing enabled but no handlers configured")

    if tracing_enabled:
        # Verify Langfuse configuration
        if not all([os.getenv(key) for key in ["LANGFUSE_PUBLIC_KEY", "LANGFUSE_SECRET_KEY", "LANGFUSE_HOST"]]):
            print("Warning: Langfuse environment variables missing")
        # Verify LangSmith configuration
        if not os.getenv("LANGCHAIN_API_KEY"):
            print("Warning: LANGCHAIN_API_KEY not set")

    try:
        api_key_variable = "OPENAI_API_KEY"
        api_keyname = config.get('api_keyname', "OPENAI_API_KEY_olca")
        api_key = os.getenv(api_keyname)
        if api_key:
            os.environ[api_key_variable] = api_key
    except:
        #load .env file in current dir or HOME and find OPENAI_API_KEY
        try:
            dotenv.load_dotenv()
        except:
            #load in HOME
            try:
                dotenv.load_dotenv(dotenv.find_dotenv(usecwd=False))
            except:
                print("Error: Could not load .env file")
                exit(1)

    system_instructions = config.get('system_instructions', '')
    user_input = config.get('user_input', '')
    default_model_id = "gpt-4o-mini"
    recursion_limit = config.get('recursion_limit', 15)
    disable_system_append = _parse_args().disable_system_append
    # Use the system_instructions and user_input in your CLI logic
    model_name = config.get('model_name', default_model_id)
    provider, base_model, host = parse_model_uri(model_name)
    
    if provider == "ollama":
        from langchain_ollama import OllamaLLM
        model = OllamaLLM(model=base_model, base_url=host if host else None)
    elif provider == "openai":
        from langchain_openai import ChatOpenAI
        model = ChatOpenAI(model=base_model, temperature=0)
    else:
        # default fallback
        from langchain_openai import ChatOpenAI
        model = ChatOpenAI(model=model_name, temperature=0)

    print("System Instructions:", system_instructions)
    print("User Input:", user_input)
    print("Recursion Limit:", recursion_limit)
    print("Trace:", tracing_enabled)
    print("Model Name:", model_name)
    
    selected_tools = ["terminal"]
    
    disable_system_append = _parse_args().disable_system_append
    
    human_switch = args.human
    #look in olca_config.yaml for human: true
    if "human" in config:
        human_switch = config["human"]
        
    if human_switch:
        selected_tools.append("human")
    
    if args.math:
        from langchain_openai import OpenAI
        math_llm = OpenAI()
        selected_tools.append("llm-math")
        if human_switch:
            tools = load_tools(selected_tools, llm=math_llm, allow_dangerous_tools=True, input_func=get_input)
        else:
            tools = load_tools(selected_tools, llm=math_llm, allow_dangerous_tools=True)
    else:
        if human_switch:
            tools = load_tools(selected_tools, allow_dangerous_tools=True, input_func=get_input)
        else:
            tools = load_tools(selected_tools, allow_dangerous_tools=True)
    
    if human_switch:
        user_input = user_input + " Dont forget to USE THE HUMAN-IN-THE-LOOP TOOL"
        system_instructions = system_instructions + ". Use the human-in-the-loop tool"
    
    # Define the graph
    graph = create_react_agent(model, tools=tools)
    
    if graph.config is None:
        graph.config = {}
    graph.config["recursion_limit"] = recursion_limit
    
    inputs, system_instructions, user_input = prepare_input(user_input, system_instructions, not disable_system_append, human_switch)
    
    setup_required_directories(system_instructions, user_input)
    
    try:
        graph_config = {"callbacks": callbacks} if callbacks else {}
        if recursion_limit:
            graph_config["recursion_limit"] = recursion_limit
        print_stream(graph.stream(inputs, config=graph_config))
    except GraphRecursionError as e:
        print("Recursion limit reached. Please increase the 'recursion_limit' in the olca_config.yaml file.")
        print("For troubleshooting, visit: https://python.langchain.com/docs/troubleshooting/errors/GRAPH_RECURSION_LIMIT")
    except KeyboardInterrupt:
        print("\nExiting gracefully.")
        tracing_manager.flush()
        tracing_manager.shutdown()
        exit(0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting gracefully.")
        exit(0)
