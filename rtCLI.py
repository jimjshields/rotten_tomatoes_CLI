import requests, json
import sys
from blessings import Terminal

term = Terminal()

# TODO: Move these to their own file.
### Utility Functions ###

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

### Request Classes ###

class APIRequest(object):
	"""Represents a request to the Rotten Tomatoes API."""

	def __init__(self):
		"""Initializes the request with an empty endpoint to be filled in by
		   specific request types."""

		self.endpoint = ''

	def make_endpoint(self, endpoint_str='', query='', full_endpoint=''):
		"""Constructs an endpoint with the consistent api path and
		   the given endpoint and api key appended.
		   If given a query (e.g., a search), can insert that as well.
		   If given the full endpoint (e.g., when getting a set of reviews
		   for a movie directly from the API), you can pass the full endpoint."""
		
		api_key = 'zyduzhcjdgzkzc3dmas2uph6'

		if full_endpoint:
			return '%s?&apikey=%s' % (full_endpoint, api_key)
		else:
			return 'http://api.rottentomatoes.com/api/public/v1.0/%s%s&apikey=%s' % (endpoint_str, query, api_key)

	def make_request(self):
		"""Makes a request to a given endpoint and returns a parsed JSON."""

		results = requests.get(self.endpoint).json()
		return results

class SearchRequest(APIRequest):
	"""Represents a search request object."""

	def __init__(self, query):
		"""Initializes the search request with a given query."""

		self.query = query.replace(' ', '+')
		self.endpoint = self.make_endpoint(endpoint_str='movies.json?', query='q=' + self.query)

class ReviewsRequest(APIRequest):
	"""Represents a reviews request object."""

	def __init__(self, reviews_endpoint):
		"""Initializes the search request with a given query."""

		self.endpoint = self.make_endpoint(full_endpoint=reviews_endpoint)

class BoxOfficeRequest(APIRequest):
	"""Represents a box office request object."""

	def __init__(self, limit=16, country='us'):
		"""Initializes a box office request with a given limit and country.
		   Defaults to 16 and the US."""

		self.endpoint = self.make_endpoint(endpoint_str='lists/movies/box_office.json?limit=%s&country=%s' % (limit, country))

# searching = True
# while searching:
# 	search_query = raw_input("What do you want to search for? ")
# 	s = SearchRequest(search_query)
# 	search_results = s.make_request()

# 	movies = [(i['title'], i['ratings']['critics_score'], i['links']['reviews'], i['year']) for i in search_results['movies'] if i['ratings']['critics_score'] != -1]
# 	sorted_by_rating = sorted(movies, key=lambda tup: tup[1], reverse=True)
# 	sorted_by_year = sorted(movies, key=lambda tup: tup[3], reverse=True)
# 	for i, movie in enumerate(sorted_by_year):
# 		if movie[1] != -1:
# 			if movie[1] < 60:
# 				print term.red('%s. %s: %s (%s)' % (i + 1, movie[0], movie[1], movie[3]))
# 			else:
# 				print term.green('%s. %s: %s (%s)' % (i + 1, movie[0], movie[1], movie[3]))


# 	search_choice = int(raw_input('Do you want to keep searching (1) or more info (2)? '))
# 	if search_choice == 2:
# 		searching = False

# selected_movie = int(raw_input("Which movie do you want more info on? ")) - 1
# reviews_results = ReviewsRequest(sorted_by_year[selected_movie][2]).make_request()
# reviews_dict = [k for k in reviews_results['reviews']]

# print divider('-')
# for review in reviews_dict:
# 	review_text = center_text(review['date']) + '\n'
# 	review_text += center_text(review['critic'] + ' - ' + review['publication']) + '\n'
# 	review_text += center_text(review['quote']) + '\n'
# 	if review['links']:
# 		review_text += center_text(review['links']['review'])

# 	if review['freshness'] == 'fresh':
# 		print term.green(review_text)
# 	else:
# 		print term.red(review_text)

# 	print divider('-')