import sys
import csv 
import datetime

filename = open(sys.argv[1])
reader = csv.reader(filename, delimiter=',')

next(reader)

daysWeek = []

for line in reader:
	new_date = datetime.datetime.strptime(line[1], "%m/%d/%Y %H:%M:%S %p")
	daysWeek.append(new_date.strftime("%A"))

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for day in weekdays:
	cnt = daysWeek.count(day)
	print "%s == %s" % (day, cnt)
