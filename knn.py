import math

class Point:
    def __repr__(self):
        return "Point"
    def __str__(self):
        return "x1: %d\nx2: %d\ny1: %s\n" %(self.x1,self.x2,self.y1)
    def __init__(self, x1, x2, y1):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1

def dist(point1, point2):
    term1 = (point2.x2-point1.x1)**2
    term2 = (point2.x2-point1.x1)**2
    return math.sqrt(term1+term2)

#make sure that I actually understand what's going on here
#I mean, I wrote it, but the off-by-one error took a while to fix
def knn(k, point, pointset):
    nnset = [0 for i in range(k)]
    to_fill = 0
    for p in pointset:
        curdist = dist(point,p)
        #if the distance is less than the kth closest, put it in order
        if to_fill < len(nnset):
            #insert in the proper spot
            j = to_fill
            while j > 0 and curdist < nnset[j-1][1]:
                #shift up by one and decrement
                nnset[j] = nnset[j-1]
                j = j-1
            nnset[j] = (p,curdist)
            to_fill = to_fill + 1
        elif curdist < nnset[k-1][1]:
            insert((p,curdist),nnset)
    return nnset

#this doesn't seem to be doing what I want it to
def insert(point, pointset):
    #assume pointset is in decreasing order
    #assume the values in pointset are stored as (point, distance)
    #assume point is passed as (point,distance)
    hole = len(pointset)
    while hole > 0 and point[1] < pointset[hole-1][1]:
        hole = hole - 1
        if hole > 0:
            pointset[hole] = pointset[hole - 1]
    pointset[hole] = point

def guesstype(point,k,pointset):
    k_set = knn(k,point,pointset)
    types = {}
    for i in range(len(k_set)):
        curpoint = k_set[i][0]
        if curpoint.y1 in types:
            types[curpoint.y1] = types[curpoint.y1] + 1
        else:
            types[curpoint.y1] = 1
    alltypes = [(k,v) for (k,v) in types.items()]
    sorted(alltypes,key =lambda kv: kv[1])
    return alltypes[len(alltypes)-1][0]

points = [Point(1,4,"a"),Point(1,3,"a"),Point(-2,6,"b"),Point(3,5,"c"),Point(-1,7,"a"),Point(4,-3,"b")]
p = Point(2,3,"u")
