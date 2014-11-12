import csv 
import sys
import pandas as pd
import scipy as sp
import numpy as np
import datetime as dt
import dateutil.parser as dparser
import matplotlib
import matplotlib.pyplot as plt



def lineGraph(my, appl):
	plt.plot(my, appl, marker = 'o')
	plt.grid(True)
	plt.ylabel('APPL Price')
	plt.xlabel('Month-Year')
	plt.title('Apple Equity Price')
	plt.xticks(rotation = 45)
	

	plt.savefig('problem1a.png', dpi = 120)
	plt.show()

if __name__ == '__main__':
	f = open(sys.argv[1])
	reader = csv.reader(f, delimiter = ',')
	next(reader)

	my = []
	appl = []

	for line in reader:
		date = dt.datetime.strptime(line[0], '%Y-%m')
		my.append(date)
		appl.append(line[1])


	lineGraph(my, appl)