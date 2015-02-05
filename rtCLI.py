import requests, json
import sys
from blessings import Terminal

term = Terminal()

def center_text(string):
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

def divider(char):
	"""Returns a divider the width of the given terminal."""

	width = term.width
	return char * width

class APIRequest(object):
	"""Represents a request to the Rotten Tomatoes API."""

	def __init__(self):
		"""Initializes the request with an empty endpoint to be filled in by
		   specific request types."""
		
		self.endpoint = ''

	def make_request(self):
		"""Makes a request to a given endpoint and returns a parsed JSON."""

		results = requests.get(self.endpoint).json()
		return results

class SearchRequest(APIRequest):
	"""Represents a search request."""

	def __init__(self, query):
		"""Initializes the search request with a given query."""

		self.query = query.replace(' ', '+')
		self.endpoint = 'http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=zyduzhcjdgzkzc3dmas2uph6&q=%s'\
						% (self.query)

searching = True
while searching:
	search_query = raw_input("What do you want to search for? ")
	s = SearchRequest(search_query)
	search_results = s.make_request()

	movies = [(i['title'], i['ratings']['critics_score'], i['links']['reviews'], i['year']) for i in search_results['movies'] if i['ratings']['critics_score'] != -1]
	sorted_by_rating = sorted(movies, key=lambda tup: tup[1], reverse=True)
	sorted_by_year = sorted(movies, key=lambda tup: tup[3], reverse=True)
	for i, movie in enumerate(sorted_by_year):
		if movie[1] != -1:
			if movie[1] < 60:
				print term.red('%s. %s: %s (%s)' % (i + 1, movie[0], movie[1], movie[3]))
			else:
				print term.green('%s. %s: %s (%s)' % (i + 1, movie[0], movie[1], movie[3]))


	search_choice = int(raw_input('Do you want to keep searching (1) or more info (2)? '))
	if search_choice == 2:
		searching = False

selected_movie = int(raw_input("Which movie do you want more info on? ")) - 1
reviews_results = requests.get('%s?apikey=zyduzhcjdgzkzc3dmas2uph6' % (sorted_by_year[selected_movie][2])).json()
reviews_dict = [k for k in reviews_results['reviews']]

print divider('-')
for review in reviews_dict:
	review_text = center_text(review['date']) + '\n'
	review_text += center_text(review['critic'] + ' - ' + review['publication']) + '\n'
	review_text += center_text(review['quote']) + '\n'
	if review['links']:
		review_text += center_text(review['links']['review'])

	if review['freshness'] == 'fresh':
		print term.green(review_text)
	else:
		print term.red(review_text)

	print divider('-')