# Typed State Example

This prototype illustrates how future versions of `olca` will use LangGraph `StateGraph`.

```python
from olca.state_helpers import ConversationState, create_state_graph

sg = create_state_graph()
# Add nodes and edges here when implementing typed states
```

The example currently does nothing, but serves as a starting point for the migration to LangGraph 0.4.
\nSee `typed_state.ipynb` for a Jupyter demonstration.
