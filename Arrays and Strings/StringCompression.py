
# TIME - O(n)
# SPACE - O(1)


def stringCompress(s):  
  result = ''
  i = 0
  while i < len(s):
    curr = s[i]
    count = 0
    while curr == s[i]:
      i + = 1
      count + = 1
    result += (curr + str(count))
  
  return result if len(result) < len(s) else s
      
  
