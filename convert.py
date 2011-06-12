# vim:fileencoding=utf-8
def convert(s):
	global data_loaded

	if data_loaded == False:
		load_data()
		data_loaded = True

	ss = convert_single_symbol(s)
	if ss != None:
		return ss

	s = convert_latex_symbols(s)
	s = convert_superscripts(s)
	s = convert_subscripts(s)
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

# _23 => ₂3
# _{23} => ₂₃
def convert_superscripts(s):
	s = list(s)
	ss = ""
	mode_normal, mode_caret, mode_long = range(3)
	mode = mode_normal
	for ch in s:
		if mode == mode_normal and ch == '^':
			mode = mode_caret
			continue
		elif mode == mode_caret and ch == '{':
			mode = mode_long
			continue
		elif mode == mode_caret:
			ss += translate_if_possible(ch, superscripts)
			mode = mode_normal
			continue
		elif mode == mode_long and ch == '}':
			mode = mode_normal
			continue

		if mode == mode_normal:
			ss += ch
		else:
			ss += translate_if_possible(ch, superscripts)
	return ss

# ^23 => ²3
# ^{23} => ²³
def convert_subscripts(s):
	s = list(s)
	ss = ""
	mode_normal, mode_caret, mode_long = range(3)
	mode = mode_normal
	for ch in s:
		if mode == mode_normal and ch == '_':
			mode = mode_caret
			continue
		elif mode == mode_caret and ch == '{':
			mode = mode_long
			continue
		elif mode == mode_caret:
			ss += translate_if_possible(ch, subscripts)
			mode = mode_normal
			continue
		elif mode == mode_long and ch == '}':
			mode = mode_normal
			continue

		if mode == mode_normal:
			ss += ch
		else:
			ss += translate_if_possible(ch, subscripts)
	return ss

def translate_if_possible(ch, d):
	if ch in d:
		return d[ch]
	return ch

def load_data():
	global subscripts, superscripts

	print("loading data")
	load_symbols()
	load_dict("data/subscripts", subscripts)
	load_dict("data/superscripts", superscripts)

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
latex_symbols = []
