
def subtract(a,b):
  return a + (-b)
 
def multiply(a,b):
  first, second = a,b
  if a < b:
    first,second = b,a
  answer = 0
  for _ in range(abs(second)):
    answer += first
  
  return answer if second > 0 else -answer

def divide(a,b):
  
  D = abs(a)
  d = abs(b)
  q = 0
  while D >= d:
    D -= d
    q += 1
  
  negative = int(a<0) + int(b<0)
  if negative == 1:
    return -q
  else:
    return q
