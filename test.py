

a = {}
result = []

a["BOS"] = .467
a["CHI"] = .345
a["ATL"] = .347
a["MIA"] = .190
a["PHX"] = .190
a["SAS"] = .837
a["GSW"] = .823


for key, value in sorted(a.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    result.append(key)
print result

