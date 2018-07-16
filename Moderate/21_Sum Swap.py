# TIME - O(n + m)

def sumSwap(nums1,nums2):
  sum1, sum2 = sum(nums1), sum(nums2)
  if sum1 > sum2:
    nums1, nums2 = nums2, nums1
  
  for i,num in enumerate(nums2):
    d[num] = i
  
  for i,num in enumerate(nums1):
    if num + diff in d:
      return (d[num+diff],i)
  
    
