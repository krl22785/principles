import sys
import csv
from collections import Counter


filename = open(sys.argv[1])
f = csv.reader(filename, delimiter=',')
hashtags = []

for line in f:
	hashtags.extend(line[4:])

hashtagCounter = Counter(hashtags)

cnt = 0

sortedHashtag = sorted(hashtagCounter.items(), key = lambda x: (-x[1], x[0]), reverse = False)

for i in sortedHashtag:
	if cnt < 14:
		print str(i[0]) + " " + str(i[1])
		cnt += 1
	else:
		break
