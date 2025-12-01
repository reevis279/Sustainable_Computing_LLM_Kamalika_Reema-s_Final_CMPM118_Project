#bash script to make sure ollama is install within WSL

#!/bin/bash

# Check if the 'ollama' command exists
if command -v ollama &> /dev/null; then
    echo "Ollama is installed. Version information:"
    ollama --version
else
    echo "Ollama is not installed or not found in your PATH."
    echo "You can download and install it from https://ollama.com/download"
fi