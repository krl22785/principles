import sys
import csv 

filename = open(sys.argv[1]) # be careful with type of file open you use 
reader = csv.reader(filename, delimiter=',')

next(reader) #use next reader to skip first line

agencyComplaintsByZip = {} 

for line in reader:
	agency = line[3]
	zipCode = line[7]

	if agency in agencyComplaintsByZip:
		if zipCode in agencyComplaintsByZip[agency]:
			agencyComplaintsByZip[agency][zipCode] = 1
		else:
			agencyComplaintsByZip[agency][zipCode] = 1
	else:
		myDict = {}
		myDict[zipCode] = 1
		agencyComplaintsByZip[agency] = myDict

sortedAgencies = sorted(agencyComplaintsByZip.keys())

## this is where i finished

for agencies in sortedAgencies:
	counts = agencyComplaintsByZip[agencies]
	maxCount = -1 
	maxKey = ""

	for zip in counts:
		count = counts[zip]
		if count > maxCount:
			maxCount = count
			maxKey = zip

	if maxCount == 0:
		assert(False)
	
	allMax = [z for z,t in counts.iteritems() if t==maxCount]
	strAllMax = " ".join(sorted(allMax))


