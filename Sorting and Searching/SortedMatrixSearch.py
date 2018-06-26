
# TIME - O(R+C)

def sortedMatrixSearch(grid,key):
  R = len(grid)
  C = len(grid[0])
  row = 0
  col = C-1
  while r < R and col >= 0:    
    if grid[row][col] == key:
      return True
    elif grid[row][col] > key:
      col -= 1
    else:
      row += 1
  return False
