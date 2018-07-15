# TIME - O(R * C)

def isvalid(matrix,row,col):
  if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
    return True
  return False


def water(matrix,row,col):
  if matrix[row][col] != 0:
    return 0
  else:
    matrix[row][col] -= 1
    total = 1
    for i in range(-1,2):
      for j in range(-1,2):
        if isvalid(matrix,row+i,col+j):
          total += match(matrix,row+i,col+j)
    return total
  


def pondSize(matrix):
  res = []
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if matrix[i][j] == 0:
        res.append(water(matrix,i,j))
  return res
