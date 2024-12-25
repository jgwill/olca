import os
from langfuse.callback import CallbackHandler as LangfuseCallbackHandler

class TracingManager:
    def __init__(self, config):
        self.config = config
        self.handlers = []
        self.initialize_tracing()

    def initialize_tracing(self):
        tracing_enabled = self.config.get('tracing', False)
        providers = self.config.get('tracing_providers', ['langsmith'])

        if not tracing_enabled:
            return

        if 'langsmith' in providers:
            self._setup_langsmith()

        if 'langfuse' in providers:
            handler = self._setup_langfuse()
            if handler:
                self.handlers.append(handler)

    def _setup_langsmith(self):
        api_key = os.getenv("LANGCHAIN_API_KEY") or os.getenv("LANGSMITH_API_KEY")
        if api_key:
            os.environ["LANGCHAIN_TRACING_V2"] = "true"

    def _setup_langfuse(self):
        if not (os.getenv("LANGFUSE_PUBLIC_KEY") and os.getenv("LANGFUSE_SECRET_KEY")):
            print("Warning: LANGFUSE_PUBLIC_KEY/LANGFUSE_SECRET_KEY not set for Langfuse tracing")
            return None
            
        return LangfuseCallbackHandler()

    def get_callbacks(self):
        return self.handlers if self.handlers else None
