import sys
import csv
from collections import Counter
import datetime as dt
import dateutil.parser as dparser 

filename = open(sys.argv[1])
f = csv.reader(filename, delimiter=',')

daytime = []
db = {}

for line in f:
	
	daytime.append(line[1])

	if line[0] not in db:
		db[line[0]] = 1
	else:
		db[line[0]] += 1

min_daytime = dparser.parse(min(daytime))
max_daytime = dparser.parse(max(daytime))

min_daytime_final = min_daytime .strftime('%B %d %Y, %H:%M:%S')
max_daytime_final = max_daytime .strftime('%B %d %Y, %H:%M:%S')

db =sorted(db.items(), key=lambda x: -x[1])

print "%s tweeted the most" % str(db[0][0])
print "Dataset range: %s and %s" % (min_daytime_final, max_daytime_final)





