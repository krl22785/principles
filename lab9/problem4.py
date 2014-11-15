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
	zipIndex = headers.index('Incident Zip')

	complaintsperzip = {}

	for row in reader:
		try:
			zipcode = row[zipIndex]

			if zipcode in complaintsperzip:
				complaintsperzip[zipcode] += 1
			else:
				complaintsperzip[zipcode] = 1
		except:
			pass 

	return {'zip_complaints': complaintsperzip}

	#bbox = shape.bbox
def getZipBorough(zipBoroughFilename):

	filename = open(zipBoroughFilename)
	reader = csv.reader(filename, delimiter = ',')
	reader.next()

	return {row[0]: row[1] for row in reader}

def drawPlot(shapeFilename, mapPoints, zipBorough):
	#print finalDots['size']
	
	dat = shapefile.Reader(shapeFilename)
	polygons = {'lat_list': [], 'lng_list': [], "size": [], "lat_bbox": [], "lng_bbox": []}

	record_index = 0
	for r in dat.iterRecords():
		currentZip = r[0]

		if currentZip in zipBorough:
			shape = dat.shapeRecord(record_index).shape

			points = shape.points
			lngs = [p[0] for p in points]
			lats = [p[1] for p in points]

			bbox = shape.bbox

			lats_box = float((bbox[1] + bbox[3])/2)
			lngs_box = float((bbox[0] + bbox[2])/2)

			polygons['lng_bbox'].append(lngs_box)
			polygons['lat_bbox'].append(lats_box)
			polygons['lng_list'].append(lngs)
			polygons['lat_list'].append(lats)

			if currentZip in mapPoints['zip_complaints']:
				complaints = mapPoints['zip_complaints'][currentZip]
				size = math.log(complaints, 2)

			polygons['size'].append(size)

		record_index += 1


	output_file("q4.html", title="shape and points example")
	TOOLS="pan,wheel_zoom,box_zoom,reset,previewsave"

	patches(polygons['lng_list'], polygons['lat_list'], \
            fill_color='#d17d65', line_color='gray', \
            tools=TOOLS, plot_width = 900, plot_height = 700, \
            title = 'Concetration of 311 Calls')
	hold()

	scatter(polygons['lng_bbox'], polygons['lat_bbox'],
		fill_color='red',color='red', fill_alpha=1.0, line_alpha=0.1, size=polygons['size'], tools=TOOLS, plot_width=1100, plot_height=700, name="mapPoints")

	show()




if __name__ == '__main__':
    if len(sys.argv) != 4:
        print 'Usage:'
        print sys.argv[0] + 'n [complaintsfile] [zipboroughfile] [shapefile]'
        print '\ne.g.: ' + sys.argv[0] + ' 311nyc.csv zip_borough.csv shape_data/ NYPD DOT'
    else:
    	mapPoints = loadZipComplaints(sys.argv[1])
    	zipBorough = getZipBorough(sys.argv[2])
    	drawPlot(sys.argv[3], mapPoints, zipBorough)