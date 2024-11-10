#!/bin/bash

echo "Pushing for $1 seconds."

./push.sh

sleep $1

./remove.sh

echo "Time over, files removed."

