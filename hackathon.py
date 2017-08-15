import csv

win_dict = {}
ordered_seeding_array = []


def wins_to_winpercentage(wins, games_played):
	win_percentage = wins/games_played
	return win_percentage

def winpercentage_to_wins(win_percentage, games_played):
	wins = win_percentage * games_played
	return wins
	

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


def csv_to_array(csv_file_name):
	results = []
	with open(csv_file_name) as csvfile:
		reader = csv.reader(csvfile) # change contents to floats
		for row in reader: # each row is a list
			results.append(row)
	return results

print(csv_to_array('Analytics_Attachment/2016_17_NBA_Scores-Table 1.csv')[1][0])

