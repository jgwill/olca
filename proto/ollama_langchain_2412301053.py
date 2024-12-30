import getpass
import os
from langchain_ollama import ChatOllama
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from langgraph.types import interrupt

from langchain_community.agent_toolkits.load_tools import load_tools

import warnings
#

# Suppress the specific UserWarning
warnings.filterwarnings("ignore", category=UserWarning, message="The shell tool has no safeguards by default. Use at your own risk.")

# Set up environment variables for Ollama
def set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")

set_env("LANGCHAIN_API_KEY")  # Optional for tracing

# Initialize the Ollama model
model = ChatOllama(model="llama3.1", temperature=0)

# Define the human-in-the-loop function
def human_review(state):
    result = interrupt({
        "task": "Please review the output and provide any necessary edits.",
        "output": state["output"]
    })
    return result["edited_text"]

# Set up memory for human-in-the-loop
memory = MemorySaver()
selected_tools = ["terminal","human"]
tools = load_tools(selected_tools, allow_dangerous_tools=True)
# Create the chain with human-in-the-loop
graph = create_react_agent(
    model,
    tools=tools
)

# Example input
inputs = {"messages": [("system","You interact well and try to resolve question using your common LLM, just present results to the user."),("user", "Answer the question :What is Langchain? and then present that to the user to accept the answer(make sure to present the results).  Write your status at each steps in the file ./status.txt (make sure you read it and update it at each time keeping an history)")]}

# Run the chain
output_stream = graph.stream(inputs)

# Process the output and allow for human review
for output in output_stream:
    if "output" in output:
        edited_output = human_review(output)
        print("Final Output:", edited_output)
