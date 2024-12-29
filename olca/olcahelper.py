import os
import yaml

def ensure_directories_exist(extra_directories=None):
    directories = ['./reports', './log', './.olca']
    if extra_directories:
        directories += extra_directories
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)

def extract_extra_directories_from_olca_config_system_and_user_input(system_instructions, user_input):
    extra_directories = []
    for input in [system_instructions, user_input]:
        if input:
            for word in input.split():
                if word.startswith("./") and word.endswith("/"):
                    extra_directories.append(word)
    return extra_directories

def setup_required_directories(system_instructions, user_input):
    try:
        extra_directories = extract_extra_directories_from_olca_config_system_and_user_input(system_instructions, user_input)
        ensure_directories_exist(extra_directories)
    except:
        ensure_directories_exist()

def initialize_config_file():
    try:
        default_system_instructions = "You are interacting using the human tool addressing carefully what the user is asking."
        default_user_input = "Interact with me to write a story using the 3 act structure that we will save in ./story/ - Make sure you interact with me and wont quit."
        
        default_model_name = "gpt-4o-mini"
        default_recursion_limit = 12
        default_temperature = 0
        use_default_human_input = True
        use_default_tracing = True

        config = {
            "api_keyname": input("api_keyname [OPENAI_API_KEY]: ") or "OPENAI_API_KEY",
            "model_name": input("model_name [gpt-4o-mini]: ") or default_model_name,
            "recursion_limit": int(input("recursion_limit [12]: ") or default_recursion_limit),
            "temperature": float(input("temperature [0]: ") or default_temperature),
            "human": input("human [true]: ").lower() in ["true", "yes", "y", "1", ""] or use_default_human_input,
            "tracing": input("tracing [true]: ").lower() in ["true", "yes", "y", "1", ""] or use_default_tracing,
            "tracing_providers": ["langsmith", "langfuse"]
        }
        
        user_system_instructions = input(f"system_instructions [{default_system_instructions}]: ")
        user_system_instructions = user_system_instructions or default_system_instructions
        user_system_instructions = user_system_instructions.replace("\n", " ").replace("\r", " ").replace("\t", " ")

        user_core_input = input(f"user_input [{default_user_input}]: ")
        user_core_input = user_core_input or default_user_input
        user_core_input = user_core_input.replace("\n", " ").replace("\r", " ").replace("\t", " ")
        
        config["system_instructions"] = user_system_instructions
        config["user_input"] = user_core_input

        with open('olca.yml', 'w') as file:
            yaml.dump(config, file)
        print("Configuration file 'olca.yml' created successfully.")
        inputs, system_instructions, user_input = prepare_input(config["user_input"], config["system_instructions"], True, config["human"])
        setup_required_directories(system_instructions, user_input)
    except KeyboardInterrupt:
        print("\nConfiguration canceled by user.")
        exit(0)
