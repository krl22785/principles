import csv 
import sys
import pandas as pd
import scipy as sp
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def allComplaintsbyAgency(dictionary):
	df = pd.DataFrame(dictionary)
	
	#colList = ['NYPD', 'DOT', 'DOB', 'TLC', 'DPR']
	df_agency = df[colList]
	df_agency['zipcode'] = df_agency.index

	return df_agency

def allPopulations(dictionary):
	df1 = pd.DataFrame(population.items(), columns = ['zipcode','population'])
	return df1


def mergeGraph(df_agency, df1):
	df3 = pd.merge(df_agency, df1, on='zipcode')
	df3[['population']] = df3[['population']].astype(float)

	plt.scatter(df3.population, df3.NYPD, color = 'blue', alpha = .5)
	plt.scatter(df3.population, df3.DOT, color = 'green', alpha = .5)
	plt.scatter(df3.population, df3.DOB, color = 'red', alpha = .5)
	plt.scatter(df3.population, df3.TLC, color = 'black', alpha = .5)
	plt.scatter(df3.population, df3.DPR, color = 'orange', alpha = .5)
	plt.xlabel("Population")
	plt.ylabel("Number of Complaints")
	plt.xlim(xmax = 120000, xmin = 0)
	plt.ylim(ymax = 1500, ymin = 0)
	plt.title("Number of Complaints by Population by Agency")
	plt.legend(colList, loc = 'upper left')

	plt.show()



if __name__ == '__main__':
	filename = open(sys.argv[1])
	reader = csv.reader(filename, delimiter = ',')
	next(reader)

	colList = ['NYPD', 'DOT', 'DOB', 'TLC', 'DPR']

	agencyComplaints = {}

	for line in reader:
		agency = line[3]
		zipCode = line[8][:5]

		if agency in agencyComplaints:
			if zipCode in agencyComplaints[agency]:
				agencyComplaints[agency][zipCode] += 1
			else:
				agencyComplaints[agency][zipCode] = 1
		else:
			dictCnt = {} 
			dictCnt[zipCode] = 1
			agencyComplaints[agency] = dictCnt

	df_agency = allComplaintsbyAgency(agencyComplaints)

	filename1 = open(sys.argv[2])
	reader1 = csv.reader(filename1, delimiter = ',')

	population = {} 

	for line in reader1:
		population[line[0]] = line[1]

	df1 = allPopulations(population)

	mergeGraph(df_agency, df1)



