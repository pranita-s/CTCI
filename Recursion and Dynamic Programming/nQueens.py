# TIME - O(n!)

def nQueens(n):
  def queenPlacement(row):    
    if row ==n:
      result.append(list(col_placement))
      return    
    for col in range(n):      
      if all(abs(col-c) not in (0,row-i) for i,c in enumerate(col_placement[:row])):
        col_placement[row] = col
        queenPlacement(row+1)
        
  result = []
  col_placement = [0] * n
  queenPlacement(0)
  return result
 
print(nQueens(4))
