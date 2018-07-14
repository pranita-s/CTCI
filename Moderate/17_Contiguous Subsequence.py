# TIME - O(n)

def contiguousSubsequence(arr):
  sum = 0
  maxSum = -float('inf')
  
  for i, num in enumerate(arr):
    sum += num
    if maxSum < sum:
      maxSum = sum
    elif sum < 0:
      sum = 0
  
  return maxSum
    
