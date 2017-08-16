
from __future__ import division 

import csv
import math
import numpy as np

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
	if games_played == 0:
		return 1.000
	else:
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

def determine_index_order(seeded_team_name_list, alphabetical_team_name_list, index_conversion_array):
	for correct_index_team in seeded_team_name_list:
		counter = 0
		for wrong_index_team in alphabetical_team_name_list:
			if correct_index_team == wrong_index_team:
				index_conversion_array.append(counter)
			else:
				counter += 1
	return index_conversion_array
	
# Take in all team arrays with information about wins and perfect win expectancy, and the ordered tuple of team names returned by order_dict()
# Return nothing. write the eliminated team name with the date to csv via the function write_to_csv().
def elim_determine(alphabetical_team_name_list, seeded_team_name_list, index_order, alphabetical_win_list, alphabetical_expected_wins_list, 
					alphabetical_elimination_date_array, game):
	determine_index_order(seeded_team_name_list, alphabetical_team_name_list, index_order)
	last_seed_team = seeded_team_name_list[7]
	standard = alphabetical_win_list[index_order[7]] 
	i = 8
	while i < len(seeded_team_name_list):
		comp_val = alphabetical_expected_wins_list[index_order[i]]
		if comp_val < standard:
			if alphabetical_elimination_date_array[index_order[i]] is np.string_:
				print(seeded_team_name_list[i] + " is eliminated on " + alphabetical_elimination_date_array[index_order[i]])
			else:
				alphabetical_elimination_date_array[index_order[i]] = game[0]
				print(seeded_team_name_list[i] + " is eliminated on " + game[0])
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

def number_to_date(number):
	'''
	:param number: Integer representing the day of the season a game is being played on, assuming first day is day 0

	Returns {String} date in format MM/DD/YYYY (month or day can be 1 digit)
	'''
	nba_days_in_month = {'october': 6, 'november': 30, 'december': 31, 'january': 31, 'february': 27, 'march': 31, 'april': 12}
	index_to_month = {'0': 'october', '1': 'november', '2': 'december', '3': 'january', '4': 'february', '5': 'march', '6': 'april'}
	month_name_to_number = {'october': 10, 'november': 11, 'december': 12, 'january': 1, 'february': 2, 'march': 3, 'april': 4}
	
	# Create a list of upper bound numbers for each month
	maxes = []
	i = 0
	while i < len(nba_days_in_month):
		if i == 0:
			maxes.append(nba_days_in_month[index_to_month[str(0)]])
		else:
			track = 0
			for num in range(i+1):
				track += nba_days_in_month[index_to_month[str(num)]]
			maxes.append(track)
		i += 1
	
	# Use the maxes bounds to find month and day for the number
	m = 0
	day = None
	year = None

	if number < 7:
		day = 25 + number
		month = 'october'
		year = 2016
	else:
		elem = 0
		while elem < len(maxes):
			if number > maxes[elem]:
				m += 1
			else:
				day = number - maxes[elem - 1]
				break
			elem += 1
		month = index_to_month[str(m)]

	# Convert all types to build the date string
	month_number = month_name_to_number[month]
	if month_number <= 10:
		year = 2016
	else:
		year = 2017

	return str(month_number) + '/' + str(day) + '/' + str(year)

#execute

game_data = []
team_data = []

east_team_names = []
west_team_names = []

format_array_with_data('Analytics_Attachment/2016_17_NBA_Scores-Table 1.csv', game_data)

format_array_with_data('Analytics_Attachment/Division_Info-Table 1.csv', team_data)

# Reading team names into arrays by conference
for array in team_data:
    if array[2] == 'East':
        east_team_names.append(array[0])
    elif array[2] == "West":
        west_team_names.append(array[0])

east_wins = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
east_perfect_wins = [82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82]
east_games_played = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
east_win_percentage = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

west_wins = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
west_perfect_wins = [82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82]
west_games_played = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
west_win_percentage = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def find_index(given_item_to_find, team_name_list):
    counter = 0
    for i in team_name_list:
        if given_item_to_find == i:
            return counter
        else:
            counter+=1

for game in game_data:
    winner = determine_winner(game)['winner']
    loser = determine_winner(game)['loser']
    
    if winner in west_team_names:
        index = find_index(winner, west_team_names)
        west_wins[index] += 1
        west_games_played[index] += 1
        west_win_percentage[index] = wins_to_winpercentage(west_wins[index], west_games_played[index])
        # print(west_wins[index])
        # print(west_games_played[index])
        # if west_games_played[index] == 0:
        # 	print(1)
        # else:
        # 	print(west_wins[index] / west_games_played[index])
        # print(wins_to_winpercentage(west_wins[index], west_games_played[index]))
    elif winner in east_team_names:
        index = find_index(winner, east_team_names)
        east_wins[index] += 1
        east_games_played[index] += 1
        east_win_percentage[index] = wins_to_winpercentage(east_wins[index], east_games_played[index])
        # print(east_wins[index])
        # print(east_games_played[index])
        # if east_games_played[index] == 0:
        # 	print(1)
        # else:
        # 	print(east_wins[index] / east_games_played[index])
        # print(wins_to_winpercentage(east_wins[index], east_games_played[index]))
        
    if loser in west_team_names:
        index = find_index(loser, west_team_names)
        west_games_played[index] += 1
        west_win_percentage[index] = wins_to_winpercentage(west_wins[index], west_games_played[index])
        # print(west_wins[index])
        # print(west_games_played[index])
        # if west_games_played[index] == 0:
        # 	print(1)
        # else:
        # 	print(west_wins[index] / west_games_played[index])
        # print(wins_to_winpercentage(west_wins[index], west_games_played[index]))
        west_perfect_wins[index] -= 1
    elif loser in east_team_names:
        index = find_index(loser, east_team_names)
        east_games_played[index] += 1
        east_win_percentage[index] = wins_to_winpercentage(east_wins[index], east_games_played[index])
        # print(east_wins[index])
        # print(east_games_played[index])
        # if east_games_played[index] == 0:
        # 	print(1)
        # else:
        # 	print(east_wins[index] / east_games_played[index])
        # print(wins_to_winpercentage(east_wins[index], east_games_played[index]))
        east_perfect_wins[index] -= 1
    
    west_name_to_win_percentage_dict = {}
    west_name_to_win_percentage_dict = write_team_to_dict(west_win_percentage, west_team_names, west_name_to_win_percentage_dict)
    
    east_name_to_win_percentage_dict = {}
    east_name_to_win_percentage_dict = write_team_to_dict(east_win_percentage, east_team_names, east_name_to_win_percentage_dict)
    
    west_seeded_team_name_list = []
    east_seeded_team_name_list = []
    
    west_seeded_win_percentage_array = []
    east_seeded_win_percentage_array = []
    
    order_dict(west_name_to_win_percentage_dict, west_seeded_team_name_list, west_seeded_win_percentage_array)
    order_dict(east_name_to_win_percentage_dict, east_seeded_team_name_list, east_seeded_win_percentage_array)
    print(west_seeded_team_name_list)
    print(east_seeded_team_name_list)
    
    west_index_order = []
    east_index_order = []

    west_alphabetical_elimination_date_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    east_alphabetical_elimination_date_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    elim_determine(west_team_names, west_seeded_team_name_list, west_index_order, west_wins, west_perfect_wins, west_alphabetical_elimination_date_array, game)
    elim_determine(east_team_names, east_seeded_team_name_list, east_index_order, east_wins, east_perfect_wins, east_alphabetical_elimination_date_array, game)
    print(west_alphabetical_elimination_date_array)
    print(east_alphabetical_elimination_date_array)

