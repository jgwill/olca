import os
import sys
try:
    import dotenv
except ImportError:
    dotenv = None
import webbrowser

def load_environment():
    if dotenv:
        dotenv.load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))
    
    # Try loading from home directory if variables are still not set
    if not all([
        os.getenv(key)
        for key in [
            "LANGFUSE_PUBLIC_KEY",
            "LANGFUSE_SECRET_KEY",
            "LANGFUSE_HOST",
            "LANGCHAIN_API_KEY",
            "OPENAI_API_KEY",
        ]
    ]):
        if dotenv:
            dotenv.load_dotenv(dotenv_path=os.path.expanduser("~/.env"))

def initialize_langfuse(debug=False):
    try:
        from langfuse import Langfuse
    except ImportError:
        return None
    required_vars = ["LANGFUSE_PUBLIC_KEY", "LANGFUSE_SECRET_KEY", "LANGFUSE_HOST"]
    if not all(os.getenv(var) for var in required_vars):
        return None
    
    return Langfuse(
        public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
        secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
        host=os.getenv("LANGFUSE_HOST"),
        debug=debug
    )
