import sys
import csv
from collections import Counter
#import os.path #


filename1 = open(sys.argv[1])
f1 = csv.reader(filename1, delimiter=',')

filename2 = open(sys.argv[2])
f2 = csv.reader(filename2, delimiter=',')

hashtag1 = []
hashtag2 = []

for ht1 in f1:
	hashtag1.extend(ht1[4:])

for ht2 in f2:
	hashtag2.extend(ht2[4:])

x = set(hashtag1).intersection(hashtag2)

for j in sorted(x):
	print j
