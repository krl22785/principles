import sys
import csv
import datetime 
import time

with open(sys.argv[1]) as filename:
	reader = csv.reader(filename, delimiter=',')

	next(reader) # skip header

	numRows = 0

	#%m/%d/%Y %H:%M:%S

	mindate = time.strftime("%m/%d/%Y %H:%M:%S %p")
	maxdate = 0
	
	for line in reader:
		numRows += 1
		createdDate = line[1]
		if createdDate 	< mindate:
			mindate = line[1]
		elif createdDate > maxdate:
			maxdate = line[1]
		else:
			pass

	mind = datetime.datetime.strptime(mindate, "%m/%d/%Y %I:%M:%S %p")
	maxd = datetime.datetime.strptime(maxdate, "%m/%d/%Y %I:%M:%S %p")
	
	print '%d complaints between %s and %s' % (numRows, mind, maxd)
