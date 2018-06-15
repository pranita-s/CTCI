
# TIME - O(n)
# SPACE - O(1)

def partition(head):
	less , greater = ListNode(0), ListNode(0)
	
	while head:
		if head.data < 3:
			less.next = head
			less, head = less.next, head.next
		else:
			greater = head
			greater, head = greater.next, head.next
	
	less.next = greater.next
	return less.next
