
# TIME - O(l1 + l2)


def sortedMerge(A,B):
  index = len(A)+len(B)-1
  a = len(A)-1
  b = len(B)-1
  while a>=0 and b >=0:
    if A[a] > B[b]:
      A[index] = A[a]
      a -= 1
    else:
      A[index] = B[b]
      b -= 1
    index -=1
  
  while b >= 0:
    A[index] = B[b]
    index -= 1
    b -= 1
  
  return A
    
