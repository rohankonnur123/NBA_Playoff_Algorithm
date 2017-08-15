
import csv
import math

game_data = []

win_dict = {}
ordered_seeding_array = []

def csv_to_array(csv_file_name, write_array):
	'''
	:param csv_file_name Name of the csv file being used
	Returns {Array} 2D array of tabular data from the csv file
	'''
	with open(csv_file_name) as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			write_array.append(row)
	return

def format_array_with_data(csv_file_name, write_array):
	csv_to_array(csv_file_name, write_array)
	write_array = write_array[1:]
	return write_array

def wins_to_winpercentage(wins, games_played):
	'''
	:param wins Number of wins the team currently has
	:param games_played Number of games the team has played
	Returns {Float} the team's win percentage
	'''
	win_percentage = wins/games_played
	return win_percentage

def winpercentage_to_wins(win_percentage, games_played):
	'''
	:param win_percentage Team's current win percentage
	:param games_played Number of games the team has played
	Returns {Integer} the number of wins the team currently has
	'''
	wins = win_percentage * games_played
	return wins

# Take in a list of win percentages, a list of team names, and an empty global dictionary.
# Return a global dictionary of team name keys and win percentage values.
def write_team_to_dict(alphabetical_win_percentage_list, alphabetical_team_name_list, name_to_win_percentage_dict):
	i=0
	while i < len(alphabetical_team_name_list):
		name_to_win_percentage_dict[alphabetical_team_name_list[i]] = alphabetical_win_percentage_list[i]
		i += 1
	return name_to_win_percentage_dict

# Take in the dictionary outputted by write_team_to_dict(), an array to write the ordered seeds to, and an array to write corresponding win % to
# Return the two arrays of team names and win % in order from most wins to least
def order_dict(name_to_win_percentage_dict, seeded_team_name_list, seeded_win_percentage_array):
	for key, value in sorted(name_to_win_percentage_dict.iteritems(), key=lambda (k,v): (v,k), reverse=True):
	    seeded_team_name_list.append(key)
	    seeded_win_percentage_array.append(value)

index_order = []
def determine_index_order(seeded_team_name_list, alphabetical_team_name_list, index_conversion_array):
	for correct_index_team in seeded_team_name_list:
		counter = 0
		for wrong_index_team in alphabetical_team_name_list:
			if correct_index_team == wrong_index_team:
				index_conversion_array.append(counter)
			else:
				counter += 1
	print(index_conversion_array)
	return index_conversion_array
	
# Take in all team arrays with information about wins and perfect win expectancy, and the ordered tuple of team names returned by order_dict()
# Return nothing. write the eliminated team name with the date to csv via the function write_to_csv().
def elim_determine(alphabetical_team_name_list, seeded_team_name_list, index_order, alphabetical_win_list, alphabetical_expected_wins_list):
	determine_index_order(seeded_team_name_list, alphabetical_team_name_list, index_order)
	last_seed_team = seeded_team_name_list[7]
	standard = alphabetical_win_list[index_order[7]] 
	i = 8
	while i < len(seeded_team_name_list):
		comp_val = alphabetical_expected_wins_list[index_order[i]]
		if comp_val < standard:
			print(seeded_team_name_list[i] + " is eliminate!")
		else:
			print(seeded_team_name_list[i] + " is still in the running!")
		i+=1

def write_to_csv(alphabetical_team_name_list, current_iterative_date):
	return

def determine_winner(game):
	'''
	:param game: List containing specs about the game (teams, winner, loser, scores, etc.)
	Returns a dictionary of the winning team and losing team {'winner': winning_team, 'loser': losing_team}
	'''
	home_team = game[1]
	away_team = game[2]

	if game[-1] == 'Away':
		return {'winner': away_team, 'loser': home_team}
	return {'winner': home_team, 'loser': away_team}

def date_to_number(date):
	'''
	:param date: String formatted MM/DD/YYYY (could be only one digit for month or day)
	Returns {Integer} that represents the day of the season, assuming the first game was played on day 0
	'''
	day_of_season = 0
	number_to_month = {'11': 'november', '12': 'december', '1': 'january', '2': 'february', '3': 'march', '4': 'april'}
	nba_days_in_month = {'november': 30, 'december': 31, 'january': 31, 'february': 27, 'march': 31, 'april': 12}

	month = int(date.split('/')[0])
	day = int(date.split('/')[1])
	year = int(date.split('/')[2])

	if year == 16:
		if month == 10:
			return day - 25
		else:
			if month == 11:
				return day + 6
			else:
				return day + nba_days_in_month['november'] + 6
	else:
		i = 1
		full_month_days = 6 + nba_days_in_month['november'] + nba_days_in_month['december']
		additional_days = 0
		while i <= month:
			if i == month:
				additional_days += day
			else:
				i_name = number_to_month[str(i)]
				i_days = nba_days_in_month[i_name]
				full_month_days += i_days
			i += 1
		return full_month_days + additional_days


# Set the global array with all the game data
# Abstract away the csv file and just reference the array now
csv_to_array('Analytics_Attachment/2016_17_NBA_Scores-Table 1.csv', game_data)

# remove labels
game_data = game_data[1:]