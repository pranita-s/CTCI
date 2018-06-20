
# TIME = O(logn) (without duplicates)

def magicIndex(arr,left,right):
	if left < right:
		mid = (left+right)//2
		if mid == arr[mid]:
			return mid
		elif mid < arr[mid]:
			return magicIndex(arr,left,mid-1)
		elif mid > arr[mid]:
			return magicIndex(arr,mid+1,right)
	else:
		return False
		
		
# TIME - O(logn) (with duplicates)



def magicIndex(arr,start,end):
	if start <= end:
		mid = (start+end)//2
		if mid == arr[mid]:
			return mid
		
		left = min(mid-1,arr[mid])
		left_value = magicIndex(arr,start,left)
		if left_value:
			return left_value
		
		right = max(mid+1,arr[mid])
		right_value = magicIndex(arr,right,end)
		if right_value:
			return right_value
	else:
		return None
		
