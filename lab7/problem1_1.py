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

next(reader)

agency = {}

for i in reader:
    if i[3] in agency:
        agency[i[3]] += 1 
    else:
        agency[i[3]] = 1 

df = pd.DataFrame(agency.items(), columns=['agency','count'])
df1 = df.set_index(['agency'])
df2 = df1.loc[['NYPD', 'DOB','DOT','TLC','DPR']]
df2 = df2.sort(columns='count', ascending=False)


df2.plot(kind='bar', grid=False, legend=False, color='blue', alpha=.5)
plt.title("Total Complaints by Agency")
plt.ylabel("Total Complaints")
plt.xlabel("Agency")
plt.ylim(ymax = 100000, ymin = 0)

plt.show()