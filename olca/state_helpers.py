"""Typed state utilities for upcoming LangGraph migration."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List

from langgraph.graph import StateGraph, END


@dataclass
class ConversationState:
    """Example typed state for streaming conversations."""

    messages: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)


def create_state_graph() -> StateGraph[ConversationState]:
    """Return a minimal StateGraph configured for conversation states."""
    sg: StateGraph[ConversationState] = StateGraph(ConversationState)
    sg.add_node("echo", lambda state: state)
    sg.set_entry_point("echo")
    sg.add_edge("echo", END)
    return sg
