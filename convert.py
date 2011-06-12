# vim:fileencoding=utf-8
def convert(s):
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
			ss += translate_if_possible(ch, supscripts)
			mode = mode_normal
			continue
		elif mode == mode_long and ch == '}':
			mode = mode_normal
			continue

		if mode == mode_normal:
			ss += ch
		else:
			ss += translate_if_possible(ch, supscripts)
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

supscripts = {}
supscripts["0"] = "⁰"
supscripts["1"] = "¹"
supscripts["2"] = "²"
supscripts["3"] = "³"
supscripts["4"] = "⁴"
supscripts["5"] = "⁵"
supscripts["6"] = "⁶"
supscripts["7"] = "⁷"
supscripts["8"] = "⁸"
supscripts["9"] = "⁹"
supscripts["+"] = "⁺"
supscripts["-"] = "⁻"
supscripts["="] = "⁼"

subscripts = {}
subscripts["0"] = "₀"
subscripts["1"] = "₁"
subscripts["2"] = "₂"
subscripts["3"] = "₃"
subscripts["4"] = "₄"
subscripts["5"] = "₅"
subscripts["6"] = "₆"
subscripts["7"] = "₇"
subscripts["8"] = "₈"
subscripts["9"] = "₉"
subscripts["+"] = "₊"
subscripts["-"] = "₋"
subscripts["="] = "₌"

