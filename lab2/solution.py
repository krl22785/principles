import sys
import os.path
import csv
import urllib2


def clear():  
  database = {} 
  pass

def insert(fieldValues):
  
  if fieldValues[0] not in database.keys():
    job_details = {}

    for j in range(1, len(rowName)): #rowname is named in global at the very bottom
      job_details[rowName[j]] = fieldValues[j]
      database[fieldValues[0]] = job_details

def update_all(params):
    query_field_name = params[0]
    query_field_value = params[1]
    update_field_name = params[2]
    update_field_value = params[3]

    updatedRowCount = 0

    if query_field_name == 'Job ID':
      for masterKey, details in sorted(database.items()):
        if masterKey == query_field_value:
          updatedRowCount += 1
          details[update_field_name] = update_field_value
    else:
      for masterKey, details in sorted(database.items()):
        if details[query_field_name] == query_field_value:
          updatedRowCount += 1
          details[update_field_name] = update_field_value
    
    print str(updatedRowCount)

def delete_all(params):
  field_name, field_value = params
  
  if field_name == 'Job ID':
    for masterKey, details in sorted(database.items()):
      if masterKey == field_value:
        del database[field_value]
  else:
    for masterKey, details in sorted(database.items()):
      if details[field_name] == field_value:
        del database[masterKey]
    
def find(params):
  field_name, field_value = params

  if field_name == 'Job ID':
    for key, value in sorted(database.items()):
      if key == field_value:
        #output = output + '|' + database[field_value]
        print '{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}'.format(key, value['Agency'], value['# Of Positions'], value['Business Title'], value['Civil Service Title'], value['Salary Range From'], value['Salary Range To'], value['Salary Frequency'], value['Work Location'], value['Division/Work Unit'], value['Job Description'], value['Minimum Qual Requirements'],value['Preferred Skills'],value['Additional Information'],value['Posting Date'])
      else:
        pass
  else:
    for key, value in sorted(database.items()):
      if value[field_name] == field_value:
        print '{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}'.format(key, value['Agency'], value['# Of Positions'], value['Business Title'], value['Civil Service Title'], value['Salary Range From'], value['Salary Range To'], value['Salary Frequency'], value['Work Location'], value['Division/Work Unit'], value['Job Description'], value['Minimum Qual Requirements'],value['Preferred Skills'],value['Additional Information'],value['Posting Date'])


def count(params):
  field_name, field_value = params

def dump(params):

  for key, value in sorted(database.items()):
    print '{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}'.format(key, value['Agency'], value['# Of Positions'], value['Business Title'], value['Civil Service Title'], value['Salary Range From'], value['Salary Range To'], value['Salary Frequency'], value['Work Location'], value['Division/Work Unit'], value['Job Description'], value['Minimum Qual Requirements'],value['Preferred Skills'],value['Additional Information'],value['Posting Date'])
      
    
def view(fieldNames):
  
  for jobid in sorted(database):
    output = ''
    for field in fieldNames:
      if field == 'Job ID':
        output = output + '|' + jobid
        #print output
      else:
        output = output + '|' + database[jobid][field]
        #print output
    print output[1:]


def executeCommand(commandLine):
  tokens = commandLine.split('|') 
  command = tokens[0]
  parameters = tokens[1:] 

  if command == 'insert':
    insert(parameters)
  elif command == 'delete_all':
    delete_all(parameters)
  elif command == 'update_all':
    update_all(parameters)
  elif command == 'find':
    find(parameters)
  elif command == 'count':
    count(parameters)
  elif command == 'count_unique':
    count_unique(parameters)
  elif command == 'clear':
    clear()
  elif command == 'dump':
    dump(parameters)
  elif command == 'view':
    view(parameters)
  else:
    print 'ERROR: Command %s does not exist' % (command,)
    assert(False)

def executeCommands(commandFileName):
  f = open(commandFileName)
  for line in f:
    executeCommand(line.strip())

if __name__ == '__main__':

  database = {}
  rowName = []

  if os.path.isfile('database.txt'):
    f = open('database.txt', 'w+')

    rowName = ['Job ID', 'Agency','# Of Positions','Business Title','Civil Service Title','Salary Range From','Salary Range To','Salary Frequency','Work Location','Division/Work Unit','Job Description','Minimum Qual Requirements','Preferred Skills','Additional Information','Posting Date']

  else:
    url = 'http://vgc.poly.edu/projects/gx5003-fall2014/week2/lab/data/NYC_Jobs_sample.csv'
    response = urllib2.urlopen(url)
    cr = csv.reader(response, delimiter='|')
    rowName = []
    for i, j in enumerate(cr):
      if i == 0:
        for k in j:
          rowName.append(k)
      else:
        pass

  executeCommands(sys.argv[1])

  with open('database.txt', 'w') as f:
    f.write(str(database))

    f.close()






  