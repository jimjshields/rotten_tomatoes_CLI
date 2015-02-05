# import requests, json
import sys
from blessings import Terminal
from classes import *
from formatting import center_text, divider

term = Terminal()

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
reviews_results = ReviewsRequest(search_endpoint=sorted_by_year[selected_movie][2]).make_request()
reviews_dict = [k for k in reviews_results['reviews']]

print divider('-', term)
for review in reviews_dict:
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