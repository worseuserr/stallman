#!/bin/python3
import colorsys
import subprocess
import time
import random as ran
import signal

def quit(signum, frame):
	exit(0)
signal.signal(signal.SIGINT, quit)
signal.signal(signal.SIGTERM, quit)

subprocess.run(["clear"])
subprocess.Popen(["zsh"])
time.sleep(120)
while (True):
	time.sleep(120)
	subprocess.run(["feh", "-F", "-Z", "/sgoinfre/moulinette face reveal.png"])
	time.sleep(ran.randint(120, 500))
