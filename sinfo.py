#!/bin/python3
import sys
import json

# script to easily fetch info about any file in /files as long as there is an entry in the .info.json file.
# use like ./sinfo.py {filename}
# not case sensitive, shows all entries that match (even just partly) with the filename e.g. "./sinfo.py moul" will show info about MOUL and EMOUL.

if (len(sys.argv) != 2):
	print("Enter the name (or part thereof) of a filename in /files to get info about the script.\nUsage:\n\t./sinfo.py {filename}")
	exit(1)

def output(file, data):
	print(f"{('-'*border) if count<2 else '\b'}\n\nEntry: {file}\n\tFile name:   {data["FILE"]}\n\tRisk:        {data["RISK"]}\n\tDescription: {data["DOES"]}\n\n{'-'*border}", end = '')

arg = sys.argv[1]
count = 0
border = 50
if (arg[-3:] == '.py'):
	arg = arg[:-3]
with open('.info.json', 'r') as file:
	infoList = json.load(file)
	for file, data in infoList.items():
		if (arg.lower() in file.lower()):
			count += 1
			output(file, data)
	if (count == 0):
		print(f"No entries found for '{arg}'.")
		exit(1)
