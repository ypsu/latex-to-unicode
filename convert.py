def convert(s):
	global data_loaded

	if data_loaded == False:
		load_data()
		data_loaded = True

	ss = convert_single_symbol(s)
	if ss != None:
		return ss

	s = convert_latex_symbols(s)
	s = apply_modifier(s, "^", superscripts)
	s = apply_modifier(s, "_", subscripts)
	s = apply_modifier(s, "\\bb", textbb)
	s = apply_modifier(s, "\\bf", textbf)
	s = apply_modifier(s, "\\it", textit)
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
			newtext += translate_if_possible(ch, D)
			mode = mode_normal
			continue
		elif mode == mode_long and ch == '}':
			mode = mode_normal
			continue

		if mode == mode_normal:
			newtext += ch
		else:
			newtext += translate_if_possible(ch, D)
	return newtext

def translate_if_possible(ch, d):
	if ch in d:
		return d[ch]
	return ch

def load_data():
	global blackboard, subscripts, superscripts

	load_symbols()
	load_dict("data/subscripts", subscripts)
	load_dict("data/superscripts", superscripts)
	load_dict("data/textbb", textbb)
	load_dict("data/textbf", textbf)
	load_dict("data/textit", textit)

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
latex_symbols = []
