from typing import Annotated
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import argparse
import fusewill_utils as fu

langfuse=fu.langfuse

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from typing_extensions import TypedDict
 
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
 
class State(TypedDict):
    # Messages have the type "list". The `add_messages` function in the annotation defines how this state key should be updated
    # (in this case, it appends messages to the list, rather than overwriting them)
    messages: Annotated[list, add_messages]
 
graph_builder = StateGraph(State)
 
llm = ChatOpenAI(model = "gpt-4o-mini", temperature = 0.2)
 
# The chatbot node function takes the current State as input and returns an updated messages list. This is the basic pattern for all LangGraph node functions.
def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}
 
# Add a "chatbot" node. Nodes represent units of work. They are typically regular python functions.
graph_builder.add_node("fusewillchatbot", chatbot)
 
# Add an entry point. This tells our graph where to start its work each time we run it.
graph_builder.set_entry_point("fusewillchatbot")
 
# Set a finish point. This instructs the graph "any time this node is run, you can exit."
graph_builder.set_finish_point("fusewillchatbot")
 
# To be able to run our graph, call "compile()" on the graph builder. This creates a "CompiledGraph" we can use invoke on our state.
graph = graph_builder.compile()

from IPython.display import Image, display
display(Image(graph.get_graph().draw_mermaid_png()))

from langfuse.callback import CallbackHandler
 
# Initialize Langfuse CallbackHandler for Langchain (tracing)
langfuse_handler = CallbackHandler()
 
for s in graph.stream({"messages": [HumanMessage(content = "What is Langfuse in 2 sentences?")]},
                      config={"callbacks": [langfuse_handler]}):
    print(s)