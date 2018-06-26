class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

class Line:

    def __init__(self,point1,point2):
        self.m = (point2.y - point1.y)/((point2.x-point1.x))
        self.c = point2.y - self.m * point2.x

def findIntersection(line1,line2):
    if line1.m == line2.m and line1.c == line2.c:
        print("Same line")
    elif line1.m == line2.m and line1.c != line2.c:
        print("Will never intersect")
    else:
        x = (line1.c - line2.c)/(line2.m - line1.m)
        y = line1.m * x + line1.c
    return (x,y)


if __name__ == '__main__':
    line1 = Line(Point(0,1),Point(5,6))
    line2 = Line(Point(4,-1),Point(-1,4))
    print(findIntersection(line1,line2))
