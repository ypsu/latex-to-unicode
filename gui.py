#!/usr/bin/python
import os
import sys

sys.path += [ os.getcwd(), os.getcwd() + "/guis" ]

for implementation in os.listdir("guis"):
	if implementation[-6:] != "gui.py":
		continue
	try:
		__import__(implementation[:-3])
		sys.exit(0)
	except ImportError:
		# Try next implementation
		continue
	except ValueError:
		# This only occours because I was to lazy to check for __init__
		continue
sys.stderr.write("No suitable GUI module was found. Please install either PyGTK or Tkinter\n")
