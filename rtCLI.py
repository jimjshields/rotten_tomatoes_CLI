import requests, json
import sys
from blessings import Terminal

term = Terminal()

def center_text(string):
	"""Centers a string on a given terminal window."""

	width = term.width
	padding =  ((width - len(string)) / 2) * ' '
	return padding + string + padding

def divider(char):
	"""Returns a divider the width of the given terminal."""

	width = term.width
	return char * width

searching = True
while searching:
	search_query = raw_input("What do you want to search for? ")
	search_query.replace(' ', '+')
	search_results = requests.get('http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=zyduzhcjdgzkzc3dmas2uph6&q=%s' % (search_query)).json()

	movies = [(i['title'], i['ratings']['critics_score'], i['links']['reviews'], i['year']) for i in search_results['movies']]
	sorted_by_rating = sorted(movies, key=lambda tup: tup[1], reverse=True)
	for i, movie in enumerate(sorted_by_rating):
		print '%s. %s: %s (%s)' % (i + 1, movie[0], movie[1], movie[3])

	search_choice = int(raw_input('Do you want to keep searching (1) or more info (2)? '))
	if search_choice == 2:
		searching = False

selected_movie = int(raw_input("Which movie do you want more info on? ")) - 1
reviews_results = requests.get('%s?apikey=zyduzhcjdgzkzc3dmas2uph6' % (sorted_by_rating[selected_movie][2])).json()
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