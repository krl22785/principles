import sys
import csv
from collections import Counter
import datetime 
import dateutil.parser as dparser 


filename = open(sys.argv[1])
f = csv.reader(filename, delimiter=',')

frequency = {} 

for line in f:
	createdDate = line[1]

	if createdDate in frequency:
		frequency[createdDate] += 1
	else:
		frequency[createdDate] = 1

sortedfrequency = sorted(frequency.items(), key = lambda x: (-x[1], x[0]), reverse = False)
date = dparser.parse(sortedfrequency[0][0])

print "%s with %s tweets" % (date.strftime('%B %d %Y, %H:%M:%S'), sortedfrequency[0][1])
print 

#daytime = []

#for line in f:
#	daytime.append(line[1])
	

#daytimeCounter = Counter(daytime)

#t = daytimeCounter.most_common(1)


#for i in t:
#	t1 = dparser.parse(i[0])
#	t1_date = t1.strftime('%B %d %Y')
#	t1_time = t1.strftime('%H:%M:%S')
#	print  '%s, %s with %s tweets' % (str(t1_date), str(t1_time), i[1])

	





#S e pt em b e r 19 2 0 1 4 , 2 1 : 3 9: 1 9 wit h 13 t w e e t s