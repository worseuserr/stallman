#!/bin/python3
import subprocess
import time

i = 0
while (i <= 50):
	subprocess.Popen(["gnome-terminal", "-x", "bash", "-c", f"/sgoinfre/ENOUL.py"])
	i += 1
	time.sleep(0.01)
