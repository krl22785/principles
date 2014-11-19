import pandas as pd 
import datetime as dt
import csv 
import sys
import matplotlib
import matplotlib.pyplot as plt
#pd.set_option('display.mpl_style', 'default')



filename = open(sys.argv[1])
reader = csv.reader(filename, delimiter = ',')
headers = next(reader)

boroughComplaints = {}

for complaint in reader:
    borough = complaint[23]
    day_time = dt.datetime.strptime(complaint[1], "%m/%d/%Y %H:%M:%S %p")
    day = day_time.strftime('%Y-%m-%d')
    
    if borough in boroughComplaints:
        if day in boroughComplaints[borough]:
            boroughComplaints[borough][day] += 1
        else:
            boroughComplaints[borough][day] = 1
            
    else:
        dictCnt = {}
        dictCnt[day] = 1
        boroughComplaints[borough] = dictCnt

## create pandas dataframe

df = pd.DataFrame(boroughComplaints)
ymin = 0 
ymax = 2000

#del df["Unspecified"]

plt.figure(figsize=(6,8))

plt.subplot(511)
df["BRONX"].plot(color = '#d7191c', linewidth = 1.5)
plt.title("Bronx")
plt.ylabel('311 Calls')
plt.ylim(0, 2000)

plt.subplot(512)
df["BROOKLYN"].plot(color = "#fdae61", linewidth = 1.5)
plt.title("Brooklyn")
plt.ylabel('311 Calls')
plt.ylim(0, 2000)

plt.subplot(513)
df["MANHATTAN"].plot(color = '#b2abd2', linewidth = 1.5)
plt.title("Manhattan")
plt.ylabel('311 Calls')
plt.ylim(0, 2000)

plt.subplot(514)
df["QUEENS"].plot(color = '#abdda4', linewidth = 1.5)
plt.title("Queens")
plt.ylabel('311 Calls')
plt.ylim(0, 2000)

plt.subplot(515)
df["STATEN ISLAND"].plot(color = '#2b83ba', linewidth = 1.5)
plt.title("Staten Island")
plt.ylabel('311 Calls')
plt.ylim(0, 2000)

plt.tight_layout()

plt.show()


