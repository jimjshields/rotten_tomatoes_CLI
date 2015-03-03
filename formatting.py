### Utility Functions ###

def center_text(string, term):
	"""Centers a string on a given terminal window."""

	width = term.width
	if len(string) > width:
		last_line_start = len(string) - (len(string) % width)
		last_line = string[last_line_start:]
		first_lines = string[:last_line_start]
		padding = ((width - len(last_line)) / 2) * ' '
		last_line = padding + last_line + padding

		return first_lines + '\n' + last_line

	padding =  ((width - len(string)) / 2) * ' '
	return padding + string + padding

def divider(char, term):
	"""Returns a divider the width of the given terminal."""

	width = term.width
	return char * width

def check_for_reviews(rating):
	"""Returns 'No reviews yet.' for a movie with no reviews."""
	
	return 'No reviews yet.' if rating == -1 else '{0}%'.format(rating)