import os
from langfuse.callback import CallbackHandler as LangfuseCallbackHandler
import langsmith

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
            handler = self._setup_langsmith()
            if handler:
                self.handlers.append(handler)

        if 'langfuse' in providers:
            handler = self._setup_langfuse()
            if handler:
                self.handlers.append(handler)

    def _setup_langsmith(self):
        os.environ["LANGCHAIN_TRACING_V2"] = "true"
        api_key = os.getenv("LANGCHAIN_API_KEY") or os.getenv("LANGSMITH_API_KEY")
        
        if not api_key:
            print("Warning: LANGCHAIN_API_KEY/LANGSMITH_API_KEY not set for LangSmith tracing")
            return None
            
        return langsmith.Client(api_key=api_key)

    def _setup_langfuse(self):
        if not (os.getenv("LANGFUSE_PUBLIC_KEY") and os.getenv("LANGFUSE_SECRET_KEY")):
            print("Warning: LANGFUSE_PUBLIC_KEY/LANGFUSE_SECRET_KEY not set for Langfuse tracing")
            return None
            
        return LangfuseCallbackHandler()

    def get_callbacks(self):
        return self.handlers if self.handlers else None
