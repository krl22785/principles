import csv 
import sys
import pandas as pd
import scipy as sp
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def allComplaints(dictionary):
	df = pd.DataFrame(dictionary.items(), columns = ['zipcode','complaints'])
	return df

def allPopulations(dictionary):
	df1 = pd.DataFrame(population.items(), columns = ['zipcode','population'])
	return df1

def mergeGraph(df, df1):
	df3 = pd.merge(df, df1, on='zipcode')
	df3 = df3.set_index(['zipcode'])
	df3.sort_index(inplace=True)
	df3[['population']] = df3[['population']].astype(float)

	plt.scatter(df3.population, df3.complaints, color='b')
	plt.xlabel("Population")
	plt.ylabel("Number of Complaints")
	plt.title("Number of Complaints = f('Population')")
	plt.xlim(xmax = 120000, xmin = 0)
	plt.show()



if __name__ == '__main__':
	filename = open(sys.argv[1])
	reader = csv.reader(filename, delimiter = ',')
	next(reader)

	zipComplaints = {} 

	for i in reader: 
	    zipCode = i[8][:5]
	    if zipCode in zipComplaints:
	        zipComplaints[zipCode] += 1
	    else:
	        zipComplaints[zipCode] = 1

	df = allComplaints(zipComplaints)

	filename1 = open(sys.argv[2])
	reader1 = csv.reader(filename1, delimiter = ',')

	population = {} 

	for line in reader1:
		population[line[0]] = line[1]

	df1 = allPopulations(population)

	mergeGraph(df, df1)
