# TIME - O(n)


def peaksAndValleys(arr):
  
  for i,num in enumerate(arr):
    if i % 2 == 0 and arr[i] > arr[i+1]:
      arr[i+1],arr[i] = arr[i],arr[i+1]
    
    elif i % 2 and arr[i] <arr[i+1]:
      arr[i+1],arr[i] = arr[i],arr[i+1]
      
  return arr
  

# PYTHONIC

def peaksAndValleys(arr):
  for i in range(1,len(arr)):
    arr[i:i+2] = sorted(arr[i:i+2],reverse = i % 2)
  return arr
