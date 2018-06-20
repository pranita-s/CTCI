# TIME - O(n!)

def permute(A):
 
  def permuteHelper(soFar, remainingLength):
    if remainingLength == 0:
      result.append(soFar)
     
    for key in d:
      if d[key] > 0:
        d[key] -= 1
        permuteHelper(soFar + [key], remainingLength-1)
        d[key] += 1
  
  
  result = []
  d = {}
  for char in A:
    d[char] = d.get(char,0) + 1
  permuteHelper([],len(A))
  return result
