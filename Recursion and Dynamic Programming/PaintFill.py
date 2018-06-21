# TIME - O(R * C)

def PaintFill(grid,r,c,color):
  if grid[r][c] != color:
    PaintFillHelper(grid,r,c,grid[r][c],color)
  return grid
  
def PaintFillHelper(grid,r,c,oldColor,newColor):
  if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
    return
  
  if grid[r][c] == oldColor:
    grid[r][c] = newColor
    PaintFillHelper(grid,r-1,c,oldColor,newColor)
    PaintFillHelper(grid,r+1,c,oldColor,newColor)
    PaintFillHelper(grid,r,c-1,oldColor,newColor)
    PaintFillHelper(grid,r,c+1,oldColor,newColor)
 
grid = [[1,1,1],[1,1,0],[1,0,1]]
print(Paintfill(grid,1,1,2))
