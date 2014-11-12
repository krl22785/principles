import csv 
import sys 
import pandas as pd
import scipy as sp
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
import datetime as dt
import dateutil.parser as dparser 

filename = open(sys.argv[1])
reader = csv.reader(filename, delimiter=',')

next(reader)
n = []
hourCount = {}
for line in reader:
        
    x = dt.datetime.strptime(line[1], "%m/%d/%Y %I:%M:%S %p")
    n.append(x.hour)



plt.hist(n, bins = int(sys.argv[2]), color='blue', alpha = .5)
plt.xlim(xmin = 0, xmax = 23)
plt.ylim(ymin = 0, ymax = 140000)
plt.title("311 Calls By Time of Day")
plt.xlabel("Hour in the Day")
plt.ylabel("Number of Complaints")
plt.grid(True)
plt.show()