### Utility Functions ###

def center_text(string, term):
	"""Centers a string on a given terminal window."""

	width = term.width
	if len(string) > width:
		first_line = string[:width]
		second_line = string[width:]
		padding = ((width - len(second_line)) / 2) * ' '
		second_line = padding + second_line + padding

		return first_line + '\n' + second_line

	padding =  ((width - len(string)) / 2) * ' '
	return padding + string + padding

def divider(char, term):
	"""Returns a divider the width of the given terminal."""

	width = term.width
	return char * width