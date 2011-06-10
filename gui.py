#!/usr/bin/python
import os
import sys

sys.path += [ os.getcwd() ]

import_worked = False
for implementation in os.listdir("guis"):
	try:
		__import__("guis." + implementation[:-3])
		import_worked = True
	except ImportError:
		# Try next implementation
		continue
	except ValueError:
		# This only occours because I was to lazy to check for __init__
		continue
if not import_worked:
	print >> sys.stdout, "No suitable GUI module was found. Please install either PyGTK or Tkinter"
