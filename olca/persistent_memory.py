"""Persistent session memory utilities using LangGraph.

This module exposes a simple conversation workflow that keeps
user memories across sessions using ``InMemoryStore``.
It mirrors functionality from the legacy branch
``20-add-persistent-session-memory`` while adopting
new LangGraph APIs referenced in the docs.
"""

from __future__ import annotations

import uuid
from typing import TypedDict, List

from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage
from langchain_core.language_models.fake import FakeListLLM
from langgraph.func import entrypoint, task
from langgraph.graph import add_messages
from langgraph.checkpoint.memory import MemorySaver
from langgraph.store.memory import InMemoryStore, BaseStore
import os


class SessionState(TypedDict):
    """Conversation state for persistent sessions."""

    messages: List[BaseMessage]


# Cross-thread store and checkpointer for persistence
store: BaseStore = InMemoryStore()
checkpointer = MemorySaver()


def _get_llm():
    """Return an LLM suitable for tests when OPENAI_API_KEY is absent."""
    if os.getenv("OPENAI_API_KEY"):
        return ChatOpenAI(model="gpt-4o-mini", temperature=0)
    return FakeListLLM(responses=["ok"])


@task
def chat(messages: List[BaseMessage], *, store: BaseStore, user_id: str):
    """Call the LLM with previous memories and store the latest message."""

    namespace = ("memories", user_id)
    history = store.search(namespace, query="")
    remembered = "\n".join(d.value["data"] for d in history)
    system_prefix = f"User info: {remembered}" if remembered else ""

    llm = _get_llm()
    response = llm.invoke(
        [{"role": "system", "content": system_prefix}, *messages]
    )
    # Save the latest user message as a memory
    store.put(namespace, str(uuid.uuid4()), {"data": messages[-1].content})
    return response


@entrypoint(checkpointer=checkpointer, store=store)
def conversation(
    inputs: SessionState,
    *,
    previous: SessionState | None,
    config: dict,
    store: BaseStore,
):
    """Entry graph that maintains session state across threads."""

    user_id = config["configurable"].get("user_id", "default")
    prev_msgs = previous.get("messages") if previous else []
    full_input = {"messages": add_messages(prev_msgs, inputs["messages"])}
    reply = chat(full_input["messages"], store=store, user_id=user_id).result()
    return entrypoint.final(value=reply, save=add_messages(full_input["messages"], reply))


__all__ = ["conversation", "store", "checkpointer", "SessionState"]

