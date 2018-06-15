
# TIME - O(m * n)
# SPACE - O(1)

def zeroMatrix(mat):
  ROW, COL = len(mat), len(mat[0])
  rowFlag, colFlag = False, False
    
  for i in range(1,ROW):
    for j in range(1,COL):
    
      if i == 0 and mat[i][j] == 0:
        rowFlag = True
        
      if j == 0 and mat[i][j] == 0:
        rowFlag = 0  
        
      if mat[i][j] == 0:
        mat[i][0] = 0
        mat[0][j] = 0
  
  for i in range(1,ROW):
    for j in range(1,COL):
      if mat[i][0] == 0 or mat[0][j] == 0:
        mat[i][j] = 0
  
  if rowFlag:
    for i in range(COL):
      mat[0][i] = 0
  
  if colFlag:
    for i in range(ROW):
      mat[i][0] = 0
  
  return mat
  
  
  
       
