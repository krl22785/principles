import sys
import csv
#import matplotlib

# Functions for students to implement.
def solveOnlyLists(inputList):
    uniqueList = []

    for item in inputList:
    	if item not in uniqueList:
    		uniqueList.append(item)
    	else:
    		pass 

    return uniqueList

def solveDict(inputList):
    uniqueList = []
    dbList = {} 

    for item in inputList:
    	if item not in dbList:
    		dbList[item] = 1
    	else:
    		pass 

    uniqueList = dbList.keys()
    return uniqueList

def solveSorted(sortedInputList):
    uniqueList = []
    
    n = None
    for item in sortedInputList:
    	if item != n:
    		uniqueList.append(item)
    		n = item 
    	else:
    		pass 

    return uniqueList




