
# TIME - O(n)
# SPACE - O(1)


def deleteMiddleNode(head):
	slow = head
	fast = head.next
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next	
	slow.val = slow.next.val
	slow.next = slow.next.next
	return head
