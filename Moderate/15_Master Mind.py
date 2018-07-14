# TIME - O(n)

import collections
def findHits(solution, guess):
  hits = 0
  phits = 0
  sol = collections.defaultdict(int)
  
  for i, char in enumerate(guess):
    if solution[i] == char:
      hits += 1
    else:
      sol[solution[i]] += 1
  
  for i, char in enumerate(guess):
    if solution[i] != char and sol[solution[i]] > 0:
      phits += 1
      sol[solution[i]] -= 1
  
  return (hits,phits)


solution = "RGBY"
guess = "GGRR"
print(getHits(solution, guess))
print(getHits("RGGB", "YRGB"))
