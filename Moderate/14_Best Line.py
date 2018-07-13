# TIME - O(n ** 2)

import collections

class Line:

  def __init__(self,m,c):
    self.m = m
    self.c = 0
  
  def __repr__(self):
    return "{0}*x + {1}"%(self.m,self.c)

def getLine(p1,p2):
  m = 0 
  if p1[0] != p2[0]:
    m = (p1[1] - p2[1])/(p1[0] - p2[0])
  intercept = p1[1] - m * p1[0] 
  return (m,intercept)
  
def bestLine(points):
  result = None
  maxPoints  = 0
  d = collections.defaultdict(int)
  for i,p in points:
    for j in range(i,len(points)):
      line = getLine(p,points[j])
      d[line] += 1
      if maxPoints < d[line]:
        maxPoints = d[line]
        result = line
  return result



pointList = [(0,0), (1,1), (3,5), (-2,-2), (9,9), (6,7), (-1,3)]
print(bestLine(pointList))
