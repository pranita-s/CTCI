# TIME - O(n)
# SPACE - O(n)

class ListNode:

	def __init__(self,data=0,next=None)
		self.data = data
		self.next = next
		
	def addToLL(self,val):
		if self.next = None:
			self.next = ListNode(val)
		else:
			self.addToLL(self.next, val)

class Tree:

	def __init__(self,data,left = None,right = None):
		self.data = data
		self.left = left
		self.right = right
	
	
	
	def createLinkedLists(self, root, level, lists = {}):
		if root:
			if level not in lists:
				lists[level] = ListNode(root.data)
			else:
				lists[level].addToLL(root.data)
			self.createLinkedList(root.left,level+1,lists)
			self.createLinkedList(root.right,level+1,lists)
		return lists
		
		
		
