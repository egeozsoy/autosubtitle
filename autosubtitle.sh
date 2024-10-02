#!/bin/bash

# Check if the virtual environment directory exists
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate the virtual environment
source .venv/bin/activate

# Install dependencies if not already installed
if [ ! -f ".venv/installed.txt" ]; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
    touch .venv/installed.txt
fi

# Run the tool
echo "Running autosubtitle..."
python autosubtitle.py "$@"

# Deactivate the virtual environment after running
deactivate

