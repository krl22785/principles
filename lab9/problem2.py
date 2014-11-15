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

	filename = open(ComplaintFile)
	reader = csv.reader(filename, delimiter = ',')
	headers = reader.next()

	zipIndex = headers.index('Incident Zip')
	latColIndex = headers.index('Latitude')
	lngColIndex = headers.index('Longitude')
	agencyIndex = headers.index('Agency')

	lat = []
	lng = []

	complaintsbyzip = {}
	twoZip = [agency_one, agency_two] #use to select only two zips 

	for row in reader:
		agency = row[agencyIndex]

		if agency in twoZip:
			try:
				lat.append(float(row[latColIndex]))
				lng.append(float(row[lngColIndex]))
				zipcode = row[zipIndex]

				if zipcode in complaintsbyzip:
					if agency in complaintsbyzip[zipcode]:
						complaintsbyzip[zipcode][agency] += 1
					else:
						complaintsbyzip[zipcode][agency] = 1

				else:
					complaintsbyzip[zipcode] = {}
					complaintsbyzip[zipcode][agency] = 1
			except:
				pass
		else:
			pass

	return {'zip_complaints': complaintsbyzip}

def filterMapPoints(mapPoints):
	twoZip = [agency_one, agency_two]

	for i in mapPoints['zip_complaints'].values():
		if twoZip[0] not in i:
			i[twoZip[0]] = 0
		elif twoZip[1] not in i:
			i[twoZip[1]] = 0
		else:
			pass

	return mapPoints

def getZipBorough(zipBoroughFilename):

	filename = open(zipBoroughFilename)
	reader = csv.reader(filename, delimiter = ',')
	reader.next()

	return {row[0]: row[1] for row in reader}

def drawPlot(shapeFilename, mapPoints, zipBorough):
	
	dat = shapefile.Reader(shapeFilename)
	polygons = {'lat_list': [], 'lng_list': [], 'color_list' : []} #, 'zip': []} #, 'top_agency': [], 'agency_count': []}

	colorscale = ["#203c7f", "#2e4176", "#3c456e", "#4a4a65", "#574e5d", "#655354", "#73584c", "#815c43", "#8f613b", "#9d6632", "#aa6a2a", "#b86f21", "#c67319", "#d47810"]
	#colorscale = ["#F1EEF6", "#D4B9DA", "#C994C7", "#DF65B0", "#DD1C77", "#980043"]

	
	record_index = 0

	for r in dat.iterRecords():
		currentZip = r[0]

		#keeps only ny area zips
		if currentZip in zipBorough:
			shape = dat.shapeRecord(record_index).shape
			points = shape.points

			lngs = [p[0] for p in points]
			lats = [p[1] for p in points]

			polygons['lng_list'].append(lngs)
			polygons['lat_list'].append(lats)

			if currentZip in mapPoints['zip_complaints']:
				colorIndex = (mapPoints['zip_complaints'][currentZip][agency_one] / float(sum(mapPoints['zip_complaints'][currentZip].values()))) * (len(colorscale) - 1)
				color = colorscale[int(colorIndex)]
			else:
				color = 'white'

			polygons['color_list'].append(color)
				
		record_index += 1	

	output_file("shapeAndPoints_test1.html", title = "NYC by Zip" )
	TOOLS="pan,wheel_zoom,box_zoom,reset,previewsave,resize,hover"

	patches(polygons['lng_list'], polygons['lat_list'], \
            fill_color=polygons['color_list'], line_color='gray', \
            tools=TOOLS, plot_width = 900, plot_height = 700, \
            title = 'Color Code Agency')

	hold()

	x, y = -73.625, 40.55
	for i, area in enumerate(colorscale):
		if i == 0: 
			rect([x], [y], color=colorscale[i], width=0.025, height=.025)
			text([x], [y], text=agency_one, angle=0, text_font_size="6pt", text_align="center", text_baseline="middle")
			y = y + .025
		elif i == (len(colorscale) - 1):
			rect([x], [y], color=colorscale[i], width=0.025, height=.025)
			text([x], [y], text=agency_two, angle=0, text_font_size="6pt", text_align="center", text_baseline="middle")
			y = y + .025
		else:
			rect([x], [y], color=colorscale[i], width=0.025, height=.025)
			text([x], [y], text="" , angle=0, text_font_size="6pt", text_align="center", text_baseline="middle")
			y = y + .025
	show()


if __name__ == '__main__':
    if len(sys.argv) != 6:
        print 'Usage:'
        print sys.argv[0] + '1. 311nyc.csv 2. zip_borough.csv 3. shape_data/nyshape.shp 4. agency one 5. agency two'
        print '\ne.g.: ' + sys.argv[0] + ' 311nyc.csv zip_borough.csv shape_data/ NYPD DOT'
    else:
    	agency_one = str(sys.argv[4])
    	agency_two = str(sys.argv[5])
        mapPoints1 = loadZipComplaints(sys.argv[1])
        mapPoints = filterMapPoints(mapPoints1) ## HEHREHEHRE 
        zipBorough = getZipBorough(sys.argv[2])
        drawPlot(sys.argv[3], mapPoints, zipBorough)








