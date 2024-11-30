#!/bin/python3

import subprocess
import time
import signal
import atexit

def set(value):
	subprocess.run(["xrandr", "--output", "eDP", "--brightness", str(round(value, 3))]);

def quit(signum, frame):
	# fix before exit
	set(1);
	exit(0);
signal.signal(signal.SIGINT, quit);
signal.signal(signal.SIGTERM, quit);
atexit.register(quit)

val = 1;
by = 0.001;		# amount of brightness decrease per iteration
t = 0.3; 		# time in seconds between iterations
fixdelay = 1; 	# time in seconds when brightness reaches 0 until it gets set back to 1

subprocess.run(["clear"]);
subprocess.Popen(["zsh"]);

time.sleep(30);
while (True):
	val = 1;
	while (val > 0):
		set(val);
		val -= by;
		time.sleep(t);
	time.sleep(fixdelay);
	set(1);
