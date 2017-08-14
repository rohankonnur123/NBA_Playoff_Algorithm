
win_dict = {}
ordered_seeding_array = []

# Take in a list of win percentages, a list of team names, and an empty global dictionary.
# Return a global dictionary of team name keys and win percentage values.
def write_team_to_dict(win_percentage, team_name, dictionary):
	i=0
	while i < len(team_name):
		win_dict[team_name[i]] = win_percentage[i]
		i += 1


# Take in the dictionary outputted by write_team_to_dict()
# Return an ordered tuple of team names by win percentage from greatest to least.
def order_dict(win_dict, ordered_seeding_array):
	for key, value in sorted(win_dict.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    	result.append(key)
    	

# Take in all team arrays with information about wins and perfect win expectancy, and the ordered tuple of team names returned by order_dict()
# Return nothing. write the eliminated team name with the date to csv via the function write_to_csv().
def elim_determine(team_arrays, ordered_list):
	standard = ordered_list[8].wins
	i = 9
	while i < len(team_name):
		comp_val = ordered_list[i].expected_wins
		if comp_val < standard:
			write_to_csv(team_name[i])


def write_to_csv(team_name, current_iterative_date):
	return

