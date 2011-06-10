import gtk
import glib
import convert

window = gtk.Window()
window.set_title("Latex to Unicode converter")
table = gtk.Table(rows=3, columns=2)
window.add(table)
table.attach(gtk.Label("Latex:"), 0, 1, 0, 1, 0, 0, xpadding=5, ypadding=5)
latex_input = gtk.Entry()
latex_input.set_width_chars(50)
table.attach(latex_input, 1, 2, 0, 1, xpadding=5, ypadding=5)
table.attach(gtk.Label("Preview:"), 0, 1, 1, 2, 0, 0, xpadding=5, ypadding=5)
preview_input = gtk.Entry()
preview_input.set_sensitive(False)
preview_input.set_width_chars(50)
table.attach(preview_input, 1, 2, 1, 2, xpadding=5, ypadding=5)
hbox = gtk.HBox(True, 5)
paste_button = gtk.Button("Paste")
hbox.add(paste_button)
cancel_button = gtk.Button("Cancel")
hbox.add(cancel_button)
table.attach(hbox, 0, 2, 2, 3, 0, 0, xpadding=5 , ypadding=5)
window.set_position(gtk.WIN_POS_CENTER)
window.show_all()

def paste(*arguments):
	print(preview_input.get_text())
	window.hide()

window.connect("hide", lambda *x: gtk.main_quit())
def input_changed(widget, event):
	if len(event.string) == 1:
		if ord(event.string) == 13:
			paste()
		elif ord(event.string) == 27:
			window.hide()
		else:
			preview_input.set_text(convert.convert(widget.get_text()))
	else:
		preview_input.set_text(convert.convert(widget.get_text()))

latex_input.connect("key-release-event", input_changed)
cancel_button.connect("clicked", lambda *x: gtk.main_quit())
paste_button.connect("clicked", paste)

gtk.main()
