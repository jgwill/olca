"""Run a simple conversation workflow with persistent session memory."""
from __future__ import annotations

import argparse
from langchain_core.messages import HumanMessage
from olca.persistent_memory import conversation, SessionState


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("message", type=str)
    parser.add_argument("--user", default="demo")
    args = parser.parse_args(argv)

    state = SessionState(messages=[HumanMessage(content=args.message)])
    for update in conversation.stream(
        state,
        config={"configurable": {"user_id": args.user}},
        stream_mode="updates",
    ):
        print(update)


if __name__ == "__main__":
    main()
