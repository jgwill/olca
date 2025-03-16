import os
from olca.utils import initialize_langfuse
import warnings
import requests
import redis
import json

# Ignore specific Langfuse warning
warnings.filterwarnings("ignore", message="Item exceeds size limit", category=UserWarning)

class TracingManager:
    def __init__(self, config):
        self.config = config
        self.handlers = []
        self.langfuse = None
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
        from langfuse.callback import CallbackHandler as LangfuseCallbackHandler
        from langfuse import Langfuse
        self.langfuse = initialize_langfuse()
        if not self.langfuse:
            print("Warning: Missing Langfuse environment variables")
            return None
            
        return LangfuseCallbackHandler()

    def get_callbacks(self):
        return self.handlers if self.handlers else None

    def flush(self):
        if self.langfuse:
            self.langfuse.flush()

    def shutdown(self):
        if self.langfuse:
            self.langfuse.shutdown()

def handle_qstash_messages(qstash_topic, qstash_token):
    headers = {
        "Authorization": f"Bearer {qstash_token}"
    }
    response = requests.get(f"https://qstash.upstash.io/v1/topics/{qstash_topic}/messages", headers=headers)
    if response.status_code == 200:
        messages = response.json()
        for message in messages:
            session_id = message.get("session_id")
            if session_id:
                state = load_session_from_redis(session_id, "redis://localhost:6379")
                if state:
                    print(f"Starting session {session_id} with state: {state}")
                    # Start the session with the loaded state
    else:
        print(f"Failed to fetch messages from QStash: {response.status_code}")

def load_session_from_redis(session_id, redis_url):
    redis_client = redis.Redis.from_url(redis_url)
    state = redis_client.get(session_id)
    if state:
        return json.loads(state)
    return None
