import os
import sys
import dotenv
import webbrowser
import redis
import json
import requests

def load_environment():
    dotenv.load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))
    
    # Try loading from home directory if variables are still not set
    if not all([os.getenv(key) for key in ["LANGFUSE_PUBLIC_KEY", "LANGFUSE_SECRET_KEY", "LANGFUSE_HOST", 
                                          "LANGCHAIN_API_KEY", "OPENAI_API_KEY"]]):
        dotenv.load_dotenv(dotenv_path=os.path.expanduser("~/.env"))

def initialize_langfuse( debug=False):
    from langfuse import Langfuse
    required_vars = ["LANGFUSE_PUBLIC_KEY", "LANGFUSE_SECRET_KEY", "LANGFUSE_HOST"]
    if not all(os.getenv(var) for var in required_vars):
        return None
    
    return Langfuse(
        public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
        secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
        host=os.getenv("LANGFUSE_HOST"),
        debug=debug
    )

def store_session_in_redis(session_id, state, redis_url):
    redis_client = redis.Redis.from_url(redis_url)
    redis_client.set(session_id, json.dumps(state))

def load_session_from_redis(session_id, redis_url):
    redis_client = redis.Redis.from_url(redis_url)
    state = redis_client.get(session_id)
    if state:
        return json.loads(state)
    return None

def share_scratchpad_between_agents(scratchpad_key, content, redis_url):
    redis_client = redis.Redis.from_url(redis_url)
    redis_client.set(scratchpad_key, json.dumps(content))

def get_shared_scratchpad(scratchpad_key, redis_url):
    redis_client = redis.Redis.from_url(redis_url)
    content = redis_client.get(scratchpad_key)
    if content:
        return json.loads(content)
    return None

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
