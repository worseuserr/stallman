#!/bin/bash

# Specify the hardcoded directory where the Python files are located
HARD_CODED_DIR="/sgoinfre"

# Check if the directory exists
if [ ! -d "$HARD_CODED_DIR" ]; then
    echo "The specified directory does not exist: $HARD_CODED_DIR"
    exit 1
fi

# Iterate through all Python files in the hardcoded directory
for file in "$HARD_CODED_DIR"/*.py; do
    # Check if the file exists in the current directory
    if [ -f "./$(basename "$file")" ]; then
        echo "Removing Python file: $file"
        rm -rf "$file"
    fi
done

echo "Done removing matching Python files."
