import re
import sys

def bump_version(file_path, new_version):
    with open(file_path, 'r') as file:
        content = file.read()

    if file_path.endswith('setup.py'):
        content = re.sub(r'version\s*=\s*[\'"]([^\'"]*)[\'"]', f'version = "{new_version}"', content)
    elif file_path.endswith('pyproject.toml'):
        content = re.sub(r'version\s*=\s*[\'"]([^\'"]*)[\'"]', f'version = "{new_version}"', content)
    
    with open(file_path, 'w') as file:
        file.write(content)

def increment_version(version):
    major, minor, patch = map(int, version.split('.'))
    patch += 1
    return f"{major}.{minor}.{patch}"

def get_current_version(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    match = re.search(r'version\s*=\s*[\'"]([^\'"]*)[\'"]', content)
    return match.group(1) if match else None

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: python bump.py")
        sys.exit(1)

    current_version = get_current_version('pyproject.toml')
    if current_version is None:
        print("Error: Could not find the current version.")
        sys.exit(1)
        
    new_version = increment_version(current_version)

    files_to_update = [
        'setup.py',
        'pyproject.toml'
    ]

    for file_path in files_to_update:
        bump_version(file_path, new_version)

    print(f"Version bumped to {new_version} in {', '.join(files_to_update)}")