
# TIME - O(m*n)
# SPACE - O(1)


def rotateMatrix(mat):
  mat_size = len(mat)-1
  for i in range(len(mat)//2):
    for j in range(i, mat_size - i):
      mat[i][j] , mat[~j][i] , mat[~i][~j], mat[j][~i]  = mat[~j][i] , mat[~i][~j] , mat[j][~i], mat[i][j]

  return mat
  
