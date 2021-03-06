import csv
import shapefile
import sys
import math
import operator
from bokeh.plotting import *
from bokeh.sampledata.iris import flowers
from bokeh.objects import HoverTool, ColumnDataSource
from collections import OrderedDict
import numpy as np
import math


def loadZipComplaints(ComplaintFile):

	filename = open(ComplaintFile)
	reader = csv.reader(filename, delimiter = ',')

	headers = reader.next()

	x0 = -74.30
	x1 = -73.60
	y0 = 40.40 
	y1 = 41.00

	xdiff = (-73.60--74.30)
	ydiff = (41.00 - 40.40)

	latColIndex = headers.index('Latitude')
	lngColIndex = headers.index('Longitude')

	lat = [] 
	lng = []

	xindex = [] 
	yindex = []

	for row in reader:
		try:
			lat.append(float(row[latColIndex]))
			lng.append(float(row[lngColIndex]))
			yindex.append(np.floor((float(row[latColIndex]) - y0) / float((ydiff/n))))
			xindex.append(np.floor((float(row[lngColIndex]) - x0) / float((xdiff/n))))

		except:
			pass 

	return {'lat_list': lat, 'lng_list': lng, 'index': zip(yindex, xindex)} 

def getZipBorough(zipBoroughFilename):

	filename = open(zipBoroughFilename)
	reader = csv.reader(filename, delimiter = ',')
	reader.next()

	return {row[0]: row[1] for row in reader}


def getDots(mapPoints): 
	x0 = -74.30
	x1 = -73.60
	y0 = 40.40 
	y1 = 41.00

	xdiff = (-73.60--74.30)
	ydiff = (41.00 - 40.40)

	compare = {}
	for line in mapPoints['index']:
		if line not in compare:
			compare[line] = 1
		else:
			compare[line] += 1 

	total = sum(compare.values())

	lng1 = []
	lat1 = []
	size = []

	for k, v in compare.iteritems():
		y = y0 + float((ydiff/n) * k[0])
		x = x0 + float((xdiff/n) * k[1])

		y1 = y + ((ydiff/n)/2.00)
		x1 = x + ((xdiff/n)/2.00)

		size1 = math.log(v, 2) #(v/float(total)) * 200.00

		lat1.append(y1)
		lng1.append(x1)
		size.append(size1)

	return {"lat_list": lat1, "lng_list": lng1, "size": size}


def drawPlot(shapeFilename, mapPoints, zipBorough, finalDots):
	
	dat = shapefile.Reader(shapeFilename)
	polygons = {'lat_list': [], 'lng_list': []}
	sizeScale = range(1, n+1)

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

		record_index += 1

	output_file("Problem3.html", title="shape and points example")
	TOOLS="pan,wheel_zoom,box_zoom,reset,previewsave"

	patches(polygons['lng_list'], polygons['lat_list'], \
            fill_color='#f7d779', line_color='black', \
            tools=TOOLS, plot_width = 1100, plot_height = 900, \
            title = 'Concetration of 311 Calls by %s Grids' % n)
	hold()

	scatter(finalDots['lng_list'], finalDots['lat_list'],
		fill_color='red',color='red', fill_alpha=.75, line_alpha=0.1, size=finalDots['size'], tools=TOOLS, plot_width=1100, plot_height=700, name="mapPoints")

	show()

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print 'Usage:'
        print sys.argv[0] + '1. [n] 2. [complaintsfile] 3. [zipboroughfile] 4. [shapefile]'
        print '\ne.g.: ' + sys.argv[0] + ' 311nyc.csv zip_borough.csv shape_data/ NYPD DOT'
    else:
    	n = int(sys.argv[1])
    	mapPoints = loadZipComplaints(sys.argv[2])
    	zipBorough = getZipBorough(sys.argv[3])
    	finalDots = getDots(mapPoints)
    	drawPlot(sys.argv[4], mapPoints, zipBorough, finalDots)

 
    	

