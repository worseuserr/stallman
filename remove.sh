#!/bin/bash

HARD_CODED_DIR="/sgoinfre"

if [ ! -d "$HARD_CODED_DIR" ]; then
    echo "The specified directory does not exist: $HARD_CODED_DIR"
    exit 1
fi

for file in "$HARD_CODED_DIR"/*.py; do
    if [ -f "./files/$(basename "$file")" ]; then
        echo "Removing Python file: $file"
        rm -rf "$file"
    fi
done

echo "Done removing matching Python files."
