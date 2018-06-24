 # TIME - O(n)
 
 
 
 def search(nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

            else:
                if nums[right] < target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
