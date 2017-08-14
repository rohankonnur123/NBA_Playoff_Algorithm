

# a = {}
result = []

# a["BOS"] = .467
# a["CHI"] = .345
# a["ATL"] = .347
# a["MIA"] = .190
# a["PHX"] = .190
# a["SAS"] = .837
# a["GSW"] = .823


win_dict = {}
team_name = ["BOS", "CHI", "ATL", "MIA", "PHX", "SAS", "GSW"]
win_percentage = [.467, .345, .347, .190, .190, .837, .823]

i=0
while i < len(team_name):
	win_dict[team_name[i]] = win_percentage[i]
	i += 1
print win_dict


for key, value in sorted(win_dict.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    result.append(key)
print result




