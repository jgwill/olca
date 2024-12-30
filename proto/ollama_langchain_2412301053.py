import getpass
import os
from langchain_ollama import ChatOllama
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from langgraph.types import interrupt

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
selected_tools = ["terminal"]
# Create the chain with human-in-the-loop
graph = create_react_agent(
    model,
    tools=selected_tools,  # Add any terminal tools if needed
    interrupt_before=["tools"],
    checkpointer=memory
)

# Example input
inputs = {"messages": [("user", "What is the weather today?")]}

# Run the chain
output_stream = graph.stream(inputs)

# Process the output and allow for human review
for output in output_stream:
    if "output" in output:
        edited_output = human_review(output)
        print("Final Output:", edited_output)
