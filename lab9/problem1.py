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
    topAgency = []
    totalComplaints = []

    polygons = {'lat_list': [], 'lng_list': [], 'color_list' : [], 'zip': [], 'top_agency': [], 'agency_count': []}
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
        
            shape = dat.shapeRecord(record_index).shape
            points = shape.points

            lngs = [p[0] for p in points]
            lats = [p[1] for p in points]

            polygons['lng_list'].append(lngs)
            polygons['lat_list'].append(lats)

            if currentZip in mapPoints['zip_complaints']:
                
                sortedlist = sorted(mapPoints['zip_complaints'][currentZip].items(), key=operator.itemgetter(1), reverse=True)
                agency = sortedlist[0][0]
                count = sortedlist[0][1]

                #########print currentZip, sortedlist

                if agency in colors:
                    color = colors[agency]
                else:
                    color = 'white'
            else:
                color = 'white'

            polygons['color_list'].append(color)
            polygons['zip'].append(currentZip)
            polygons['top_agency'].append(agency)
            polygons['agency_count'].append(count)

        record_index += 1

    source = ColumnDataSource(
        data=dict(
            long=polygons['lng_list'],
            lat = polygons['lat_list'],
            col=polygons['color_list'],
            zipcode= polygons['zip'],
            agency= polygons['top_agency'],
            count= polygons['agency_count'],
        )
    )

    output_file("Problem1.html", title = "NYC by Zip" )

    TOOLS="pan,wheel_zoom,box_zoom,reset,previewsave,resize,hover"

    patches(polygons['lng_list'], polygons['lat_list'], source=source, \
            fill_color = 'col', line_color='gray', \
            tools=TOOLS, plot_width = 900, plot_height = 700, \
            title = 'Zip Codes by Agency Complaint')
 
    hover = curplot().select(dict(type=HoverTool))
    hover.tooltips = OrderedDict([
        ("Zip Code", "@zipcode"),
        ("Agency", "@agency"),
        ("Complaints", "@count"),
    ])

    hold()

    for i, area in enumerate(colors.items()):
        scatter(0, 0, color = area[1], size = .4, legend = area[0])

    show()

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print 'Usage:'
        print sys.argv[0] + '1: [complaints] 2: [zip_borough] 3: [shapefile]'
        print '\ne.g.: ' + sys.argv[0] + ' 311nyc.csv zip_borough.csv shape_data/'
    else:
        mapPoints = loadZipComplaints(sys.argv[1])
        zipBorough = getZipBorough(sys.argv[2])
        drawPlot(sys.argv[3], mapPoints, zipBorough)
