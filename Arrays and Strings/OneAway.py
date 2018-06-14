
# TIME - O(n)
# SPACE - O(1)

def OneAway(s,t):
  minLength = min(len(s),len(t))
  for i in range(minLength):
    if s[i] != t[j]:
      return s[i+1:] == t[i+1:]
    elif len(s) > len(t):
      return s[i+1:] == t[i:]
    else:
      return s[i:] == t[i+1:]
 
  return abs(len(s) - len(t)) == 1
