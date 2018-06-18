
# TIME  - O(H)
# SPACE - O(1)


def FCA_parentPointers(root,node1,node2):
	
	def getDepth(node):
		d=0
		while node:
			d += 1
			node = node.parent
	
	dep1,dep2 = getDepth(node1), getDepth(node2)
	
	if dep1 < dep2:
		node1, node2 = node2, node1
	
	for _ in range(abs(dep1-dep2)):
		node1 = node1.parent
		
	
	while node1 is not node2:
		node1, node2 = node1.parent, node2.parent
	
	return node1
	
