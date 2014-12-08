import sys
import time
import csv
import math
from scipy import spatial

def loadRoadNetworkIntersections(filename):
    #bbox around Manhattan
    latBounds = [40.6,40.9]
    lngBounds = [-74.05,-73.90]
    #
    listWithIntersectionCoordinates = []
    f = open(filename)
    reader = csv.reader(f, delimiter=' ')
    for l in reader:
        try:
            point = [float(l[0]),float(l[1])]
            if latBounds[0] <= point[0] <= latBounds[1] and lngBounds[0] <= point[1] <= lngBounds[1]:
                listWithIntersectionCoordinates.append(point)
        except:
            print l

    return listWithIntersectionCoordinates

def loadTaxiTrips(filename):
    #load pickup positions
    loadPickup = True
    #bbox around Manhattan
    latBounds = [40.6,40.9]
    lngBounds = [-74.05,-73.90]
    #
    f = open(filename)
    reader = csv.reader(f)
    header = reader.next()
    #
    if loadPickup:
        lngIndex = header.index(' pickup_longitude')
        latIndex = header.index(' pickup_latitude')
    else:
        latIndex = header.index(' dropoff_latitude')
        lngIndex = header.index(' dropoff_longitude')
    result = []
    for l in reader:
        try:
            point = [float(l[latIndex]),float(l[lngIndex])]
            if latBounds[0] <= point[0] <= latBounds[1] and lngBounds[0] <= point[1] <= lngBounds[1]:
                result.append(point)

        except:
            print l
    return result

def naiveApproach(intersections, tripLocations):
    counts = {}
    startTime = time.time()

    # cnt = 1
    for trip in tripLocations:
        x1 = trip[0]
        y1 = trip[1]

        # print 'counting ' +  str(cnt)
        # cnt += 1

        var = +1
        key = None

        for i, intersection in enumerate(intersections):

            x2 = intersection[0]
            y2 = intersection[1]

            d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

            if d < var:
                var = d
                key = i
            else:
                pass

        if key in counts:
            counts[key] += 1
        else:
            counts[key] = 1

    #print sorted(counts.items(), key=lambda(k): k)[0:5]
    endTime = time.time()
    print 'The naive computation took', (endTime - startTime), 'seconds'
    return counts

def kdtreeApproach(intersections, tripLocations):
    counts = {}
    startTime = time.time()

    lat = []
    lon = []

    for intersection in intersections:
        lat.append(intersection[0])
        lon.append(intersection[1])

    tree = spatial.KDTree(zip(lat, lon))

    ind = tree.query(tripLocations)[1]

    for i in ind:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

    #print sorted(counts.items(), key=lambda(k): k)[0:5]
    endTime = time.time()
    print 'The kdtree computation took', (endTime - startTime), 'seconds'
    return counts

def plotResults(intersections, counts):
    #TODO: intersect the code to plot here
    print 'TODO'

if __name__ == '__main__':

    roadIntersections = loadRoadNetworkIntersections(sys.argv[1])
    tripPickups = loadTaxiTrips(sys.argv[2])

    naiveCounts = naiveApproach(roadIntersections,tripPickups)
    kdtreeCounts = kdtreeApproach(roadIntersections,tripPickups)

    ##plotResults(roadIntersections,kdtreeCounts)
