#!/bin/bash

TARGET_DIR="/sgoinfre"

if [ ! -d "$TARGET_DIR" ]; then
  echo "Error: Target directory does not exist."
  exit 1
fi

for file in files/*.py; do
  if [ -f "$file" ]; then
    chmod 755 "$file"
    cp "$file" "$TARGET_DIR"
    echo "Copied: $file"
  fi
done

echo "All .py files have been copied."
