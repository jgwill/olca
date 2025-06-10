"""Typed state utilities for upcoming LangGraph migration."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List

from langgraph.graph import StateGraph
from langgraph.graph.state import State


@dataclass
class ConversationState(State):
    """Example typed state for streaming conversations."""

    messages: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)


def create_state_graph() -> StateGraph[ConversationState]:
    """Return a minimal StateGraph configured for conversation states."""
    sg: StateGraph[ConversationState] = StateGraph()
    # Implementation will be expanded during the LangGraph 0.4 migration.
    return sg
