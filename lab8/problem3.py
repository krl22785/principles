import csv 
import sys
import pandas as pd
import scipy as sp
import numpy as np
import datetime as dt
import dateutil.parser as dparser
import matplotlib
import matplotlib.pyplot as plt


def plotDots(proc, year, pwr):

	fig1 = plt.figure(figsize=[14,8])
	ax = fig1.add_subplot(121)

	
	ax.plot(year,index,'o')
	ax.set_yticks(index)
	ax.set_yticklabels(proc)
	ax.set_xlim(xmin=min(year)-5, xmax=max(year)+5)
	ax.set_ylim(ymin=min(index)-1, ymax=max(index)+1)
	ax.hlines(index, [0] , year, linestyles='dotted', lw=5)
	ax.set_title("Year of Introduction")
	ax.set_xlabel("Year")

	ax = fig1.add_subplot(122)
	ax.plot(trans,index,'o')
	ax.set_yticks(index)
	ax.set_yticklabels(proc)
	ax.set_ylim(ymin=min(index)-1, ymax=max(index)+1)
	ax.set_xlim(xmin=min(trans)-2, xmax=max(trans)+2)
	ax.hlines(index, [0] , trans, linestyles='dotted', lw=5)
	ax.set_title("Number of Transistors")
	ax.set_xlabel("Transistors")

	plt.tight_layout()

	return fig1



if __name__ == '__main__':
	f = open(sys.argv[1])
	reader = csv.reader(f, delimiter = ',')
	next(reader)

	proc = []
	year = []
	trans = []

	for i in reader:
		proc.append(i[0])
		year.append(float(i[1]))
		pwr = np.log10(float(i[2]))

		trans.append(pwr)

	index = np.arange(len(proc))

	fig = plotDots(proc, year, pwr)
	fig.savefig('problem3.png', dpi = 120)

	plt.show()