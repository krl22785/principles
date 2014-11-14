import csv
import shapefile
import sys
import math
import operator
from bokeh.plotting import *
from bokeh.sampledata.iris import flowers
from bokeh.objects import HoverTool, ColumnDataSource
from collections import OrderedDict


def loadZipComplaints(ComplaintFile):

    filename =  open(ComplaintFile)
    reader = csv.reader(filename, delimiter = ',')
    headers = reader.next()
    zipIndex = headers.index('Incident Zip')
    latColIndex = headers.index('Latitude')
    lngColIndex = headers.index('Longitude')
    agencyIndex = headers.index('Agency')

    lat = []
    lng = []

    agencyDict = {}
    colors = []
    complaintsperzip = {}


    for row in reader:
        try:
            lat.append(float(row[latColIndex]))
            lng.append(float(row[lngColIndex]))
            agency = row[agencyIndex]
            zipcode = row[zipIndex]

            ##WHAT DOES THIS DO?
            if not agency in agencyDict:
                agencyDict[agency] = len(agencyDict)

            if zipcode in complaintsperzip:
                if agency in complaintsperzip[zipcode]:
                    complaintsperzip[zipcode][agency] += 1
                else:
                    complaintsperzip[zipcode][agency] = 1
            else:
                complaintsperzip[zipcode]={}
                complaintsperzip[zipcode][agency]=1

        except:
            pass


    return {'zip_complaints': complaintsperzip}



def getZipBorough(zipBoroughFilename):

    filename = open(zipBoroughFilename)
    reader = csv.reader(filename, delimiter = ',')
    reader.next()

    return {row[0]: row[1] for row in reader}


def drawPlot(shapeFilename, mapPoints, zipBorough):

    dat = shapefile.Reader(shapeFilename)

    zipCodes = []

    zc = []
    topAgency = []
    totalComplaints = []

    polygons = {'lat_list': [], 'lng_list': [], 'color_list' : [], 'top_agency': [], 'agency_count': []}
#    colorscale = ["#a6cee3", "#1f78b4", "#b2df8a", "#33a02c", "#fb9a99", "#e31a1c", "#fdbf6f", "#ff7f00", "#cab2d6", "#6a3d9a", "#ffff99", "#b15928"]

    colors = {'NYPD': "#33a02c",
              'DOT': "#1f78b4",
              'DOB': "#b2df8a",
              'HPD': "#a6cee3",
              'DSNY': "#fb9a99",
              'DPR': "#e31a1c",
              'DOHMH': "#fdbf6f",
              'DEP': "#ff7f00",
              'DCA': "#cab2d6",
              'TLC': "#6a3d9a",
              'FDNY': "#ffff99",
              'DHS': "#b15928"}

    record_index = 0
    for r in dat.iterRecords():
        currentZip = r[0]

        if currentZip in zipBorough:
            zipCodes.append(currentZip)

            shape = dat.shapeRecord(record_index).shape
            points = shape.points

            lngs = [p[0] for p in points]
            lats = [p[1] for p in points]

            polygons['lng_list'].append(lngs)
            polygons['lat_list'].append(lats)


            if currentZip in mapPoints['zip_complaints']:
                #sort based on top complaints
                sortedlist = sorted(mapPoints['zip_complaints'][currentZip].items(), key=operator.itemgetter(1), reverse=True)
                agency = sortedlist[0][0]
                polygons['top_agency'].append(agency)
                count = sortedlist[0][1]
                polygons['agency_count'].append(count)

            #sortedlist[0][0], sortedlist[0][1] 
        record_index += 1

    print polygons




if __name__ == '__main__':
    if len(sys.argv) != 4:
        print 'Usage:'
        print sys.argv[0] + '1: [complaints] 2: [zip_borough] 3: [shapefile]'
        print '\ne.g.: ' + sys.argv[0] + ' 311nyc.csv zip_borough.csv shape_data/'
    else:
        mapPoints = loadZipComplaints(sys.argv[1])
        zipBorough = getZipBorough(sys.argv[2])
        drawPlot(sys.argv[3], mapPoints, zipBorough)






#dat = shapefile.Reader(shapeFilename)

#test = sorted(mapPoints['zip_complaints'].items(), key=operator.itemgetter(1), reverse = True)
#uniques = {}
#for v in mapPoints['zip_complaints'].items():
    #test = sorted(v[1].items(), key=operator.itemgetter(1), reverse = True)
    #print "%s: %s" % (v[0], test[0][0])
    #j = test[0][0]
    #if j not in uniques:
    #    uniques[j] = 1
#    else:
#        uniques[j] += 1

#print uniques
