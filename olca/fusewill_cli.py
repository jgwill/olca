from ast import alias
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import argparse
import fusewill_utils as fu
from fusewill_utils import (
    list_traces,
    create_dataset,
    create_prompt,
    update_prompt,
    delete_dataset,
    get_trace_by_id,
    open_trace_in_browser,
    print_traces,
    print_trace,
    list_traces_by_score,  # Ensure the updated function is imported
    export_traces,
    import_traces
)
import dotenv
import json
import sys, termios, tty
#dotenv.load_dotenv()

def get_single_char_input():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def main():
    parser = argparse.ArgumentParser(description="FuseWill Langfuse CLI Wrapper")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # list_traces command
    parser_list = subparsers.add_parser('list_traces', help='List traces',aliases=['lt'])
    parser_list.add_argument('-L','--limit', type=int, default=100, help='Number of traces to fetch')
    parser_list.add_argument('--output_dir', type=str, default='../output/traces', help='Directory to save traces')
    parser_list.add_argument('-C','--comments',  action='store_true', help='Show comments from the traces', default=False)
    parser_list.add_argument('-W','--browse-interact', action='store_true', help='Ask user to open each trace in browser')

    # create_dataset command
    parser_create_dataset = subparsers.add_parser('create_dataset', help='Create a new dataset',aliases=['cd'])
    parser_create_dataset.add_argument('name', help='Name of the dataset')
    parser_create_dataset.add_argument('-D','--description', default='', help='Description of the dataset')
    parser_create_dataset.add_argument('-M','--metadata', type=str, default='{}', help='Metadata in JSON format')

    # create_prompt command
    parser_create_prompt = subparsers.add_parser('create_prompt', help='Create a new prompt',aliases=['cp'])
    parser_create_prompt.add_argument('name', help='Name of the prompt')
    parser_create_prompt.add_argument('prompt_text', help='Prompt text')
    parser_create_prompt.add_argument('--model_name', default='gpt-4o-mini', help='Model name')
    parser_create_prompt.add_argument('--temperature', type=float, default=0.7, help='Temperature')
    parser_create_prompt.add_argument('--labels', nargs='*', default=[], help='Labels for the prompt')
    parser_create_prompt.add_argument('--supported_languages', nargs='*', default=[], help='Supported languages')

    # update_prompt command
    parser_update_prompt = subparsers.add_parser('update_prompt', help='Update an existing prompt',aliases=['up'])
    parser_update_prompt.add_argument('name', help='Name of the prompt')
    parser_update_prompt.add_argument('new_prompt_text', help='New prompt text')

    # delete_dataset command
    parser_delete_dataset = subparsers.add_parser('delete_dataset', help='Delete a dataset')
    parser_delete_dataset.add_argument('name', help='Name of the dataset')

    # get_trace_by_id command
    parser_get_trace = subparsers.add_parser('get_trace_by_id', help='Get a trace by ID',aliases=['gt'])
    parser_get_trace.add_argument('trace_id', help='Trace ID')

    # new_score command
    parser_new_score = subparsers.add_parser('new_score', help='Create a new score',aliases=['ns'])
    parser_new_score.add_argument('name', help='Score name')
    parser_new_score.add_argument('data_type', help='Data type of the score')
    parser_new_score.add_argument('--description', default='', help='Description of the score')

    # add_score_to_trace command
    parser_add_score = subparsers.add_parser('add_score_to_trace', help='Add a score to a trace', aliases=['s2t'])
    parser_add_score.add_argument('trace_id', help='Trace ID')
    parser_add_score.add_argument('generation_id', help='Generation ID')
    parser_add_score.add_argument('name', help='Score name')
    parser_add_score.add_argument('value', help='Score value')
    parser_add_score.add_argument('--data_type', default='NUMERIC', help='Data type of the score')
    parser_add_score.add_argument('--comment', default='', help='Comment for the score')

    # list_traces_by_score command
    parser_list_by_score = subparsers.add_parser('list_traces_by_score', help='List traces by score', aliases=['ltbs','lbys','lts'])
    parser_list_by_score.add_argument('score_name', help='Score name')
    parser_list_by_score.add_argument('--min_value', type=float, help='Minimum score value')
    parser_list_by_score.add_argument('--max_value', type=float, help='Maximum score value')
    parser_list_by_score.add_argument('-L','--limit', type=int, default=100, help='Number of traces to fetch')

    # list_scores command
    parser_list_scores = subparsers.add_parser('list_scores', help='List all scores', aliases=['ls'])
    parser_list_scores.add_argument('-o', '--output', type=str, help='Output JSON file path')

    # search_traces command
    parser_search = subparsers.add_parser('search_traces', help='Search and filter traces with advanced options', aliases=['st'])
    parser_search.add_argument('--start_date', type=str, help='Start date in ISO format (e.g., 2024-01-01)')
    parser_search.add_argument('--end_date', type=str, help='End date in ISO format (e.g., 2024-12-31)')
    parser_search.add_argument('--keywords', nargs='*', help='Keywords to search in input or output')
    parser_search.add_argument('--tags', nargs='*', help='Tags to filter traces')
    parser_search.add_argument('--metadata', nargs='*', help='Metadata filters in key=value format')
    parser_search.add_argument('-L', '--limit', type=int, default=100, help='Number of traces to fetch')
    parser_search.add_argument('-o', '--output', type=str, help='Output JSON file path')

    # export_traces command
    parser_export = subparsers.add_parser('export_traces', help='Export traces', aliases=['et'])
    parser_export.add_argument('--format', choices=['json','csv'], default='json', help='Export format')
    parser_export.add_argument('-o','--output', type=str, help='Output file path')
    parser_export.add_argument('--start_date', type=str, help='Start date in ISO format (e.g., 2024-01-01)')
    parser_export.add_argument('--end_date', type=str, help='End date in ISO format (e.g., 2024-12-31)')

    # import_traces command
    parser_import = subparsers.add_parser('import_traces', help='Import traces', aliases=['it'])
    parser_import.add_argument('--format', choices=['json','csv'], default='json', help='Import format')
    parser_import.add_argument('--input', type=str, required=True, help='Input file path to read from')

    args = parser.parse_args()

    if args.command == 'list_traces' or args.command == 'lt':
        show_comments_flag = args.comments if args.comments else False
        traces = list_traces(
            limit=args.limit, 
            output_dir=args.output_dir
        )
        if not args.browse_interact:
            print_traces(traces, show_comments=show_comments_flag)
        else:
            for trace in traces.data:
                print_trace(trace, show_comments=show_comments_flag)
                print("Open this trace in browser (Y/N/Q)? ", end='', flush=True)
                try:
                    resp = get_single_char_input().lower()
                except KeyboardInterrupt:
                    print("\nExiting.")
                    sys.exit(0)
                print(resp)  # Echo the character
                if resp == 'y':
                    open_trace_in_browser(trace.id)
                elif resp == 'q':
                    print("Quitting.")
                    break
    elif args.command == 'create_dataset' or args.command == 'cd':
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
    elif args.command == 'update_prompt' or args.command == 'up':
        update_prompt(name=args.name, new_prompt_text=args.new_prompt_text)
    elif args.command == 'delete_dataset':
        delete_dataset(name=args.name)
    elif args.command == 'get_trace_by_id' or args.command == 'gt' :
        trace = get_trace_by_id(trace_id=args.trace_id)
        print(trace)
    elif args.command == 'new_score' or args.command == 'ns':
        fu.create_score(name=args.name, data_type=args.data_type, description=args.description)
    elif args.command == 'add_score_to_trace' or args.command == 's2t':
        if not fu.score_exists(name=args.name):
            fu.create_score(name=args.name, data_type=args.data_type)
        fu.add_score_to_a_trace(
            trace_id=args.trace_id,
            generation_id=args.generation_id,
            name=args.name,
            value=args.value,
            data_type=args.data_type,
            comment=args.comment
        )
    elif args.command == 'list_traces_by_score' or args.command == 'ltbs' or args.command == 'lbys' or args.command == 'lts':
        traces = fu.list_traces_by_score(
            score_name=args.score_name,
            min_value=args.min_value,
            max_value=args.max_value,
            limit=args.limit
        )
        for trace in traces:
            print_trace(trace)
            #print(f"Trace ID: {trace.id}, Name: {trace.name}")
    elif args.command == 'list_scores' or args.command == 'ls':
        scores = fu.list_scores()
        if scores:
            if args.output:
                try:
                    with open(args.output, 'w') as f:
                        json.dump(scores, f, indent=2)
                    print(f"Scores written to {os.path.realpath(args.output)}")
                except Exception as e:
                    print(f"Error writing to file {args.output}: {e}")
            else:
                print(json.dumps(scores, indent=2))
        else:
            print("No scores found.")
    elif args.command == 'search_traces' or args.command == 'st':
        metadata_filters = {}
        if args.metadata:
            for item in args.metadata:
                if '=' in item:
                    key, value = item.split('=', 1)
                    metadata_filters[key] = value
                else:
                    print(f"Ignoring invalid metadata filter: {item}")

        traces = fu.search_traces(
            start_date=args.start_date,
            end_date=args.end_date,
            keywords=args.keywords,
            tags=args.tags,
            metadata_filters=metadata_filters,
            limit=args.limit
        )

        if traces:
            if args.output:
                try:
                    with open(args.output, 'w') as f:
                        json.dump([trace.__dict__ for trace in traces], f, indent=2, default=str)
                    print(f"Traces written to {os.path.realpath(args.output)}")
                except Exception as e:
                    print(f"Error writing to file {args.output}: {e}")
            else:
                for trace in traces:
                    fu.print_trace(trace)
        else:
            print("No traces found matching the criteria.")
    elif args.command == 'export_traces' or args.command == 'et':
        output_path = args.output
        if output_path:
            if not output_path.endswith(f".{args.format}"):
                output_path += f".{args.format}"
        fu.export_traces(format=args.format, output_path=output_path, start_date=args.start_date, end_date=args.end_date)
    elif args.command == 'import_traces' or args.command == 'it':
        fu.import_traces(format=args.format, input_path=args.input)
    else:
        parser.print_help()
        exit(1)

if __name__ == '__main__':
    main()