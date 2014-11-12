import csv 
import sys
import pandas as pd
import scipy as sp
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
#%matplotlib inline
import datetime as dt

filename = open(sys.argv[1])
#sys.argv[1]
reader = csv.reader(filename, delimiter = ',')

next(reader)
agencyComplaints = {}

for line in reader:
    agency = line[3]
    day_time = dt.datetime.strptime(line[1], "%m/%d/%Y %H:%M:%S %p")
    day = day_time.strftime('%Y-%m-%d')

    #day = day_time.strftime('%b %d %Y')

    if agency in agencyComplaints:
        if day in agencyComplaints[agency]:
            agencyComplaints[agency][day] += 1
        else: 
            agencyComplaints[agency][day] = 1
    else:
        dictCnt = {} 
        dictCnt[day] = 1
        agencyComplaints[agency] = dictCnt
        
nypd = agencyComplaints['NYPD']
df_nypd = pd.DataFrame(nypd.items(), columns=['date','count']) 

tlc = agencyComplaints['TLC']
df_tlc = pd.DataFrame(tlc.items(), columns=['date','count'])

dpr = agencyComplaints['DPR']
df_dpr = pd.DataFrame(dpr.items(), columns=['date','count'])
 
df = pd.merge(df_nypd, df_tlc, on='date')
df1 = pd.merge(df, df_dpr, on = 'date')

df1.columns = ['date', 'NYPD', 'TLC', 'DPR']
df2 = df1.sort(columns='date', ascending=True)

for index, line in df2.iterrows():
    s = dt.datetime.strptime(line[0], '%Y-%m-%d')
    s1 = s.strftime('%b %d %Y')
    df2.loc[index, 'date'] = s1

df3 = df2.set_index('date')
df3.plot()
plt.ylabel("Number of Complaints")
plt.xlabel("Date")
plt.title("Number of Complaints Over Time")

plt.show()
