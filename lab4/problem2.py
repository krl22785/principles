
def searchGreaterNotSorted(L, v):
  #return -1
  cnt = 0 
  for line in L:
    if line > v:
      cnt = cnt + 1
    else:
      pass 
  
  print cnt


def searchGreaterSorted(L, v):
  #print L
  n = 0
  cnt = 0
  for line in L:
    if line <= v:
      n = n + 1
    else:
      cnt = len(L[n:])
      break
  print cnt

def searchGreaterBinSearch(L, v):

  hi = len(L)
  lo = 0 

  while lo < hi: 

    mid = (hi + lo)/2

    print "new list: " + str(lo) + " " + str(mid) + " " + str(hi)

    if L[mid] == v:
      break

    elif L[mid] < v:
      lo = mid + 1
    else:
      hi = mid

  if lo < hi:

    while mid < len(L) and L[mid] == v:
      mid += 1

    print len(L) - mid

  else:

    print len(L) - hi





def searchInRange(L, v1, v2):
  
  cnt = 0 
  x = None
  y = None

  if v2 == L[len(L)-1]:
    #n = L.count(v2) 
    x = searchGreaterBinSearch(L, v1)
    cnt = x
  else:
    x = searchGreaterBinSearch(L, v1)
    y = searchGreaterBinSearch(L, v2)
    cnt = x - y 
  
  return cnt

List = [1,1,3,4,5,5,11,13,14,15,16,17,20,22,24,25,26,27,28,30,31,31,32,33,34,44,56,78,99]
searchGreaterBinSearch(List, 99)




