from blessings import Terminal
from classes import SearchRequest, ReviewsRequest, BoxOfficeRequest, InTheatersRequest, OpeningMoviesRequest, UpcomingMoviesRequest
from formatting import center_text, divider

term = Terminal()

class MenuAction(object):

	def __init__(self):
		"""Initializes a menu action object that can be acted upon."""

	def movie_search(self):
		"""Searches for a movie."""

		searching = True

		while searching:
			search_query = raw_input("What do you want to search for? ")
			search_results = SearchRequest(search_query).make_request()

			print divider('-', term)
			print term.blue_bold('Search Results (By Relevance):')

			movies = [i for i in search_results['movies'] if i['ratings']['critics_score'] != -1]
			# sorted_by_year = sorted(movies, key=lambda dic: dic['year'], reverse=True)

			for i, movie in enumerate(movies):
				if movie['ratings']['critics_score'] < 60:
					print term.red('%s. %s: %s%% (%s)' % (i + 1, movie['title'], movie['ratings']['critics_score'], movie['year']))
				else:
					print term.green('%s. %s: %s%% (%s)' % (i + 1, movie['title'], movie['ratings']['critics_score'], movie['year']))

			search_choice = int(raw_input('Do you want to keep searching (1), get more info on a movie (2), or go to the main menu (3)? '))
			
			if search_choice == 2:
				searching = False
				selected_movie = int(raw_input("Which movie do you want more info on? ")) - 1

				reviews_results = ReviewsRequest(movie_id=movies[selected_movie]['id'], page_limit=50).make_request()

				print divider('-', term)
				for review in reviews_results['reviews']:
					review_text = center_text(review['date'], term) + '\n'
					review_text += center_text(review['critic'] + ' - ' + review['publication'], term) + '\n'
					review_text += center_text(review['quote'], term) + '\n'
					if review['links']:
						review_text += center_text(review['links']['review'], term)

					if review['freshness'] == 'fresh':
						print term.green(review_text)
					else:
						print term.red(review_text)

					print divider('-', term)

			if search_choice == 3:
				searching = False

	def get_box_office(self):
		"""Returns the box office data in a nice format."""

		box_office_data = BoxOfficeRequest(limit=20).make_request()
		print divider('-', term)
		for movie in box_office_data['movies']:
			movie_text = center_text('%s - %s%% - %s - %s minutes' % (movie['title'], movie['ratings']['critics_score'], movie['mpaa_rating'], movie['runtime']), term) + '\n'
			movie_text += center_text(', '.join([i['name'] for i in movie['abridged_cast']]), term) + '\n'
			movie_text += center_text('Synopsis', term)
			movie_text += center_text(movie['synopsis'], term)
			
			if movie['ratings']['critics_score'] >= 60:
				print term.green(movie_text)
			else:
				print term.red(movie_text)
			print divider('-', term)

	def get_in_theaters(self):
		"""Returns the in theaters data in a nice format."""

		in_theaters_data = InTheatersRequest(page_limit=20).make_request()
		print divider('-', term)
		for movie in in_theaters_data['movies']:
			movie_text = center_text('%s - %s%% - %s - %s minutes' % (movie['title'], movie['ratings']['critics_score'], movie['mpaa_rating'], movie['runtime']), term) + '\n'
			movie_text += center_text(', '.join([i['name'] for i in movie['abridged_cast']]), term) + '\n'
			movie_text += center_text('Synopsis', term)
			movie_text += center_text(movie['synopsis'], term)
			
			if movie['ratings']['critics_score'] >= 60:
				print term.green(movie_text)
			else:
				print term.red(movie_text)
			print divider('-', term)

	def get_opening(self):
		"""Returns the opening movies data in a nice format."""

		opening_data = OpeningMoviesRequest(limit=20).make_request()
		print divider('-', term)
		for movie in opening_data['movies']:
			movie_text = center_text('%s - %s%% - %s - %s minutes' % (movie['title'], movie['ratings']['critics_score'], movie['mpaa_rating'], movie['runtime']), term) + '\n'
			movie_text += center_text(', '.join([i['name'] for i in movie['abridged_cast']]), term) + '\n'
			movie_text += center_text('Synopsis', term)
			movie_text += center_text(movie['synopsis'], term)

			if movie['ratings']['critics_score'] >= 60:
				print term.green(movie_text)
			else:
				print term.red(movie_text)
			print divider('-', term)

	def get_upcoming(self):
		"""Returns the upcoming movies data in a nice format."""

		upcoming_data = UpcomingMoviesRequest(page_limit=20).make_request()
		print divider('-', term)
		for movie in upcoming_data['movies']:
			movie_text = center_text('%s - %s%% - %s - %s minutes' % (movie['title'], movie['ratings']['critics_score'], movie['mpaa_rating'], movie['runtime']), term) + '\n'
			movie_text += center_text(', '.join([i['name'] for i in movie['abridged_cast']]), term) + '\n'
			movie_text += center_text('Synopsis', term)
			movie_text += center_text(movie['synopsis'], term)

			if movie['ratings']['critics_score'] >= 60:
				print term.green(movie_text)
			else:
				print term.red(movie_text)
			print divider('-', term)