import sys
import csv
import datetime as dt
import dateutil.parser as dparser 
import time
#import os.path #

filename = open(sys.argv[1])
f = csv.reader(filename, delimiter=',')

lines = 0 
mindate = time.strftime('%a %b %d %H:%M:%S %Z %Y')
maxdate = None

for line in f:
	lines += 1
	date = line[1]
	if date < mindate:
		mindate = date
	elif date > maxdate:
		maxdate = date
	else:
		pass 

mind = dparser.parse(mindate)
maxd = dparser.parse(maxdate)

newmin = mind.strftime('%B %d %Y, %H:%M:%S')
newmax = maxd.strftime('%B %d %Y, %H:%M:%S')

print "There were %s tweets between %s and %s" % (lines, newmin, newmax)

