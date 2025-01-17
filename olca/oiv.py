#!/bin/env python
#@STCGoal Create an agent callable with command line
#@STCIssue The original script was not callable from the command line.

from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_openai import ChatOpenAI
import argparse
import os
import json
import tlid
import warnings

warnings.filterwarnings("ignore", message="The function `loads` is in beta. It is actively being worked on, so the API may change.")
DEBUG_MODE=False

prompt=None
def _create_agent_tools(tool_name = "arxiv",temperature = 0.0,tool_hub_tag = "jgwill/react",chatbot_model = "gpt-4o-mini"):
    global prompt
    
    llm = ChatOpenAI(temperature=temperature,name=chatbot_model)
    
    tools = load_tools(
        [tool_name],
        )
    if DEBUG_MODE:
          
      print("Tools:")
      print(tools)
      print("--------------")
    prompt = hub.pull(tool_hub_tag)
    
    if DEBUG_MODE:
      print("prompt:")
      print(prompt)
      print("--------------")

    agent = create_react_agent(llm, tools, prompt)
    
    if DEBUG_MODE:
      print("Agent:")
      print(agent)
      print("--------------")
    return tools,agent


def create_agent_executor(tools, agent) -> AgentExecutor:
    return AgentExecutor(agent=agent, tools=tools, verbose=True,handle_parsing_errors=True)
   



# tools, agent=_create_agent_tools()

# agent_executor=create_agent_executor(tools, agent)
def ask_agent(input_request, agent_executor=None,tool_hub_tag = "jgwill/react",chatbot_model = "gpt-4o-mini"):
  if agent_executor is None:
    tools, agent = _create_agent_tools(tool_hub_tag=tool_hub_tag)
    agent_executor = create_agent_executor(tools, agent)
  
  resp = agent_executor.invoke(
    {
      "input": input_request,
    }
  )
  
  return resp

def serialize_response_to_json(resp):
    return json.dumps(resp)

def serialize_response_to_json_file(resp, filename):
  json_str=serialize_response_to_json(resp)
  with open(filename, 'w') as f:
    f.write(json_str)
    
def serialize_response_to_markdown(o):
    output=o["output"]
    string_md="# Output\n"
    #string_md+=f"## Model\n{o['model']}\n"
    #string_md+=f"## Prompt\n{o['prompt']['prompt']}\n"
    string_md+=f"## Input\n{o['input']}\n"
    string_md+=f"## Output\n{output}\n"
    return string_md

def serialize_response_to_markdown_file(o, filename):
    string_md=serialize_response_to_markdown(o)
    with open(filename, 'w') as f:
        f.write(string_md)


def main():
    global prompt
    args = parse_cli_arguments()

    input_request = args.input
    tool_hub_tag = "jgwill/react" if args.hub_tag is None else args.hub_tag
    resp = ask_agent(input_request,tool_hub_tag=tool_hub_tag,chatbot_model=args.chatbot_model)
    outdir=os.path.join(os.getcwd(),"output")
    os.makedirs(outdir, exist_ok=True)
    out_filename = f"{args.prefix}{tlid.get_minutes()}.json"
    outfile=os.path.join(outdir,out_filename)
    o={}
    prompt_dict = {
        "promptdata": str(prompt)
    }
    o["model"]=args.chatbot_model
    o["prompt"]=prompt_dict
    o["input"]=input_request
    o["output"]=resp["output"]
    serialize_response_to_json_file(o, outfile)
    serialize_response_to_markdown_file(o, outfile.replace(".json",".md"))
    VERBOSE_RESULT=False
    if VERBOSE_RESULT:
        print("==================================")
        print(input_request)
        print("============RESPONSE============")
        print(resp)
        print("==================================")
        print("=============INPUT Request=====================")
        print(input_request)
        print("==================================")
        print("============OUTPUT============")
    output=resp["output"]
    print(output)

def parse_cli_arguments():
    parser = argparse.ArgumentParser(description='Process Input request for pattern search.')
    parser.add_argument('-I','--input', type=str,
                        help='an input request for the searched article')
    ##--hub_tag
    parser.add_argument('-H','-ht','--hub_tag', type=str,
                        help='The hub tag for the process',default="jgwill/react")
    #--chatbot_model
    parser.add_argument('-M','-m','--chatbot_model', type=str,
                        help='a chatbot model for the processing',default="gpt-4o-mini")
    #--prefix
    parser.add_argument('-P','-p','--prefix', type=str,
                        help='a file prefix for output',default="arxiv-")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main()
