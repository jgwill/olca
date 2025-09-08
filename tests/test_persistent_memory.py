import os
from olca.persistent_memory import conversation, SessionState
from langchain_core.messages import HumanMessage


def test_conversation_stream():
    os.environ.pop("OPENAI_API_KEY", None)
    state = SessionState(messages=[HumanMessage(content="hi")])
    outputs = list(
        conversation.stream(
            state,
            config={"configurable": {"user_id": "test", "thread_id": "t1"}},
            stream_mode="updates",
        )
    )
    assert outputs
    assert any(isinstance(o, dict) for o in outputs)
