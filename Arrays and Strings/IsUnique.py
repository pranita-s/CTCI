
## Time - O(n) 
## Space - O(1)


def isUnique(s):
  status = 0
  for char in s:
    temp = ord(char)-ord('a')
    if status & (1<<temp):
      return False
    status |= (1<<temp)
   
   return True
    
  
