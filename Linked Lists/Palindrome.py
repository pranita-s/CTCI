
# TIME - 
# SPACE -

def reverse(l):
	dummy = ListNode(0)
	dummy.next = l
	dummy = sublist_head
	subiter = sublist_head.next
	while subiter:
		temp = subiter.next
		sublist_head.next, subiter.next, temp.next  = temp, temp.next, sublist_head.next
	return dummy.next
		

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
	
	
	
