# TIME - O(n)

def subSort(arr):

  _min, _max = float('inf'), -float('inf')
  left, right = 0 , len(arr)-1
  
  for i, num in enumerate(arr):
    _min = min(_min, arr[-(i+1)])
    _max = max(_max, arr[i])
    if _max != arr[i]:
      left = i
    if _min != arr[-(i+1)]:
      right = len(arr) - i - 1
    
  if left == 0:
    return 0
  return (left-right+1)
