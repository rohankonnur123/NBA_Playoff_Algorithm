
win_percent = {}
ordered_seeding_array = []

# Take in a list of win percentages, a list of team names, and an empty global dictionary.
# Return a global dictionary of team name keys and win percentage values.
def write_team_to_dict(win_percentage, team_name, dictionary):
	for i in team_name:
		win_percent[team_name] = win_percentage
	return win_percent

# Take in the dictionary outputted by write_team_to_dict()
# Return an ordered tuple of team names by win percentage from greatest to least.
def order_dict(win_percent_dict, ordered_seeding_array):
	for key, value in sorted(ordered_seeding_array.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    	result.append(key)
    return result

# Take in all team arrays with information about wins and perfect win expectancy, and the ordered tuple of team names returned by order_dict()
# Return nothing. write the eliminated team name with the date to csv via the function write_to_csv().
def elim_determine(team_arrays, ordered_list):
	standard = ordered_list[8].wins
	i = 9
	while i < team_name.length:
		comp_val = ordered_list[i].expected_wins
		if comp_val < standard:
			write_to_csv(team_name[i])


def write_to_csv(team_name, current_iterative_date):
	return


