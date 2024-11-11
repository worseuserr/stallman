#!/bin/python3
import colorsys
import subprocess
import time
import random as ran
import signal

valstart = 50
gamstart = 2

startmult = 1

by = 0.025

def lerp(val, goal, t):
	return val + (goal - val) * t

#subprocess.run(["xrandr", "--output", "eDP", "--gamma", f"{val}:{val}:{val}"])
def boom():
	val = valstart * startmult
	gam = gamstart * startmult
	flash = subprocess.Popen(["feh", "-F", "-Z", "/sgoinfre/thinkfast.jpg"])
	time.sleep(0.9)
	subprocess.Popen(["feh", "-F", "-Z", "/sgoinfre/moulinette face reveal.png"])
	subprocess.run(["xrandr", "--output", "eDP", "--brightness", "0"])
	time.sleep(0.15)
	subprocess.run(["xrandr", "--output", "eDP", "--brightness", f"{val}", "--gamma", f"{gam}:{gam}:{gam}"])
	flash.kill()
	while (val > 1 or gam > 1):
		if (val > 1):
			val = lerp(val, 0.95, by)
		if (gam > 1):
			gam = lerp(gam, 0.95, by)
		subprocess.run(["xrandr", "--output", "eDP", "--brightness", f"{val}", "--gamma", f"{gam}:{gam}:{gam}"])
		time.sleep(0.01)
	subprocess.run(["xrandr", "--output", "eDP", "--brightness", "1", "--gamma", "1"])


def quit(signum, frame):
	exit(0)
signal.signal(signal.SIGINT, quit)
signal.signal(signal.SIGTERM, quit)

subprocess.run(["clear"])
subprocess.Popen(["zsh"])
time.sleep(10)
while (True):
	boom()
	time.sleep(ran.randint(120, 500))
