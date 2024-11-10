#!/bin/bash

# Define the target directory
TARGET_DIR="/sgoinfre"

# Check if the target directory exists
if [ ! -d "$TARGET_DIR" ]; then
  echo "Error: Target directory does not exist."
  exit 1
fi

# Move all .py files in the current directory to the target directory
for file in *.py; do
  if [ -f "$file" ]; then
    chmod 755 "$file"
    cp "$file" "$TARGET_DIR"
    echo "Copied: $file"
  fi
done

echo "All .py files have been copied."
