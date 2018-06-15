
# TIME - O(n)
# SPACE - O(1)

def findSize(head):
	size = 0
	while head:
		size += 1
		head = head.next
	return size

def findIntersection(l1,l2):
	size1, size2 = findSize(l1), findSize(l2)
	
	if size1 < size2:
		l1, l2 = l2, l1
	
	for _ in range(size1 - size2):
		l1 = l1.next
	
	while l1 and l2 and l1 is not l2:
		l1, l2 = l1.next, l2.next
	
	return l1
