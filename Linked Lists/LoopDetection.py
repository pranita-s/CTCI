
# TIME - O(n)
# SPACE - O(1)

def loopDetection(head):
	slow = fast = head
	while slow is not fast:
		slow, fast  = slow.next, fast.next.next
	
	slow = head
	
	while slow is not fast:
		slow, fast = slow.next, fast.next
	
	return slow
