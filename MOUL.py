#!/bin/python3
import colorsys
import subprocess
import time
import random as ran
import signal

org = "/sgoinfre/MOUL.py"
name = "YOUHAVEBEENRICHARDSTALLMANd"

def quit(signum, frame):
	exit(0)
signal.signal(signal.SIGINT, quit)
signal.signal(signal.SIGTERM, quit)

print(__file__)

if (__file__ == org):
	subprocess.run([
		"cp", f"{org}", f"/tmp/{name}.py"
	])
	subprocess.run([
    		"gnome-terminal", "-x", "bash", "-c", f"/tmp/{name}.py"
	])
	time.sleep(2)
	subprocess.run([
		"rm", "-rf", f"/tmp/{name}.py"
	])
	exit(0)

time.sleep(120)
while (True):
	subprocess.run([
		"feh", "-F", "-Z", "/sgoinfre/moulinette face reveal.png"
	])
	time.sleep(ran.randint(120, 500))

