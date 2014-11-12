import sys
import csv
from collections import Counter
from operator import itemgetter, attrgetter

with open(sys.argv[1]) as filename:
	reader = csv.reader(filename, delimiter=',')

	NY = []
	SF = []
	
	for line in reader:
		if float(line[2]) <= -73.6895 and float(line[2]) >= -74.2557 and float(line[3]) >= 40.4957 and float(line[3]) <= 40.9176:
			#line.extend(n)
			NY.extend(line[4:])
		elif float(line[2]) <= -122.3247 and float(line[2]) >= -122.5155 and float(line[3]) >= 37.7038 and float(line[3]) <= 37.8545:
			#line.extend(s)
			SF.extend(line[4:])
		else:
			pass
	
	ny_ouput = Counter(NY)
	#print ny_ouput
	ny_final = ny_ouput.most_common(len(ny_ouput))

	sf_ouput = Counter(SF)
	sf_final = sf_ouput.most_common(len(sf_ouput))
	
	ny_final = sorted(ny_final, key=lambda x: (-x[1],x[0]))
	sf_final = sorted(sf_final, key=lambda x: (-x[1],x[0]))

	## OUTPUT 
	cnt_ny = 0
	print "New York:"
	for j in ny_final:
		if cnt_ny < 10:
			print "%s, %s" % (j[0], j[1])
			cnt_ny = cnt_ny + 1
		else:
			pass

	cnt_sf = 0 
	print "San Francisco:"
	for k in sf_final:
		if cnt_sf < 10:
			print "%s, %s" % (k[0], k[1])
			cnt_sf = cnt_sf + 1
		else:
			pass 