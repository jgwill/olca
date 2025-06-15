from typing import Annotated, TypedDict

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langfuse.langchain import CallbackHandler
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages


class State(TypedDict):
    """Conversation state for LangGraph."""

    messages: Annotated[list, add_messages]


def build_graph() -> StateGraph[State]:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

    def chatbot(state: State) -> dict:
        return {"messages": [llm.invoke(state["messages"])]}

    sg = StateGraph(State)
    sg.add_node("chat", chatbot)
    sg.set_entry_point("chat")
    sg.set_finish_point("chat")
    return sg.compile()


def main():
    graph = build_graph()
    cb = CallbackHandler()
    for update in graph.stream({"messages": [HumanMessage(content="Hello there!")]}, config={"callbacks": [cb]}):
        print(update)


if __name__ == "__main__":
    main()
