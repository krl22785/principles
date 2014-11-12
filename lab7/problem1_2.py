import csv 
import sys 

import pandas as pd
import scipy as sp
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
import pylab

filename = open(sys.argv[1])
reader = csv.reader(filename, delimiter = ",")

showCount = int(sys.argv[2])

next(reader)

agency = {}

for i in reader:
    if i[3] in agency:
        agency[i[3]] += 1 
    else:
        agency[i[3]] = 1 

df = pd.DataFrame(agency.items(), columns=['agency','count'])
df1 = df.set_index(['agency'])
df1 = df1.sort(columns='count', ascending=False)
showTable = df1[:showCount]


showTable.plot(kind='bar', grid=False, legend=False, color = 'red', alpha = .5)
plt.ylabel("Total Complaints")
plt.xlabel(("Top %s Agencies" % showCount))
plt.title("Top %s Agencies by Complaints" % showCount)
plt.show()