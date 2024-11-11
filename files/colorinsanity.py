#!/bin/python3
import subprocess
import time

def quit(signum, frame):
	exit(0)
signal.signal(signal.SIGINT, quit)
signal.signal(signal.SIGTERM, quit)

