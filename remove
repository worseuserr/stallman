#!/bin/bash

TARGET_DIR="/sgoinfre"

if [ ! -d "$TARGET_DIR" ]; then
	echo "$TARGET_DIR not found, wtf??"
	exit 1
fi

for file in "$TARGET_DIR"/*.sm; do
	if [ -f "./scripts/$(basename "$file")" ]; then
		echo "Removing Python file: $file"
		rm -rf "$file"
	fi
done

echo "Done removing matching Python files."
