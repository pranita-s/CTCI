
# TIME - 
# SPACE -

def Palindrome(head):
	size = findSize(head)
	slow = fast = head
	
	while fast and fast.next:
		slow , fast = slow.next, fast.next.next
	
	if size % 2:
		slow = slow.next
	
	l1, l2 = head, reverse(slow)
	
	while l1 and l2:
		if l1.data != l2.data:
			return False
		l1, l2 = l1.next, l2.next
	
	if l1 or l2:
		return False
	
	return True
	
	
	
