import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import argparse
from fusewill_utils import (
    list_traces,
    create_dataset,
    create_prompt,
    update_prompt,
    delete_dataset,
    get_trace_by_id
)
import dotenv
import json
dotenv.load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="Langfuse CLI Wrapper")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # list_traces command
    parser_list = subparsers.add_parser('list_traces', help='List traces')
    parser_list.add_argument('--limit', type=int, default=100, help='Number of traces to fetch')
    parser_list.add_argument('--output_dir', type=str, default='../output/traces', help='Directory to save traces')

    # create_dataset command
    parser_create_dataset = subparsers.add_parser('create_dataset', help='Create a new dataset')
    parser_create_dataset.add_argument('name', help='Name of the dataset')
    parser_create_dataset.add_argument('--description', default='', help='Description of the dataset')
    parser_create_dataset.add_argument('--metadata', type=str, default='{}', help='Metadata in JSON format')

    # create_prompt command
    parser_create_prompt = subparsers.add_parser('create_prompt', help='Create a new prompt')
    parser_create_prompt.add_argument('name', help='Name of the prompt')
    parser_create_prompt.add_argument('prompt_text', help='Prompt text')
    parser_create_prompt.add_argument('--model_name', default='gpt-4o-mini', help='Model name')
    parser_create_prompt.add_argument('--temperature', type=float, default=0.7, help='Temperature')
    parser_create_prompt.add_argument('--labels', nargs='*', default=[], help='Labels for the prompt')
    parser_create_prompt.add_argument('--supported_languages', nargs='*', default=[], help='Supported languages')

    # update_prompt command
    parser_update_prompt = subparsers.add_parser('update_prompt', help='Update an existing prompt')
    parser_update_prompt.add_argument('name', help='Name of the prompt')
    parser_update_prompt.add_argument('new_prompt_text', help='New prompt text')

    # delete_dataset command
    parser_delete_dataset = subparsers.add_parser('delete_dataset', help='Delete a dataset')
    parser_delete_dataset.add_argument('name', help='Name of the dataset')

    # get_trace_by_id command
    parser_get_trace = subparsers.add_parser('get_trace_by_id', help='Get a trace by ID')
    parser_get_trace.add_argument('trace_id', help='Trace ID')

    args = parser.parse_args()

    if args.command == 'list_traces':
        list_traces(limit=args.limit, output_dir=args.output_dir)
    elif args.command == 'create_dataset':
        metadata = json.loads(args.metadata)
        create_dataset(name=args.name, description=args.description, metadata=metadata)
    elif args.command == 'create_prompt':
        create_prompt(
            name=args.name,
            prompt_text=args.prompt_text,
            model_name=args.model_name,
            temperature=args.temperature,
            labels=args.labels,
            supported_languages=args.supported_languages
        )
    elif args.command == 'update_prompt':
        update_prompt(name=args.name, new_prompt_text=args.new_prompt_text)
    elif args.command == 'delete_dataset':
        delete_dataset(name=args.name)
    elif args.command == 'get_trace_by_id':
        trace = get_trace_by_id(trace_id=args.trace_id)
        print(trace)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()