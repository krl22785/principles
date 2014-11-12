# Functions for students to implement.

naive = []
def buildNaive(points, n):
    #global naive
    del naive[:]

    for i in points:
        naive.append(list(i))

    return None

onedim = []
def buildOneDim(points,n):
    #global onedim
    del onedim[:] #erasing previous data
    
    #onedim = [[]for j in range(1,n+1)]

    for j in range(1,n+1):
        onedim.append([])

    for i in points:
        index = int(i[0] * n)
        onedim[index].append(i)

    return None

twodim = []
def buildTwoDim(points,n):
    #global twodim
    del twodim[:] #erasing previous data
    #your code here

    for j in range(0, n):
        twodim.append([])
    
    for i, j in enumerate(twodim):
        for k in range(0, n):
            twodim[i].append([])


    for i in points:
        index_x = int(i[0]*n)
        index_y = int(i[1]*n)

        twodim[index_x][index_y].append(i)

    return None
#    print twodim


def queryNaive(x0, y0, x1, y1):
    count = 0
    for i in naive:
        if i[0] > x0 and i[0] < x1 and i[1] > y0 and i[1] < y1:
            count = count + 1 
        else: 
            pass 

    return count


def queryOneDim(x0, y0, x1, y1):
    count = 0

    start = int(x0 * len(onedim))
    end = int(x1 * len(onedim)) + 1

    for item in onedim[start:end]:
        for k in item:
            if k[0] >= x0 and k[0] <= x1 and k[1] >= y0 and k[1] <= y1:
                count = count + 1 
            else:
                pass
    
    return count

def queryTwoDim(x0, y0, x1, y1):
    count = 0

    startx = int(x0 * len(twodim))
    endx = int(x1 * len(twodim)) + 1

    starty = int(x0 * len(twodim))
    endy = int(x1 * len(twodim)) + 1

    for item in twodim[startx:endx]:
        for innerItem in item[starty:endy]:
    
            for point in innerItem:
                if point[0] >= x0 and point[0] <= x1 and point[1] >= y0 and point[1] <= y1:
                    count = count + 1
                else:
                        pass
                
                

    return count
    #print test




#points = [(0.01,0.01),(0.25,0.29),(0.22,0.35),(0.27,0.78),(0.61,0.42),(0.72,0.66),(0.48,0.43),(0.00,0.28),(0.26,0.32),(0.88,0.72)]
#buildNaive(points, 0)
#queryNaive(0,0,.45,.45)
#buildOneDim(points, 4)
#queryOneDim(.2,.2,.9,.9)
#buildTwoDim(points, 4)
#queryTwoDim(0,0,.7,.7)

   #if x1 > 1:
    #    start = int(x0 * len(twodim))
     #   end = int(len(twodim)) - 1
    #elif x1 < 0:
    #    count = 0
    #else:
     #   start = int(x0 * len(twodim))
     #   end = int(x1 * len(twodim))

