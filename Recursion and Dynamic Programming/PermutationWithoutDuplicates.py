
# TIME - O(n * n!)  (n! permutations and we spend O(n) time to store each one)

result = []
def permute(s):
  permuteHelper('',s)
  print(result)

def permuteHelper(soFar, remaining):
  if remaining == '':
    result.append(soFar)
  else:
    for i in range(len(remaining)):
      permuteHelper(soFar+remaining[i], remaining[:i]+remaining[i+1:])

permute('abc')

#########################################################################################

def permute(s):  
  def permuteHelper(i):   
      if i == len(s)-1:
        result.append(s)      
      
      for i in range(j,len(s)):
        s[i] , s[j] = s[j], s[i]
        permuteHelper(i+1)
        s[i], s[j] = s[j], s[i]
       
  result = []
  permuteHelper(0)
  return result
