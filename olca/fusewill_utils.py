
from langfuse import Langfuse
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import json

import dotenv
dotenv.load_dotenv()

langfuse = Langfuse()

def list_traces(limit=100, output_dir="../output/traces"):
    traces = langfuse.get_traces(limit=limit)
    os.makedirs(output_dir, exist_ok=True)
    for trace in traces.data:
        print(f"-----Trace ID: {trace.id}--Name: {trace.name}----------")
        print(f"<output>{trace.output}</output>")
        print(f"<Metadata>{trace.metadata}</Metadata>")
        print("---")
    return traces

def add_score_to_a_trace(trace_id, generation_id, name, value, data_type="NUMERIC", comment=""):
    langfuse.score(
        trace_id=trace_id,
        observation_id=generation_id,
        name=name,
        value=value,
        data_type=data_type,
        comment=comment
    )

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
    return langfuse.get_prompt(name=name,label="production")
  
def update_prompt(name, new_prompt_text):
    prompt = langfuse.get_prompt(name=name)
    prompt.update(prompt=new_prompt_text)

def delete_dataset(name):
    dataset = langfuse.get_dataset(name=name)
    dataset.delete()

def get_trace_by_id(trace_id):
    return langfuse.get_trace(trace_id)