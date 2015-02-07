# import requests, json
import sys
from blessings import Terminal
from classes import SearchRequest, ReviewsRequest, BoxOfficeRequest, InTheatersRequest
from formatting import center_text, divider

term = Terminal()

menu_items = ['Search for a Movie', 'Box Office', 'In Theaters', 'Opening', 'Upcoming', 'Exit']

def movie_search():
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

def get_box_office():
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

def get_in_theaters():
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




menu_functions = {
	1: movie_search,
	2: get_box_office,
	3: get_in_theaters,
	# 4: get_opening,
	# 5: get_upcoming
}

exit = False

while not exit:
	print '\n'.join(['%s. %s' % (i + 1, x) for i, x in enumerate(menu_items)])
	user_choice = int(raw_input('Enter the number for what you want to do: '))
	
	if user_choice == 6:
		exit = True
	else:
		menu_functions[user_choice]()
		print divider('-', term)


# searching = True
# while searching:
	# search_query = raw_input("What do you want to search for? ")
	# s = SearchRequest(search_query)
	# search_results = s.make_request()

	# movies = [(i['title'], i['ratings']['critics_score'], i['links']['reviews'], i['year']) for i in search_results['movies'] if i['ratings']['critics_score'] != -1]
	# sorted_by_rating = sorted(movies, key=lambda tup: tup[1], reverse=True)
	# sorted_by_year = sorted(movies, key=lambda tup: tup[3], reverse=True)
	# for i, movie in enumerate(sorted_by_year):
	# 	if movie[1] != -1:
	# 		if movie[1] < 60:
	# 			print term.red('%s. %s: %s (%s)' % (i + 1, movie[0], movie[1], movie[3]))
	# 		else:
	# 			print term.green('%s. %s: %s (%s)' % (i + 1, movie[0], movie[1], movie[3]))


# 	search_choice = int(raw_input('Do you want to keep searching (1) or more info (2)? '))
# 	if search_choice == 2:
# 		searching = False

# selected_movie = int(raw_input("Which movie do you want more info on? ")) - 1
# reviews_results = ReviewsRequest(search_endpoint=sorted_by_year[selected_movie][2]).make_request()
# reviews_dict = [k for k in reviews_results['reviews']]

# print divider('-', term)
# for review in reviews_dict:
# 	review_text = center_text(review['date'], term) + '\n'
# 	review_text += center_text(review['critic'] + ' - ' + review['publication'], term) + '\n'
# 	review_text += center_text(review['quote'], term) + '\n'
# 	if review['links']:
# 		review_text += center_text(review['links']['review'], term)

# 	if review['freshness'] == 'fresh':
# 		print term.green(review_text)
# 	else:
# 		print term.red(review_text)

# 	print divider('-', term)