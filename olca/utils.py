import os
import sys
import dotenv
import webbrowser
from langfuse import Langfuse

def load_environment():
    dotenv.load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))
    
    # Try loading from home directory if variables are still not set
    if not all([os.getenv(key) for key in ["LANGFUSE_PUBLIC_KEY", "LANGFUSE_SECRET_KEY", "LANGFUSE_HOST", 
                                          "LANGCHAIN_API_KEY", "OPENAI_API_KEY"]]):
        dotenv.load_dotenv(dotenv_path=os.path.expanduser("~/.env"))

def initialize_langfuse( debug=False):
    required_vars = ["LANGFUSE_PUBLIC_KEY", "LANGFUSE_SECRET_KEY", "LANGFUSE_HOST"]
    if not all(os.getenv(var) for var in required_vars):
        return None
    
    return Langfuse(
        public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
        secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
        host=os.getenv("LANGFUSE_HOST"),
        debug=debug
    )
