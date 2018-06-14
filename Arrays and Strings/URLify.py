
# TIME - O(n)
# SPACE - O(1)

def URLify(s):
  splitted = s.split()
  return '%20'.join(splitted)
