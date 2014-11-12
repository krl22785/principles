import sys
import csv 
from collections import Counter

filename = open(sys.argv[1])
reader = csv.reader(filename, delimiter=',')

next(reader) #use next reader to skip first line

job_dict = {}

for line in reader:
	if line[5] not in job_dict:
		job_dict[line[5]] = 1
	else:
		job_dict[line[5]] += 1

for complaint, cnt in job_dict.items():
	print "%s with %s complaints" % (complaint, cnt)






#complaintType = []
#for row in reader: 
#	complaint = row.pop(5)
#	complaintType.append(complaint)

#ct = Counter(complaintType)

#complaintList = dict((i, complaintType.count(i)) for i in complaintType)

#for com, cnt in complaintList.items():
#	print "%s with %s complaints" % ((com, cnt))



