import csv 
import sys
import pandas as pd
import scipy as sp
import numpy as np
import datetime as dt
import dateutil.parser as dparser
import matplotlib
import matplotlib.pyplot as plt


def lineGraphNormalized(my, appl):
	co = ['Apple','Microsoft']
	plt.plot(my, appl, marker = 'o')
	plt.plot(my, ms, marker = '^')
	plt.grid(True)
	plt.ylabel('Normalized Price')
	plt.xlabel('Month-Year')
	plt.title('Equity Price')
	plt.xticks(rotation = 45)
	plt.legend(co, 'upper left')

	plt.savefig('problem1b.png', dpi = 120)


	plt.show()



if __name__ == '__main__':
	f = open(sys.argv[1])
	reader = csv.reader(f, delimiter = ',')
	next(reader)

	my = []
	appl = []
	ms = []

	for line in reader:
		date = dt.datetime.strptime(line[0], '%Y-%m')
		my.append(date)
		A = float(line[1])/75.51
		M = float(line[2])/27.06
		appl.append(A)
		ms.append(M)


	lineGraphNormalized(my, appl)