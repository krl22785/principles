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
	plt.figure(1)

	plt.subplot(211)
	plt.plot(my, appl,  marker = 'o')
	plt.title("Apple Equity Price")
	plt.grid(True)
	plt.ylabel('Normalized Price')
	plt.xticks(rotation = 45)

	plt.subplot(212)
	plt.plot(my, ms,  marker = '^')
	plt.title("Microsoft Equity Price")
	plt.grid(True)
	plt.ylabel('Normalized Price')
	plt.xticks(rotation = 45)

	plt.tight_layout()

	plt.savefig('problem1c.png', dpi = 120)


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