#!/bin/bash

# Circle Catch Game Launcher
# This script checks dependencies and starts the game

echo "==================================="
echo "  Circle Catch Game Launcher"
echo "==================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed."
    echo "Please install Python 3 to run this game."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null && ! command -v pip &> /dev/null; then
    echo "Warning: pip is not installed."
    echo "Installing dependencies may fail."
fi

# Check if requirements are installed
echo "Checking dependencies..."
if ! python3 -c "import pygame" &> /dev/null || ! python3 -c "import numpy" &> /dev/null; then
    echo "Some dependencies are missing."
    echo "Installing requirements..."
    pip3 install -r requirements.txt || pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "Error: Failed to install dependencies."
        exit 1
    fi
    echo "Dependencies installed successfully!"
else
    echo "All dependencies are already installed."
fi

echo ""
echo "Starting Circle Catch Game..."
echo "Controls: Move mouse to catch circles, press Q to quit"
echo ""

# Run the game with any command line arguments passed to the script
python3 circle_game.py "$@"
