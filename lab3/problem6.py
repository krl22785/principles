import sys
import csv
from collections import Counter
import datetime as dt
import dateutil.parser as dparser 

filename = open(sys.argv[1])
f = csv.reader(filename, delimiter=',')

db = {} 

for i in f: 
	t1 = dt.datetime.strptime(i[1], '%a %b %d %H:%M:%S %Z %Y')
	t1_date = t1.strftime('%B %d %Y, %H')

	if t1_date not in db:
		db[t1_date] = 1 
	else:
		db[t1_date] = 1 + db[t1_date]

final = sorted(db.items(), key=lambda x:x[1], reverse=True)

print '%sh with %s tweets' % (final[0][0], final[0][1])



