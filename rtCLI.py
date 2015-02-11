from blessings import Terminal
from formatting import center_text, divider
from menu_actions import MenuAction, term

MENU_ACTION_NAMES = {
	1: ('Search for a Movie', MenuAction().movie_search),
	2: ('Box Office', MenuAction().get_box_office),
	3: ('In Theaters', MenuAction().get_in_theaters),
	4: ('Opening', MenuAction().get_opening),
	5: ('Upcoming', MenuAction().get_upcoming),
	6: ('Exit',)
}

exit = False

while not exit:
	print '\n'.join(['%s. %s' % (i + 1, x[0]) for i, x in enumerate(MENU_ACTION_NAMES.values())])
	user_choice = int(raw_input('Enter the number for what you want to do: '))
	
	if user_choice == 6:
		exit = True
	else:
		action = MENU_ACTION_NAMES[user_choice][1]()
		print divider('-', term)