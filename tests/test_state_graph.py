from olca.state_helpers import create_state_graph, ConversationState


def test_state_graph_stream():
    sg = create_state_graph()
    graph = sg.compile()
    state = ConversationState(messages=["hi"])
    outputs = list(graph.stream(state))
    assert outputs
    last = outputs[-1]
    assert isinstance(last, dict)
    assert "echo" in last
    assert last["echo"]["messages"] == ["hi"]
