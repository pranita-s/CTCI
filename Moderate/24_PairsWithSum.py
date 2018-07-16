# TIME - O(nlogn)

def findPairs(nums,target):
  result = []
  nums.sort()
  left,right = 0, len(nums)-1
  while left < right:
    summ = nums[left] + nums[right]
    if summ == target:
      result.append((nums[left],nums[right]))
    elif summ < target:
      left += 1
    else:
      right -= 1
  
  return result
   

# TIME - O(n)

def findPairs(nums,target):
  n_set = set(nums)
  result = set()
  for num in nums:
    if target - num in n_set:
      result.add((num,target-num))
      n_set.remove(num)
  
  return list(result)

  
  
