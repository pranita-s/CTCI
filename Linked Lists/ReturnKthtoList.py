
# TIME - O(n)
# SPACE - O(1)

def returnKthToList(head,k):
	slow = fast = head
	for _ in range(k-1):
		fast = fast.next
	while fast.next:
		slow, fast = slow.next, fast.next	
	return slow.val
