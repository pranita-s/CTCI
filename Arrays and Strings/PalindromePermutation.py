
# TIME - O(n)
# SPACE - O(1)

def palindromePermutation(s):
  i , j = 0, len(s)-1
  s.lower()
  while i < j:
    while not s[i].isalnum() and i < j :
      i + = 1
    while not s[j].isalnum() and i < j :
      j - = 1
    if s[j] != s[i]:
      return False
  return True
