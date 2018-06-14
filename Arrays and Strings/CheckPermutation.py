

# TIME - O(n)
# SPACE - O(n)


def checkPermutation(s,t):
  if len(s) != len(t):
    return False
  
  lookup = {}
  for char in s:
    lookup[char] = lookup.get(char,0) + 1
  
  for char in t:
    lookup[char] = lookup.get(char,0) - 1
    if lookup[char] < 0 :
      return False
  
  return True
  
