import requests, os

RT_API_KEY = os.environ['RT_API_KEY']

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

		if full_endpoint:
			return '%s?&apikey=%s' % (full_endpoint, RT_API_KEY)
		else:
			return 'http://api.rottentomatoes.com/api/public/v1.0/%s%s&apikey=%s' % (endpoint_str, query, RT_API_KEY)

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

	def __init__(self, movie_id='', review_type='', page_limit='', page='', country='', search_endpoint=''):
		"""Initializes the search request with a given query."""

		if search_endpoint:
			self.endpoint = self.make_endpoint(full_endpoint=search_endpoint)
		else:
			self.endpoint = self.make_endpoint('movies/%s/reviews.json?review_type=%s&page_limit=%s&page=%s&country=%s' % (movie_id, review_type, page_limit, page, country))

class BoxOfficeRequest(APIRequest):
	"""Represents a box office request object."""

	def __init__(self, limit=16, country='us'):
		"""Initializes a box office request with a given limit and country.
		   Defaults to RT defaults."""

		self.endpoint = self.make_endpoint(endpoint_str='lists/movies/box_office.json?limit=%s&country=%s' % (limit, country))

class InTheatersRequest(APIRequest):
	"""Represents an in theaters request object."""

	def __init__(self, page_limit=16, page=1, country='us'):
		"""Initializes an 'in theaters' request with a given page limit, page, and country.
		   Defaults to RT defaults."""

		self.endpoint = self.make_endpoint(endpoint_str='lists/movies/in_theaters.json?page_limit=%s&page=%s&country=%s' % (page_limit, page, country))

class OpeningMoviesRequest(APIRequest):
	"""Represents an opening movies request object."""

	def __init__(self, limit=16, country='us'):
		"""Initializes an 'opening movies' request with a given movie limit and country.
		   Defaults to RT defaults."""

		self.endpoint = self.make_endpoint(endpoint_str='lists/movies/opening.json?limit=%s&country=%s' % (limit, country))

class UpcomingMoviesRequest(APIRequest):
	"""Represents an opening movies request object."""

	def __init__(self, page_limit=16, page=1, country='us'):
		"""Initializes an 'upcoming movies' request with a given page limit, page, and country.
		   Defaults to RT defaults."""

		self.endpoint = self.make_endpoint(endpoint_str='lists/movies/upcoming.json?page_limit=%s&page=%s&country=%s' % (page_limit, page, country))

class SimilarMoviesRequest(APIRequest):
	"""Represents a similar movies request object."""

	def __init__(self, movie_id='', limit=5, search_endpoint=''):
		"""Initializes a 'similar movies' request with a given movie id and limit.
		   Or uses an endpoint given by a movie search."""

		if search_endpoint:
			self.endpoint = self.make_endpoint(full_endpoint=search_endpoint)
		else:
			self.endpoint = self.make_endpoint(endpoint_str='movies/%s/similar.json?limit=%s' % (movie_id, limit))