latex_symbols = [
	("\\alpha", "α"),
	("\\beta", "β"),
	("\\gamma", "γ"),
	("\\delta", "δ"),
	("\\epsilon", "∊"),
	("\\varepsilon", "ε"),
	("\\zeta", "ζ"),
	("\\eta", "η"),
	("\\theta", "θ"),
	("\\vartheta", "ϑ"),
	("\\iota", "ι"),
	("\\kappa", "κ"),
	("\\lambda", "λ"),
	("\\mu", "μ"),
	("\\nu", "ν"),
	("\\xi", "ξ"),
	("\\pi", "π"),
	("\\varpi", "ϖ"),
	("\\rho", "ρ"),
	("\\varrho", "ϱ"),
	("\\sigma", "σ"),
	("\\varsigma", "ς"),
	("\\tau", "τ"),
	("\\upsilon", "υ"),
	("\\phi", "φ"),
	("\\varphi", "ϕ"),
	("\\chi", "χ"),
	("\\psi", "ψ"),
	("\\omega", "ω"),
	("\\Gamma", "Γ"),
	("\\Delta", "Δ"),
	("\\Theta", "Θ"),
	("\\Lambda", "Λ"),
	("\\Xi", "Ξ"),
	("\\Pi", "Π"),
	("\\Upsilon", "Υ"),
	("\\Phi", "Φ"),
	("\\Psi", "Ψ"),
	("\\Omega", "Ω"),
	("\\leq", "≤"),
	("\\ll", "≪"),
	("\\prec", "≺"),
	("\\preceq", "≼"),
	("\\subset", "⊂"),
	("\\subseteq", "⊆"),
	("\\sqsubset", "⊏"),
	("\\sqsubseteq", "⊑"),
	("\\in", "∈"),
	("\\vdash", "⊢"),
	("\\mid", "∣"),
	("\\smile", "⌣"),
	("\\geq", "≥"),
	("\\gg", "≫"),
	("\\succ", "≻"),
	("\\succeq", "≽"),
	("\\supset", "⊃"),
	("\\supseteq", "⊇"),
	("\\sqsupset", "⊐"),
	("\\sqsupseteq", "⊒"),
	("\\ni", "∋"),
	("\\dashv", "⊣"),
	("\\parallel", "∥"),
	("\\frown", "⌢"),
	("\\notin", "∉"),
	("\\equiv", "≡"),
	("\\doteq", "≐"),
	("\\sim", "∼"),
	("\\simeq", "≃"),
	("\\approx", "≈"),
	("\\cong", "≅"),
	("\\Join", "⋈"),
	("\\bowtie", "⋈"),
	("\\propto", "∝"),
	("\\models", "⊨"),
	("\\perp", "⊥"),
	("\\asymp", "≍"),
	("\\neq", "≠"),
	("\\pm", "±"),
	("\\cdot", "⋅"),
	("\\times", "×"),
	("\\cup", "∪"),
	("\\sqcup", "⊔"),
	("\\vee", "∨"),
	("\\oplus", "⊕"),
	("\\odot", "⊙"),
	("\\otimes", "⊗"),
	("\\bigtriangleup", "△"),
	("\\lhd", "⊲"),
	("\\unlhd", "⊴"),
	("\\mp", "∓"),
	("\\div", "÷"),
	("\\setminus", "∖"),
	("\\cap", "∩"),
	("\\sqcap", "⊓"),
	("\\wedge", "∧"),
	("\\ominus", "⊖"),
	("\\oslash", "⊘"),
	("\\bigcirc", "○"),
	("\\bigtriangledown", "▽"),
	("\\rhd", "⊳"),
	("\\unrhd", "⊵"),
	("\\triangleleft", "◁"),
	("\\triangleright", "▷"),
	("\\star", "⋆"),
	("\\ast", "∗"),
	("\\circ", "∘"),
	("\\bullet", "∙"),
	("\\diamond", "⋄"),
	("\\uplus", "⊎"),
	("\\dagger", "†"),
	("\\ddagger", "‡"),
	("\\wr", "≀"),
	("\\sum", "∑"),
	("\\prod", "∏"),
	("\\coprod", "∐"),
	("\\int", "∫"),
	("\\bigcup", "⋃"),
	("\\bigcap", "⋂"),
	("\\bigsqcup", "⊔"),
	("\\oint", "∮"),
	("\\bigvee", "⋁"),
	("\\bigwedge", "⋀"),
	("\\bigoplus", "⊕"),
	("\\bigotimes", "⊗"),
	("\\bigodot", "⊙"),
	("\\biguplus", "⊎"),
	("\\leftarrow", "←"),
	("\\rightarrow", "→"),
	("\\leftrightarrow", "↔"),
	("\\Leftarrow", "⇐"),
	("\\Rightarrow", "⇒"),
	("\\Leftrightarrow", "⇔"),
	("\\mapsto", "↦"),
	("\\hookleftarrow", "↩"),
	("\\leftharpoonup", "↼"),
	("\\leftharpoondown", "↽"),
	("\\hookrightarrow", "↪"),
	("\\rightharpoonup", "⇀"),
	("\\rightharpoondown", "⇁"),
	("\\longleftarrow", "←"),
	("\\longrightarrow", "→"),
	("\\longleftrightarrow", "↔"),
	("\\Longleftarrow", "⇐"),
	("\\Longrightarrow", "⇒"),
	("\\Longleftrightarrow", "⇔"),
	("\\longmapsto", "⇖"),
	("\\uparrow", "↑"),
	("\\downarrow", "↓"),
	("\\updownarrow", "↕"),
	("\\Uparrow", "⇑"),
	("\\Downarrow", "⇓"),
	("\\Updownarrow", "⇕"),
	("\\nearrow", "↗"),
	("\\searrow", "↘"),
	("\\swarrow", "↙"),
	("\\nwarrow", "↖"),
	("\\leadsto", "↝"),
	("\\dots", "…"),
	("\\cdots", "⋯"),
	("\\vdots", "⋮"),
	("\\ddots", "⋱"),
	("\\hbar", "ℏ"),
	("\\ell", "ℓ"),
	("\\Re", "ℜ"),
	("\\Im", "ℑ"),
	("\\aleph", "א"),
	("\\wp", "℘"),
	("\\forall", "∀"),
	("\\exists", "∃"),
	("\\mho", "℧"),
	("\\partial", "∂"),
	("\\prime", "′"),
	("\\emptyset", "∅"),
	("\\infty", "∞"),
	("\\nabla", "∇"),
	("\\triangle", "△"),
	("\\Box", "□"),
	("\\Diamond", "◇"),
	("\\bot", "⊥"),
	("\\top", "⊤"),
	("\\angle", "∠"),
	("\\surd", "√"),
	("\\diamondsuit", "♢"),
	("\\heartsuit", "♡"),
	("\\clubsuit", "♣"),
	("\\spadesuit", "♠"),
	("\\neg", "¬"),
	("\\flat", "♭"),
	("\\natural", "♮"),
	("\\sharp", "♯"),
	("\\digamma", "Ϝ"),
	("\\varkappa", "ϰ"),
	("\\beth", "ב"),
	("\\daleth", "ד"),
	("\\gimel", "ג"),
	("\\lessdot", "⋖"),
	("\\leqslant", "≤"),
	("\\leqq", "≦"),
	("\\lll", "⋘"),
	("\\lesssim", "≲"),
	("\\lessgtr", "≶"),
	("\\lesseqgtr", "⋚"),
	("\\preccurlyeq", "≼"),
	("\\curlyeqprec", "⋞"),
	("\\precsim", "≾"),
	("\\Subset", "⋐"),
	("\\sqsubset", "⊏"),
	("\\therefore", "∴"),
	("\\smallsmile", "⌣"),
	("\\vartriangleleft", "⊲"),
	("\\trianglelefteq", "⊴"),
	("\\gtrdot", "⋗"),
	("\\geqq", "≧"),
	("\\ggg", "⋙"),
	("\\gtrsim", "≳"),
	("\\gtrless", "≷"),
	("\\gtreqless", "⋛"),
	("\\succcurlyeq", "≽"),
	("\\curlyeqsucc", "⋟"),
	("\\succsim", "≿"),
	("\\Supset", "⋑"),
	("\\sqsupset", "⊐"),
	("\\because", "∵"),
	("\\shortparallel", "∥"),
	("\\smallfrown", "⌢"),
	("\\vartriangleright", "⊳"),
	("\\trianglerighteq", "⊵"),
	("\\doteqdot", "≑"),
	("\\risingdotseq", "≓"),
	("\\fallingdotseq", "≒"),
	("\\eqcirc", "≖"),
	("\\circeq", "≗"),
	("\\triangleq", "≜"),
	("\\bumpeq", "≏"),
	("\\Bumpeq", "≎"),
	("\\thicksim", "∼"),
	("\\thickapprox", "≈"),
	("\\approxeq", "≊"),
	("\\backsim", "∽"),
	("\\vDash", "⊨"),
	("\\Vdash", "⊩"),
	("\\Vvdash", "⊪"),
	("\\backepsilon", "∍"),
	("\\varpropto", "∝"),
	("\\between", "≬"),
	("\\pitchfork", "⋔"),
	("\\blacktriangleleft", "◀"),
	("\\blacktriangleright", "▷"),
	("\\dashleftarrow", "⇠"),
	("\\leftleftarrows", "⇇"),
	("\\leftrightarrows", "⇆"),
	("\\Lleftarrow", "⇚"),
	("\\twoheadleftarrow", "↞"),
	("\\leftarrowtail", "↢"),
	("\\leftrightharpoons", "⇋"),
	("\\Lsh", "↰"),
	("\\looparrowleft", "↫"),
	("\\curvearrowleft", "↶"),
	("\\circlearrowleft", "↺"),
	("\\dashrightarrow", "⇢"),
	("\\rightrightarrows", "⇉"),
	("\\rightleftarrows", "⇄"),
	("\\Rrightarrow", "⇛"),
	("\\twoheadrightarrow", "↠"),
	("\\rightarrowtail", "↣"),
	("\\rightleftharpoons", "⇌"),
	("\\Rsh", "↱"),
	("\\looparrowright", "↬"),
	("\\curvearrowright", "↷"),
	("\\circlearrowright", "↻"),
	("\\multimap", "⊸"),
	("\\upuparrows", "⇈"),
	("\\downdownarrows", "⇊"),
	("\\upharpoonleft", "↿"),
	("\\upharpoonright", "↾"),
	("\\downharpoonleft", "⇃"),
	("\\downharpoonright", "⇂"),
	("\\rightsquigarrow", "⇝"),
	("\\leftrightsquigarrow", "↭"),
	("\\dotplus", "∔"),
	("\\ltimes", "⋉"),
	("\\Cup", "⋓"),
	("\\veebar", "⊻"),
	("\\boxplus", "⊞"),
	("\\boxtimes", "⊠"),
	("\\leftthreetimes", "⋋"),
	("\\curlyvee", "⋎"),
	("\\centerdot", "⋅"),
	("\\rtimes", "⋈"),
	("\\Cap", "⋒"),
	("\\barwedge", "⊼"),
	("\\boxminus", "⊟"),
	("\\boxdot", "⊡"),
	("\\rightthreetimes", "⋌"),
	("\\curlywedge", "⋏"),
	("\\intercal", "⊺"),
	("\\divideontimes", "⋇"),
	("\\smallsetminus", "∖"),
	("\\circleddash", "⊝"),
	("\\circledcirc", "⊚"),
	("\\circledast", "⊛"),
	("\\hbar", "ℏ"),
	("\\hslash", "ℏ"),
	("\\square", "□"),
	("\\blacksquare", "■"),
	("\\circledS", "Ⓢ"),
	("\\vartriangle", "△"),
	("\\blacktriangle", "▲"),
	("\\complement", "∁"),
	("\\triangledown", "▽"),
	("\\blacktriangledown", "▼"),
	("\\lozenge", "◊"),
	("\\blacklozenge", "◆"),
	("\\bigstar", "★"),
	("\\angle", "∠"),
	("\\measuredangle", "∡"),
	("\\sphericalangle", "∢"),
	("\\backprime", "‵"),
	("\\nexists", "∄"),
	("\\Finv", "Ⅎ"),
	("\\varnothing", "∅"),
	("\\eth", "ð"),
	("\\mho", "℧")
]
