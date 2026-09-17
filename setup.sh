#!/usr/bin/env sh

set -eu

PROJECT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
VENV_DIR="$PROJECT_DIR/venv"

if ! command -v python3 >/dev/null 2>&1; then
    echo "Error: Python 3 is not installed."
    exit 1
fi

if ! python3 -c "import tkinter" >/dev/null 2>&1; then
    echo "Error: Tkinter is not installed."
    echo "On Ubuntu/Debian install it with: sudo apt install python3-tk"
    exit 1
fi

if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
fi

echo "Installing dependencies..."
"$VENV_DIR/bin/python" -m pip install --upgrade pip
"$VENV_DIR/bin/python" -m pip install "customtkinter==6.0.0"

echo "Setup complete."
echo "Run SpicyMacro with: $VENV_DIR/bin/python $PROJECT_DIR/main.py"
