#!/bin/python3
import colorsys
import subprocess
import time
import random as ran
import signal
import os

loc = "/sgoinfre/moulinette_face_reveal.png"
username = os.getlogin()


def quit(signum, frame):
	exit(0)
signal.signal(signal.SIGINT, quit)
signal.signal(signal.SIGTERM, quit)

subprocess.run(["mv", f"/home/{username}/.face", f"/home/{username}/YOUGOTSTALLMAND"])
subprocess.run(["cp", "-fr", f"{loc}", f"/home/{username}/.face"])
subprocess.run(["clear"])
subprocess.run(["zsh"])
