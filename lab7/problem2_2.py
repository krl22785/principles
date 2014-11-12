import csv 
import sys
import pandas as pd
import scipy as sp
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
import datetime as dt


def ExecuteOrgData(dictionary):
    agencyTotals = {}
    for i in agencyComplaints:
        total = sum(agencyComplaints[i].values())
        agencyTotals[i] = total

    sortedTotals = sorted(agencyTotals.items(), key = lambda x: -x[1])[0:showCount]

    colList = []
    for j in sortedTotals:
        colList.append(j[0])

    df = pd.DataFrame(agencyComplaints)
    df1 = df[colList]

    for index, line in df1.iterrows():
        s = dt.datetime.strptime(index, '%Y-%m-%d')
        s1 = s.strftime('%b %d %Y')
        df1.loc[index, 'date'] = s1
    
    df2 = df1.set_index('date')

    df2.plot()
    plt.ylabel("Number of Complaints")
    plt.xlabel("Date")
    plt.title("Top %s Agencies with Complaints Over Time" % showCount)

    plt.show()

    


if __name__ == '__main__':
    pd.options.mode.chained_assignment = None
    filename = open(sys.argv[1])
    reader = csv.reader(filename, delimiter = ',')

    showCount = int(sys.argv[2])

    next(reader)
    agencyComplaints = {}

    for line in reader:
        agency = line[3]
        day_time = dt.datetime.strptime(line[1], "%m/%d/%Y %H:%M:%S %p")
        day = day_time.strftime('%Y-%m-%d')

        if agency in agencyComplaints:
            if day in agencyComplaints[agency]:
                agencyComplaints[agency][day] += 1
            else: 
                agencyComplaints[agency][day] = 1
        else:
            dictCnt = {} 
            dictCnt[day] = 1
            agencyComplaints[agency] = dictCnt

    ExecuteOrgData(agencyComplaints)