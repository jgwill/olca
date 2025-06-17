#!/data/data/com.termux/files/usr/bin/bash
# Simple helper to install olca on Termux

set -e

# Use python3.11 if available
pkg install -y python git clang

python3 -m pip install --upgrade pip

# install dependencies without langfuse or google generative ai
# includes python-dotenv for environment loading
python3 -m pip install -r requirements.txt

# install package in editable mode
python3 -m pip install -e .

echo "oLCa installed. Run 'olca --help' to get started."
