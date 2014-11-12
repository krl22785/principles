import sys
import csv
import datetime# as dt
import dateutil.parser as dparser 
from collections import Counter
import time
#import os.path #


filename = open(sys.argv[1])
f = csv.reader(filename, delimiter=',')

mindate = time.strftime('%a %b %d %H:%M:%S %Z %Y')
maxdate = None

users = {}
for line in f:
	user = line[0]
	date = line[1]
	if user in users:
		users[user] += 1
	else:
		users[user] = 1

	if date < mindate:
		mindate = date 
	elif date > maxdate:
		maxdate = date
	else:
		pass
		
cnt = 0
for name in users:
	cnt += 1

mind = dparser.parse(mindate)
maxd = dparser.parse(maxdate)

newmin = mind.strftime('%B %d %Y, %H:%M:%S')
newmax = maxd.strftime('%B %d %Y, %H:%M:%S')

print "%s users tweeted between %s and %s" % (cnt, newmin, newmax)