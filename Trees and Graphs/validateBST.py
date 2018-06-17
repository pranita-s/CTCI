
# TIME - O(n)
# SPACE - O(H)


def validateBST(root):
	if not root:
		return True
	
	def helper(root, lower, upper):
		if not root:
			return True
		
		return lower <= root.data <= upper and helper(root.left, lower, root.data) and helper(root.right, root.data, upper)
		
	return helper(root, -float('inf'), float('inf'))
