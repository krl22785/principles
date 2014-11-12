import csv 
import sys
import pandas as pd
import scipy as sp
import numpy as np
import datetime as dt
import dateutil.parser as dparser
import matplotlib
import matplotlib.pyplot as plt



def scatterplot(data, data_name):

	N = len(data)
	colors = np.random.rand(N)
	fig = plt.figure(figsize=[10, 10])

	for i in range(N):
		for j in range(N):
			ax = fig.add_subplot(N,N,i*N+j+1)
			if j == 0:
				ax.set_ylabel(data_name[i], size = '12')
			if i == 0:
				ax.set_title(data_name[j], size = '12')
			if i == j:
				ax.hist(data[i], 25, alpha = .5, color = 'orange')
				ax.xaxis.set_tick_params(labelsize=8)
				ax.yaxis.set_tick_params(labelsize=8)
			else:
				ax.scatter(data[j], data[i], c=colors)
				ax.xaxis.set_tick_params(labelsize=8)
				ax.yaxis.set_tick_params(labelsize=8)

	plt.suptitle('Gene Correlation', fontsize = 14)
	plt.tight_layout

	return fig


if __name__ == '__main__':
	f = open(sys.argv[1])
	reader = csv.reader(f, delimiter = ',')
	next(reader)


	A = []
	B = []
	C = []
	D = []

	for dp in reader:
		A.append(float(dp[0]))
		B.append(float(dp[1]))
		C.append(float(dp[2]))
		D.append(float(dp[3]))


	data = [A, B, C, D]
	data_name = ['Gene A', 'Gene C', 'Gene D', 'Gene B']

	fig = scatterplot(data, data_name)
	fig.savefig('problem4a.png', dpi = 120)
	plt.show()


