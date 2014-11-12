import sys
import csv 

filename = open(sys.argv[1])
reader = csv.reader(filename, delimiter=',')

next(reader) #use next reader to skip first line

job_dict = {} 

for line in reader:
	if line[5] not in job_dict:
		job_dict[line[5]] = 1
	else:
		job_dict[line[5]] += 1

totalLines = 0 

for com, cnt in sorted(job_dict.iteritems(), key=lambda x: (-x[1], x[0]), reverse=False):
	if totalLines < 3: 
		print "%s with %s complaints" % ((com, cnt))
		totalLines += 1
	else:
		break
		











#complaintType = []
#for row in reader: 
#	complaint = row.pop(5)
#	complaintType.append(complaint)

#complaintList = dict((i, complaintType.count(i)) for i in complaintType)

#for com, cnt in sorted(complaintList.items(), key=lambda x: (-x[1],x[0]))[:int(sys.argv[2])]:
#	print "%s with %s complaints" % ((com, cnt))


