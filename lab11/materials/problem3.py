import sys
import time
import csv
from scipy import spatial
import math
import itertools

def loadTaxiTripsPickupAndDropoffs(filename):
    #bbox around Manhattan
    latBounds = [40.6,40.9]
    lngBounds = [-74.05,-73.90]
    #
    f = open(filename)
    reader = csv.reader(f)
    header = reader.next()
    #
    lngIndex0 = header.index(' pickup_longitude')
    latIndex0 = header.index(' pickup_latitude')
    latIndex1 = header.index(' dropoff_latitude')
    lngIndex1 = header.index(' dropoff_longitude')
    result = []
    for l in reader:
        try:
            point0 = [float(l[latIndex0]),float(l[lngIndex0])]
            point1 = [float(l[latIndex1]),float(l[lngIndex1])]
            if latBounds[0] <= point0[0] <= latBounds[1] and lngBounds[0] <= point0[1] <= lngBounds[1] and latBounds[0] <= point1[0] <= latBounds[1] and lngBounds[0] <= point1[1] <= lngBounds[1]:
                result.append([point0[0],point0[1],point1[0],point1[1]])
        except:
            print l
    return result

def naiveApproach(tripLocations, startRectangle, endRectangle):
    indices = []
    startTime = time.time()

    for i, pts in enumerate(trips):

        x1 = pts[0]
        y1 = pts[1]
        x2 = pts[2]
        y2 = pts[3]

        if x1 >= startRectangle[0][0] and x1 <= startRectangle[0][1] and y1 >= startRectangle[1][0] and y1 <= startRectangle[1][1]:
            if x2 >= endRectangle[0][0] and x2 <= endRectangle[0][1] and y2 >= endRectangle[1][0] and y2 <= endRectangle[1][1]:

                indices.extend([i])
            else:
                pass
        else:
            pass

    print indices
    endTime = time.time()
    print 'The naive computation took', (endTime - startTime), 'seconds'
    return indices

def kdtreeApproach(tripLocations, startRectangle, endRectangle):
    indices = []
    startTime = time.time()

    #find radius and centroid for start rectangle
    start_lat = startRectangle[0][1] - startRectangle[0][0]
    start_lon = startRectangle[1][1] - startRectangle[1][0]
    radius = math.sqrt((start_lat/2) **2 + (start_lon/2) ** 2)

    centroid = ((startRectangle[0][0] + start_lat/2), (startRectangle[1][0] + start_lon/2))

    #Build Tree
    tree = spatial.KDTree([(i[0],i[1]) for i in tripLocations])
    ind = tree.query_ball_point(centroid, radius)

    for i in ind:
        if tripLocations[i][0] <= 40.721319 and tripLocations[i][0] >= 40.713590 and tripLocations[i][1] >= -74.011116 and tripLocations[i][1] <= -73.994722:
            if tripLocations[i][2] <= 40.748398 and tripLocations[i][2] >= 40.744532 and tripLocations[i][3] >= -74.003005 and tripLocations[i][3] <= -73.990881:
                indices.extend([i])
            else:
                pass
        else:
            pass


    endTime = time.time()
    print 'The kdtree computation took', (endTime - startTime), 'seconds'
    return indices

def extraCredit(tripLocations, startPolygon, endPolygon):
    #indices is a list that should contain the indices of the trips in the tripLocations list
    #which start in the startPolygon region and end in the endPolygon region
    indices = []

    #TODO: insert your code here. You should build the kdtree and use it to query the closest
    #      intersection for each trip

    return indices    

if __name__ == '__main__':
    #these functions are provided and they already load the data for you
    trips             = loadTaxiTripsPickupAndDropoffs(sys.argv[1])
    #
    startRectangle    = [[40.713590,40.721319],[-74.011116,-73.994722]] #[[minLat,maxLat],[minLng,maxLng]]
    endRectangle      = [[40.744532,40.748398],[-74.003005,-73.990881]] #[[minLat,maxLat],[minLng,maxLng]]

    naiveIndices = naiveApproach(trips,startRectangle, endRectangle)

    kdtreeIndices = kdtreeApproach(trips,startRectangle, endRectangle)
