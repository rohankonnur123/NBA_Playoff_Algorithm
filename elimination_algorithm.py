import csv

game_data = []

win_dict = {}
ordered_seeding_array = []

def csv_to_array(csv_file_name):
	with open(csv_file_name) as csvfile:
		reader = csv.reader(csvfile) # change contents to floats
		for row in reader: # each row is a list
			game_data.append(row)
	return

# Set the global array of game_data so that we can access and manipulate
csv_to_array('Analytics_Attachment/2016_17_NBA_Scores-Table 1.csv')
game_data = game_data[1:]

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

def determine_winner(game):
	'''
	:param game: List containing data about the game (teams, winner, loser, scores, etc.)

	Returns a dictionary of the winning team and losing team {'winner': winning_team, 'loser': losing_team}
	'''
	home_team = game[1]
	away_team = game[2]

	if game[-1] == 'Away':
		return {'winner': away_team, 'loser': home_team}
	return {'winner': home_team, 'loser': away_team}
