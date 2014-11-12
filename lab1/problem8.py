import sys
import csv 
from collections import Counter

filename = open(sys.argv[1])
reader = csv.reader(filename, delimiter=',')

masterZip = open(sys.argv[2])
masterReader = csv.reader(masterZip, delimiter=',')
next(masterReader)

all_zip = []
for row in reader:
	acc_zip = row.pop(7)
	all_zip.append(acc_zip)

man = []
que = []
brk = []
sta = []
brx = []

for i in all_zip:
	if i[:3] == '112':
		brk.append(i) #brooklyn 
	elif i[:3] == '100' or i[:3] == '101' or i[:3] == '102':
		man.append(i) #manhattan
	elif i[:3] == '103':
		sta.append(i) #staten island  
	elif i[:3] == '104':
		brx.append(i) #bronx
	elif i[:3] == '110' or i[:3] == '111' or i[:3] == "113" or i[:3] == "114" or i[:3] == "116":
		que.append(i) #queens 	
	elif i[:3] == '103':
		sta.append(i)
	else:
		continue

true_zip = []

for m in masterReader:
	real = m.pop(0)
	true_zip.append(real)

results_brk = Counter()
results_man = Counter()
results_sta = Counter()
results_que = Counter()
results_brx = Counter()

for w in brk:
	results_brk[w] = brk.count(w)

for v in man:
	results_man[v] = man.count(v)

for w in sta:
	results_sta[w] = sta.count(w)

for t in que:
	results_que[t] = que.count(t)

for s in brx:
	results_brx[s] = brx.count(s)

print "Brooklyn with %s complaints" % sum(results_brk.values()) 
print "Bronx with %s complaints" % sum(results_brx.values())
print "Manhattan with %s complaints" % sum(results_man.values()) 
print "Queens with %s complaints" % sum(results_que.values())
print "Staten Island with %s complaints" % sum(results_sta.values())

