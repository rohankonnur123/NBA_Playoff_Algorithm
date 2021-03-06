
from __future__ import division 
from collections import defaultdict

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
		if comp_val < standard: # need to change this condition so that the initial elimination date isn't overriden
			if alphabetical_elimination_date_array[index_order[i]] == 0:
				alphabetical_elimination_date_array[index_order[i]] = game[0]
		i+=1

def find_win_ties(alphabetical_win_list):
	D = defaultdict(list)
	for i,item in enumerate(alphabetical_win_list):
	    D[item].append(i)
	D = {k:v for k,v in D.items() if len(v)>1}
	return D

def find_seeded_index(seeded_team_name_list, team_name, seeded_index_counter):
	for names in seeded_team_name_list:
		if team_name == names:
			return seeded_index_counter
		else:
			seeded_index_counter += 1

def season_series_result(game_data, team_name_1, team_name_2, seeded_team_name_list):
	team_1_counter = 0
	team_2_counter = 0
	for game in game_data:
		if game[1] == team_name_1 and game[2] == team_name_2:
			if game[5] == 'Home':
				team_1_counter += 1
			elif game[5] == 'Away':
				team_2_counter += 1
		elif game[1] == team_name_2 and game[2] == team_name_1:
			if game[5] == 'Home':
				team_2_counter += 1
			elif game[5] == 'Away':
				team_1_counter += 1
	one_seeded_index_counter = 0
	two_seeded_index_counter = 0
	one_seeded_index_counter = find_seeded_index(seeded_team_name_list, team_name_1, one_seeded_index_counter)
	two_seeded_index_counter = find_seeded_index(seeded_team_name_list, team_name_2, two_seeded_index_counter)

	if team_1_counter > team_2_counter and one_seeded_index_counter < two_seeded_index_counter:
		return
	elif team_1_counter > team_2_counter and one_seeded_index_counter > two_seeded_index_counter:
		seeded_team_name_list[one_seeded_index_counter] = team_name_2
		seeded_team_name_list[two_seeded_index_counter] = team_name_1
	elif team_1_counter < team_2_counter and one_seeded_index_counter > two_seeded_index_counter:
		return
	elif team_1_counter < team_2_counter and one_seeded_index_counter < two_seeded_index_counter:
		seeded_team_name_list[one_seeded_index_counter] = team_name_2
		seeded_team_name_list[two_seeded_index_counter] = team_name_1
	return


def implement_tie_breakers(alphabetical_win_list, alphabetical_team_name_list, game_data, seeded_team_name_list, alphabetical_elimination_date_array, index_order):
	dict = find_win_ties(alphabetical_win_list)
	for key in dict:
		tied_team_alphabetical_index_1 = dict[key][0]
		tied_team_alphabetical_index_2 = dict[key][1]
		tied_team_name_1 = alphabetical_team_name_list[tied_team_alphabetical_index_1]
		tied_team_name_2 = alphabetical_team_name_list[tied_team_alphabetical_index_2]
		season_series_result(game_data, tied_team_name_1, tied_team_name_2, seeded_team_name_list)
		determine_index_order(seeded_team_name_list, alphabetical_team_name_list, index_order)
		counter = 0
		for name in seeded_team_name_list:
			if counter > 7:
				if alphabetical_elimination_date_array[index_order[counter - 1]] == 0:
					alphabetical_elimination_date_array[index_order[counter - 1]] = '4/12/17'
			else:
				counter+=1


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

west_alphabetical_elimination_date_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # alphabetical within each division
east_alphabetical_elimination_date_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # alphabetical within each division


def find_index(given_item_to_find, team_name_list):
    counter = 0
    for i in team_name_list:
        if given_item_to_find == i:
            return counter
        else:
            counter+=1


