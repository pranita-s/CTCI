# TIME - O(1)

def findBisectinLine(sq1,sq2):
  center1,center2 = sq1.center,sq2.center
  xdiff = center1.x - center2.x
  ydiff = center1.y - center2.y
  if xdiff == 0:
    if ydiff == 0:
      return lambda x:center1.y
    else:
      return None
    
    slope = float(ydiff)/xdiff
    intercept = center1.y - slope * center1.x
    return lambda x: slope * x + intercept
  

class Square:
  
  def __init__(self,center,sq_length,rotation):
    self.center = center
    self.sq_length = sq_length
    self.rotation = rotation


class Point:
  
  def __init__(self,x,y):
    self.x = x
    self.y = y



sq1 = Square(Point(2, 4.5), 2, 15)
sq2 = Square(Point(7, 4.5), 3, 45)
line = bisect_squares(sq1, sq2)
print(line(0))
print(line(11))
