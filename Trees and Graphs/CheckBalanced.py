
# TIME - O(n)
# SPACE - O(H)

def checkBalanced(root):
	if not root:
		return True
		
	def helper(root):
		if not root:
			return 0
		left_height , right_height = helper(root.left), helper(root.right)		
		if left_height < 0 or right_height < 0 or abs(left_height,right_height) > 1:
			return -1
		return max(left_height,right_height)+1	
	return (helper(root) >= 0)
