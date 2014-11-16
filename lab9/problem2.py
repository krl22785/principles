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

	complaintsbyzip = {}
	twoZip = [agency_one, agency_two] #use to select only two zips 

	for row in reader:
		agency = row[agencyIndex]
		if agency in twoZip:
			try:
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

	#for line in mapPoints['zip_complaints']:
	#	one = (mapPoints['zip_complaints'][line][agency_one] / float(sum(mapPoints['zip_complaints'][line].values())))
	#	two = (mapPoints['zip_complaints'][line][agency_two] / float(sum(mapPoints['zip_complaints'][line].values())))
	#	print "%s: %s" % (agency_one, one) + "%s: %s" % (agency_two, two)
	

def getZipBorough(zipBoroughFilename):

	filename = open(zipBoroughFilename)
	reader = csv.reader(filename, delimiter = ',')
	reader.next()

	return {row[0]: row[1] for row in reader}

def drawPlot(shapeFilename, mapPoints, zipBorough):
	
	dat = shapefile.Reader(shapeFilename)
	polygons = {'lat_list': [], 'lng_list': [], 'color_list' : [], 'agency_one_perc': [], 'agency_two_perc': []}
	colorscale = ["#203c7f", "#2e4176", "#3c456e", "#4a4a65", "#574e5d", "#655354", "#73584c", "#815c43", "#8f613b", "#9d6632", "#aa6a2a", "#b86f21", "#c67319", "#d47810"]
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
				o = (mapPoints['zip_complaints'][currentZip][agency_one] / float(sum(mapPoints['zip_complaints'][currentZip].values())))
				t = (mapPoints['zip_complaints'][currentZip][agency_two] / float(sum(mapPoints['zip_complaints'][currentZip].values())))

				one = o * 100
				two = t * 100

				colorIndex = (mapPoints['zip_complaints'][currentZip][agency_one] / float(sum(mapPoints['zip_complaints'][currentZip].values()))) * (len(colorscale) - 1)
				color = colorscale[int(colorIndex)]
			else:
				color = 'white'

			polygons['color_list'].append(color)
			polygons['agency_one_perc'].append(one)
			polygons['agency_two_perc'].append(two)
				
		record_index += 1	


		source = ColumnDataSource(
        data=dict(
            long=polygons['lng_list'],
            lat = polygons['lat_list'],
            col=polygons['color_list'],
            one= polygons['agency_one_perc'],
            two= polygons['agency_two_perc'],
        )
    )

	output_file("Problem2.html", title = "NYC by Zip" )
	TOOLS="pan,wheel_zoom,box_zoom,reset,previewsave,resize,hover"

	patches(polygons['lng_list'], polygons['lat_list'], source = source,\
            fill_color=polygons['color_list'], line_color='white', \
            tools=TOOLS, plot_width = 1100, plot_height = 900, \
            title = '%s vs %s Across Zip Codes' % (agency_one, agency_two))

	hover = curplot().select(dict(type=HoverTool))
	hover.tooltips = OrderedDict([
		("%s " % agency_one, "@one"),
		("%s " % agency_two, "@two"),
	])

	hold()

	x, y = -73.625, 40.55
	for i, area in enumerate(colorscale):
		if i == 0: 
			rect([x], [y], color=colorscale[i], width=0.025, height=.025)
			text([x], [y], text=agency_two, angle=0, text_font_size="8pt", text_align="center", text_baseline="middle", text_color = "white")
			y = y + .025
		elif i == (len(colorscale) - 1):
			rect([x], [y], color=colorscale[i], width=0.025, height=.025)
			text([x], [y], text=agency_one, angle=0, text_font_size="8pt", text_align="center", text_baseline="middle", text_color = "black")
			y = y + .025
		else:
			rect([x], [y], color=colorscale[i], width=0.025, height=.025)
			text([x], [y], text="" , angle=0, text_font_size="8pt", text_align="center", text_baseline="middle")
			y = y + .025
	show()


if __name__ == '__main__':
    if len(sys.argv) != 6:
        print 'Usage:'
        print sys.argv[0] + '1. [complaints] 2. [zip_borough] 3. [shapefile] 4. [agency 1] 5. [agency 2]'
        print '\ne.g.: ' + sys.argv[0] + ' 311nyc.csv zip_borough.csv shape_data/nyshape.shp NYPD DOT'
    else:
    	agency_one = str(sys.argv[4])
    	agency_two = str(sys.argv[5])
        mapPoints1 = loadZipComplaints(sys.argv[1])
        mapPoints = filterMapPoints(mapPoints1) ## HEHREHEHRE 
        zipBorough = getZipBorough(sys.argv[2])
        drawPlot(sys.argv[3], mapPoints, zipBorough)








