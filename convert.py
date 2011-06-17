import re

def convert(s):
	global data_loaded

	if data_loaded == False:
		load_data()
		data_loaded = True

	ss = convert_single_symbol(s)
	if ss != None:
		return ss

	s = convert_latex_symbols(s)
	s = process_starting_modifiers(s)
	s = apply_all_modifiers(s)
	return s

# If s is just a latex code "alpha" or "beta" it converts it to its
# unicode representation.
def convert_single_symbol(s):
	ss = "\\" + s
	for (code, val) in latex_symbols:
		if code == ss:
			return val
	return None

# Replace each "\alpha", "\beta" and similar latex symbols with
# their unicode representation.
def convert_latex_symbols(s):
	for (code, val) in latex_symbols:
		s = s.replace(code, val)
	return s

# If s start with "it ", "cal ", etc. then make the whole string
# italic, calligraphic, etc.
def process_starting_modifiers(s):
	s = re.sub("^bb ", r"\\bb{", s)
	s = re.sub("^bf ", r"\\bf{", s)
	s = re.sub("^it ", r"\\it{", s)
	s = re.sub("^cal ", r"\\cal{", s)
	s = re.sub("^frak ", r"\\frak{", s)
	s = re.sub("^mono ", r"\\mono{", s)
	return s

def apply_all_modifiers(s):
	s = apply_modifier(s, "^", superscripts)
	s = apply_modifier(s, "_", subscripts)
	s = apply_modifier(s, "\\bb", textbb)
	s = apply_modifier(s, "\\bf", textbf)
	s = apply_modifier(s, "\\it", textit)
	s = apply_modifier(s, "\\cal", textcal)
	s = apply_modifier(s, "\\frak", textfrak)
	s = apply_modifier(s, "\\mono", textmono)
	return s

# Example: modifier = "^", D = superscripts
# This will search for the ^ signs and replace the next
# digit or (digits when {} is used) with its/their uppercase representation.
def apply_modifier(text, modifier, D):
	text = text.replace(modifier, "^")
	newtext = ""
	mode_normal, mode_modified, mode_long = range(3)
	mode = mode_normal
	for ch in text:
		if mode == mode_normal and ch == '^':
			mode = mode_modified
			continue
		elif mode == mode_modified and ch == '{':
			mode = mode_long
			continue
		elif mode == mode_modified:
			newtext += D.get(ch, ch)
			mode = mode_normal
			continue
		elif mode == mode_long and ch == '}':
			mode = mode_normal
			continue

		if mode == mode_normal:
			newtext += ch
		else:
			newtext += D.get(ch, ch)
	return newtext

def load_data():
	load_symbols()
	load_dict("data/subscripts", subscripts)
	load_dict("data/superscripts", superscripts)
	load_dict("data/textbb", textbb)
	load_dict("data/textbf", textbf)
	load_dict("data/textit", textit)
	load_dict("data/textcal", textcal)
	load_dict("data/textfrak", textfrak)
	load_dict("data/textmono", textmono)

def load_dict(filename, D):
	with open(filename, "r") as f:
		line = f.readline()
		while line != "":
			words = line.split()
			code = words[0]
			val = words[1]
			D[code] = val
			line = f.readline()

def load_symbols():
	with open("data/symbols", "r") as f:
		line = f.readline()
		while line != "":
			words = line.split()
			code = words[0]
			val = words[1]
			latex_symbols.append((code, val))
			line = f.readline()


data_loaded = False

superscripts = {}
subscripts = {}
textbb = {}
textbf = {}
textit = {}
textcal = {}
textfrak = {}
textmono = {}
latex_symbols = []
