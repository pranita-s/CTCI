
# TIME - O(n)
# SPACE - O(1)

def loopDetection(head):
	slow = fast = head
	
	while fast and fast.next and fast.next.next:
		slow, fast = slow.next, fast.next.next
		
		if slow is fast:
			slow = head
			
			while slow is not fast:
				slow, fast = slow.next, fast.next.next
			return slow
	return None
