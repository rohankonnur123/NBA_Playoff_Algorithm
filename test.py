
from collections import defaultdict
D = defaultdict(list)
mylist = [20, 30, 25, 20]
for i,item in enumerate(mylist):
    D[item].append(i)
D = {k:v for k,v in D.items() if len(v)>1}
print(D)

a = {}
seeded_win_percentage_array = []
seeded_team_name_list = []
a["BOS"] = .467
a["CHI"] = .345
a["ATL"] = .347
a["MIA"] = .190
a["PHX"] = .190
a["SAS"] = .837
a["GSW"] = .823

def order_dict(name_to_win_percentage_dict, seeded_team_name_list, seeded_win_percentage_array):
	for key, value in sorted(name_to_win_percentage_dict.iteritems(), key=lambda (k,v): (v,k), reverse=True):
	    seeded_team_name_list.append(key)
	    seeded_win_percentage_array.append(value)

order_dict(a, seeded_team_name_list, seeded_win_percentage_array)
# print(seeded_team_name_list)
# print(seeded_win_percentage_array)



import csv
import math

game_data = []
team_data = []
east_team_names = []
west_team_names = []

def csv_to_array(csv_file_name, array_to_copy):
	'''
	:param csv_file_name Name of the csv file being used

	Returns {Array} 2D array of tabular data from the csv file
	'''
	with open(csv_file_name) as csvfile:
		reader = csv.reader(csvfile) # change contents to floats
		for row in reader: # each row is a list
			array_to_copy.append(row)
	return

# Set the global array of game_data so that we can access and manipulate
csv_to_array('Analytics_Attachment/2016_17_NBA_Scores-Table 1.csv', game_data)
game_data = game_data[1:]
print(game_data)


csv_to_array('Analytics_Attachment/Division_Info-Table 1.csv', team_data)
team_data = team_data[1:]
# print(team_data)

# Reading team names into arrays by conference
for array in team_data:
	if array[2] == 'East':
		east_team_names.append(array[0])
	else:
		west_team_names.append(array[0])
# print(east_team_names)
# print(west_team_names)



win_dict = {}
team_result = []
win_percentage_result = []
wins_result = []
team_name = ["BOS", "CHI", "ATL", "MIA", "PHX", "SAS", "GSW"]
win_percentage = [.700, .613, .400, .281, .250, .833, .774]
wins = [21, 19, 12, 9, 7, 25, 24]
games_played = [30, 31, 30, 32, 28, 30, 31]
perfect_expected_wins = [55, 43, 39, 21, 18, 63, 67]


index_order = []
def determine_index_order(team_result, team_name, index_order):
	for correct_index_team in team_result:
		counter = 0
		for wrong_index_team in team_name:
			if correct_index_team == wrong_index_team:
				index_order.append(counter)
			else:
				counter += 1
	# print(index_order)
	return index_order

i=0
while i < len(team_name):
	win_dict[team_name[i]] = win_percentage[i]
	i += 1
# print(win_dict)


for key, value in sorted(win_dict.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    team_result.append(key)
    win_percentage_result.append(value)
# print(team_result)
# print(team_name)



determine_index_order(team_result, team_name, index_order)
last_seed_team = team_result[3]
# j = 0
# for team in team_name:
# 	if team == last_seed_team:
# 		print(j)
# 	else:
# 		j += 1
# standard = wins[j]
standard = wins[index_order[3]] 
i = 4
while i < len(team_result):
	comp_val = perfect_expected_wins[index_order[i]]
	if comp_val < standard:
		print(team_result[i] + " is eliminated!")
	else:
		print(team_result[i] + " is still in the running!")
	i+=1














