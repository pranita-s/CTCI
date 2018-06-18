
# TIME - O(n + km) (k times root matches the node in big tree)
# SPACE - O(log(n) + log(m))


def checkSubtree(tree1,tree2):
	if not tree1 or not tree2:
		return False
	if helper(tree1,tree2):
		return True
	else checkSubtree(tree1.left,tree2) or checkSubtree(tree1.right, tree2)

def helper(tree1,tree2):
	if not tree1 or not tree2:
		return False
	if not tree1 and not tree2:
		return True	
	return tree1.data == tree2.data and helper(tree1.left,tree2.right) and helper(tree1.right,tree2.right)
