
class Tree:
	
	def __init__(self,data,left = None, right = None):
		self.data = data
		self.left = left
		self.right =right


def insert(root,key):
	if key <= root.data:
		if not root.left:
			root.left = Tree(key)
		else:
			insert(root.left,key)
	if key > root.data:
		if not root.right:
			root.right = Tree(key)
		else:
			insert(root.right,key)

def findSuccessor(node):
	while node.left:
		node = node.left
	return node.data


def delete(root,key):
	if not root:
		return None
	if key < root.data:
		root.left = delete(root.left,key)
	if key > root.data:
		root.right = delete(root.right,key)
	
	if not root.right:
		return root.left
	if not root.left:
		return root.right
	
	successor_val = findSuccessor(root.right)
	root.data = successor_val
	root.right = delete(root.right, successor_val)
	
	
	
	
