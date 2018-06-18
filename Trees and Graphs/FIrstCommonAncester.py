

# TIME - O(n)
# SPACE - O(H)

import collections
def firstCommonAncester(root,node1,node2):
  
	status = collections.namedtuple('status',('ancester','count'))
	
	def helper(root,node1,node2):
		if not root:
			return status(None,0)
		
		left = helper(root.left,node1,node2)
		if left.count== 2:
			return status(root,2)
		
		right = helper(root.right,node1,node2)
		if right.count == 2:
			return status(root,2)
			
			
		totalCount = left.count + right.count + int(root is node1) + int(root is node2)
		return status(root if totalCount == 2 else None, totalCount)
		
