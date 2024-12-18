#!/bin/python3
import sys
import json

# script to easily fetch info about any file in /scripts as long as there is an entry in the .info.json file.
# use like ./info.py {filename}
# not case sensitive, shows all entries that match (even just partly) with the filename e.g. "./info.py moul" will show info about MOUL and EMOUL.

if (len(sys.argv) != 2):
	print("Enter the name (or part thereof) of a filename in /scripts to get info about the script.\nUsage:\n\t./sinfo.py {filename}\n\t./sinfo.py all")
	exit(1)

def output(file, data):
	does = data['DOES'].replace("\n", f"\n\t{' '*len('Description: ')}")
	strn = f"{('-'*border) if count<2 else ''}\n\nEntry: {file}\n\n\tFile name:   {data['FILE']}\n\tRisk:        {data['RISK']}\n\tDescription: {does}\n\n{'-'*border}"
	print(strn, end = '')

arg = sys.argv[1]
count = 0
border = 50
if (arg[-3:] == '.sm'):
	arg = arg[:-3]
with open('.info.json', 'r') as file:
	infoList = json.load(file)
	if (arg.lower() == "risk"):
		print(f"{('-'*border)}\n\nEntry: RISK\n\n\tRISK: {infoList['RISK']}\n\n{'-'*border}")
		exit(0)
	for file, data in infoList.items():
		if (arg.lower() in file.lower() or (arg == "all" and file != "RISK")):
			count += 1
			output(file, data)
	if (count == 0):
		print(f"No entries found for '{arg}'.")
		exit(1)
	print('\n')
