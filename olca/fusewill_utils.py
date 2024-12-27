import os
import sys
import json
import dotenv
import webbrowser
import requests  # Add this import

# Load .env from the current working directory
dotenv.load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))

# Try loading from home directory if variables are still not set
if not os.environ.get("LANGFUSE_PUBLIC_KEY") or not os.environ.get("LANGFUSE_SECRET_KEY") or not os.environ.get("LANGFUSE_HOST"):
    dotenv.load_dotenv(dotenv_path=os.path.expanduser("~/.env"))

# Final check before exiting
missing_vars = []
if not os.environ.get("LANGFUSE_PUBLIC_KEY"):
    missing_vars.append("LANGFUSE_PUBLIC_KEY")
if not os.environ.get("LANGFUSE_SECRET_KEY"):
    missing_vars.append("LANGFUSE_SECRET_KEY")
if not os.environ.get("LANGFUSE_HOST"):
    missing_vars.append("LANGFUSE_HOST")

if missing_vars:
    print(f"Error: {', '.join(missing_vars)} not found.")
    sys.exit(1)

from langfuse import Langfuse
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import json

import dotenv
_DEBUG_=False
if _DEBUG_:
    print(os.environ.get("LANGFUSE_PUBLIC_KEY"))
    print(os.environ.get("LANGFUSE_SECRET_KEY"))
    print(os.environ.get("LANGFUSE_HOST"))

langfuse = Langfuse(
    public_key=os.environ.get("LANGFUSE_PUBLIC_KEY"),
    secret_key=os.environ.get("LANGFUSE_SECRET_KEY"),
    host=os.environ.get("LANGFUSE_HOST")
)
def dummy():
    o=langfuse.get_observations()
    g=langfuse.get_generations()
    prompts_list=langfuse.get_dataset()
    
def open_trace_in_browser(trace_id):
    base_url = os.environ.get("LANGFUSE_HOST")
    project_id = os.environ.get("LANGFUSE_PROJECT_ID")
    if not base_url or not project_id:
        print("Missing LANGFUSE_HOST or LANGFUSE_PROJECT_ID")
        return
    full_url = f"{base_url}/project/{project_id}/traces/{trace_id}"
    print(f"Opening {full_url}")
    webbrowser.open(full_url)

def get_score_by_id(score_id):
    """Retrieve score details by score ID."""
    base_url = os.environ.get("LANGFUSE_HOST")
    public_key = os.environ.get("LANGFUSE_PUBLIC_KEY")
    secret_key = os.environ.get("LANGFUSE_SECRET_KEY")
    url = f"{base_url}/api/public/scores/{score_id}"
    try:
        response = requests.get(url, auth=(public_key, secret_key))
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error retrieving score {score_id}: {e}")
        return None

def list_scores():
    """Retrieve all score configurations."""
    base_url = os.environ.get("LANGFUSE_HOST")
    public_key = os.environ.get("LANGFUSE_PUBLIC_KEY")
    secret_key = os.environ.get("LANGFUSE_SECRET_KEY")
    url = f"{base_url}/api/public/score-configs"
    try:
        response = requests.get(url, auth=(public_key, secret_key))
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error retrieving scores: {e}")
        return None

def print_trace(trace, show_comments=False):
    print(f"<Trace \n\tat=\"{trace.createdAt}\" \n\tid=\"{trace.id}\" \n\tname=\"{trace.name}\" \n\tsession_id=\"{trace.session_id}\" \n\tprojectId=\"{trace.projectId}\" >")
    print(f"<Input><CDATA[[\n{trace.input}\n]]></Input>")
    print(f"<Output><CDATA[[\n{trace.output}\n]]></Output>")
    if trace.metadata:
        print(f"<Metadata>{trace.metadata}</Metadata>")
    if trace.scores:
        print("<Scores>")
        for score_id in trace.scores:
            score = get_score_by_id(score_id)
            if score:
                print(f"<Score name=\"{score['name']}\" value=\"{score['value']}\" data_type=\"{score['dataType']}\" />")
        print("</Scores>")
    if show_comments and hasattr(trace, "comments"):
        print(f"<Comments>\n{trace.comments}\n</Comments>")
    print("</Trace>")

def print_traces(traces, show_comments=False):
    for trace in traces.data:
        print_trace(trace, show_comments)

def list_traces(limit=100, output_dir="../output/traces", show_comments=False):
    traces = langfuse.get_traces(limit=limit)
    os.makedirs(output_dir, exist_ok=True)
    return traces

def list_traces_by_score(score_name, min_value=None, max_value=None, limit=100):
    traces = langfuse.get_traces(limit=limit)
    filtered_traces = []
    for trace in traces.data:
        for score_id in trace.scores:
            score = get_score_by_id(score_id)
            if score and score.get('name') == score_name:
                if (min_value is None or score.get('value') >= min_value) and (max_value is None or score.get('value') <= max_value):
                    filtered_traces.append(trace)
                    break
    return filtered_traces

def add_score_to_a_trace(trace_id, generation_id, name, value, data_type="NUMERIC", comment=""):
    langfuse.score(
        trace_id=trace_id,
        observation_id=generation_id,
        name=name,
        value=value,
        data_type=data_type,
        comment=comment
    )

def create_score(name, data_type, description="", possible_values=None, min_value=None, max_value=None):
    langfuse.score(
        name=name,
        value="",  # Provide a placeholder value
        data_type=data_type,
        description=description,
        # For categorical:
        **({"possible_values": possible_values} if data_type == "CATEGORICAL" and possible_values else {}),
        # For numeric:
        **({"min_value": min_value, "max_value": max_value} if data_type == "NUMERIC" and min_value is not None and max_value is not None else {})
    )

def score_exists(name):
    scores = langfuse.get_scores()
    for score in scores.data:
        if score.name == name:
            return True
    return False

def create_dataset(name, description="", metadata=None):
    langfuse.create_dataset(
        name=name,
        description=description,
        metadata=metadata or {}
    )
def get_dataset(name) :
    return langfuse.get_dataset(name=name)
  
def create_prompt(name, prompt_text, model_name, temperature, labels=None, supported_languages=None):
    langfuse.create_prompt(
        name=name,
        type="text", 
        prompt=prompt_text,
        labels=labels or [],
        config={
            "model": model_name,
            "temperature": temperature,
            "supported_languages": supported_languages or [],
        }
    )
def get_prompt(name, label="production"):
    return langfuse.get_prompt(name=name,label=label)
  
def update_prompt(name, new_prompt_text):
    prompt = langfuse.get_prompt(name=name)
    prompt.update(prompt=new_prompt_text)

def delete_dataset(name):
    dataset = langfuse.get_dataset(name=name)
    dataset.delete()

def get_trace_by_id(trace_id):
    return langfuse.get_trace(trace_id)