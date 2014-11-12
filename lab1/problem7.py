import sys
import csv 
import time

if len(sys.argv) != 3:
	print "Usage: python problem7.py [filename] [zip_borough]"
	sys.exit()

datafilename = sys.argv[1]
zipfilename = sys.argv[2]

#open complaints file 
complaintsByZip = {} 

filename = open(datafilename, 'r')
reader = csv.reader(filename, delimiter = ",")

next(reader)

for line in reader:
	zipCode = line[7]
	if zipCode not in complaintsByZip:
		complaintsByZip[zipCode] = 1
	else:
		complaintsByZip[zipCode] += 1
	
#open zip-borough file 	
zipBorough = {} 
filename1 = open(zipfilename, 'r')
reader1 = csv.reader(filename1, delimiter = ",")
next(reader1)

for line in reader1:
	zipCode = line[0]
	borough = line[1]
	zipBorough[zipCode] = borough

#sum all complaints by borough 
results = {} 
for zipCode in complaintsByZip:
	borough = zipBorough[zipCode]
	complaints = complaintsByZip[zipCode]

	if borough in results:
		results[borough] += complaints
	else:
		results[borough] = complaints

for k, j in sorted(results.items(), reverse = True):
	print k, j


