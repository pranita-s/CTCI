
# TIME - O(n)
# SPACE - O(1)

def findIntersection(l1,l2):
	size1, size2 = findSize(l1), findSize(l2)
	
	if size1 < size2:
		l1, l2 = l2, l1
	
	for _ in range(size1 - size2):
		l1 = l1.next
	
	while l1 != l2:
		l1, l2 = l1.next, l2.next
	
	return l1
