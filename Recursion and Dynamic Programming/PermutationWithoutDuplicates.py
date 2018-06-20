
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


