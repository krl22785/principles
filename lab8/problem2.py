import csv 
import sys
import pandas as pd
import scipy as sp
import numpy as np
import datetime as dt
import dateutil.parser as dparser
import matplotlib
import matplotlib.pyplot as plt


def time_to_seconds(time):
	t = []
	for i in time:
		new = dt.datetime.strptime(i, '%Y-%m-%d')
		new1 = new.strftime('%s')
		t.append(float(new1))

	return t

def frequencyPlot(n, t):
	fig1 = plt.figure()
	ax = fig1.add_subplot(111)
	ax.set_xticks(t)
	ax.set_xticklabels(time, rotation = 45)
	ax.hist(n, bins=98)
	ax.grid(True, linewidth = 2)
	ax.set_title("Assignment Due Dates")
	ax.set_xlabel("Date")
	ax.set_ylabel("Count")

	plt.savefig('problem2.png', dpi = 120)
	plt.show()


if __name__ == '__main__':
	f = open(sys.argv[1])
	reader = csv.reader(f, delimiter = ',')
	next(reader)

	n = []

	time = ['2007-09-18', '2007-10-04', '2007-10-25', '2007-11-27', '2007-12-15', '2007-12-11']

	for line in reader:
		d = dt.datetime.strptime(line[0],'%Y-%m-%d %H:%M:%S')
		d1 = d.strftime('%s')
		n.append(float(d1))

	t = time_to_seconds(time)

	frequencyPlot(n, t)