for game in game_data:
	# Results for each game
    winner = determine_winner(game)['winner']
    loser = determine_winner(game)['loser']
    
    # Update array for winner
    if winner in west_team_names:
        index = find_index(winner, west_team_names)
        west_wins[index] += 1
        west_games_played[index] += 1
        west_win_percentage[index] = wins_to_winpercentage(west_wins[index], west_games_played[index])
    elif winner in east_team_names:
        index = find_index(winner, east_team_names)
        east_wins[index] += 1
        east_games_played[index] += 1
        east_win_percentage[index] = wins_to_winpercentage(east_wins[index], east_games_played[index])
        
    # Update array for loser
    if loser in west_team_names:
        index = find_index(loser, west_team_names)
        west_games_played[index] += 1
        west_win_percentage[index] = wins_to_winpercentage(west_wins[index], west_games_played[index])
        west_perfect_wins[index] -= 1
    elif loser in east_team_names:
        index = find_index(loser, east_team_names)
        east_games_played[index] += 1
        east_win_percentage[index] = wins_to_winpercentage(east_wins[index], east_games_played[index])
        east_perfect_wins[index] -= 1
    
    # Update win percentage dictionary for west
    west_name_to_win_percentage_dict = {}
    west_name_to_win_percentage_dict = write_team_to_dict(west_win_percentage, west_team_names, west_name_to_win_percentage_dict)
    
    # Update win percentage dictionary for east
    east_name_to_win_percentage_dict = {}
    east_name_to_win_percentage_dict = write_team_to_dict(east_win_percentage, east_team_names, east_name_to_win_percentage_dict)
    
    # Ordered arrays that represent conference rankings
    west_seeded_team_name_list = []
    east_seeded_team_name_list = []
    
    # Ordered arrays by win percentage
    west_seeded_win_percentage_array = []
    east_seeded_win_percentage_array = []
    
    order_dict(west_name_to_win_percentage_dict, west_seeded_team_name_list, west_seeded_win_percentage_array)
    order_dict(east_name_to_win_percentage_dict, east_seeded_team_name_list, east_seeded_win_percentage_array)
    
    west_index_order = []
    east_index_order = []

    # Arrays of date each team's elimination

    # Check results
    elim_determine(west_team_names, west_seeded_team_name_list, west_index_order, west_wins, west_perfect_wins, west_alphabetical_elimination_date_array, game)
    elim_determine(east_team_names, east_seeded_team_name_list, east_index_order, east_wins, east_perfect_wins, east_alphabetical_elimination_date_array, game)

# Check for tie breakers
implement_tie_breakers(west_wins, west_team_names, game_data, west_seeded_team_name_list, west_alphabetical_elimination_date_array, west_index_order)
implement_tie_breakers(east_wins, east_team_names, game_data, east_seeded_team_name_list, east_alphabetical_elimination_date_array, east_index_order)

# Format output
team = 0
while team < len(west_alphabetical_elimination_date_array):
	if west_alphabetical_elimination_date_array[team] == 0:
		west_alphabetical_elimination_date_array[team] = 'playoffs'
	if east_alphabetical_elimination_date_array[team] == 0:
		east_alphabetical_elimination_date_array[team] = 'playoffs'
	team += 1

# Format new team output list
league_alphabetical_array = []
csv_to_array('Analytics_Attachment/Sample_NBA_Clinch_Dates-Table 1.csv', league_alphabetical_array)
league_alphabetical_array = league_alphabetical_array[1:]

league_alphabetical_teams = [team[0] for team in league_alphabetical_array]

# Create full league lists
list_to_write = []
for elem in league_alphabetical_teams:
	if elem in east_team_names:
		index_for_name = east_team_names.index(elem)
		list_to_write.append([elem, east_alphabetical_elimination_date_array[index_for_name]])
	elif elem in west_team_names:
		index_for_name = west_team_names.index(elem)
		list_to_write.append([elem, west_alphabetical_elimination_date_array[index_for_name]])

# File we want to write output to
output_csv = 'elimination_dates.csv'

# Write to output file
with open(output_csv, 'wb') as file:
	file.write('Team')
	file.write(', ')
	file.write('Date Eliminated')
	file.write('\n')
	for line in list_to_write:
	    file.write(line[0])
	    file.write(', ')
	    file.write(line[1])
	    file.write('\n')



