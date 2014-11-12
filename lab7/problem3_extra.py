import csv 
import sys
import pandas as pd
import scipy as sp
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def allComplaintsbyAgency(dictionary):
	df = pd.DataFrame(dictionary)
	
	df_agency = df[colList]
	df_agency['zipcode'] = df_agency.index

	return df_agency

def allPopulations(dictionary):
	df1 = pd.DataFrame(population.items(), columns = ['zipcode','population'])
	return df1


def mergeGraphLog(df_agency, df):
	df_agency["NYPD"] = np.log(df_agency['NYPD'])
	df_agency["DOT"] = np.log(df_agency['DOT'])
	df_agency["DOB"] = np.log(df_agency['DOB'])
	df_agency["TLC"] = np.log(df_agency['TLC'])
	df_agency["DPR"] = np.log(df_agency['DPR'])

	df3 = pd.merge(df_agency, df1, on = 'zipcode')
	#del final['population_x']
	df3 = df3.rename(columns = {'population_y': 'population'})
	df3 = df3.set_index('zipcode')
	df3[['population']] = df3[['population']].astype(float)

	plt.scatter(df3.population, df3.NYPD, color = 'blue', alpha = .5)
	plt.scatter(df3.population, df3.DOT, color = 'green', alpha = .5)
	plt.scatter(df3.population, df3.DOB, color = 'red', alpha = .5)
	plt.scatter(df3.population, df3.TLC, color = 'black', alpha = .5)
	plt.scatter(df3.population, df3.DPR, color = 'orange', alpha = .5)
	plt.xlabel("Population")
	plt.ylabel("Log (Number of Complaints)")
	plt.title("LOG of Complaints by Population by Agency")
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

	mergeGraphLog(df_agency, df1)
