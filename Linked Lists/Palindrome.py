
# TIME - O(n)
# SPACE - O(1)

def reverse(l):
	dummy = ListNode(0)
	dummy.next = l
	dummy = sublist_head
	subiter = sublist_head.next
	while subiter.next:
		temp = subiter.next
		sublist_head.next, subiter.next, temp.next  = temp, temp.next, sublist_head.next
	return dummy.next
		

def Palindrome(head):
	slow = fast = head
	
	while fast and fast.next:
		slow , fast = slow.next, fast.next.next
	
	if fast:
		slow = slow.next
	
	l1, l2 = head, reverse(slow)
	
	while l1 and l2:
		if l1.data != l2.data:
			return False
		l1, l2 = l1.next, l2.next
	return True
	

# TIME - O(n)
# SPACE - O(n)

def palindrome(head):
	s = []
	slow = fast = head
	while fast and fast.next:
		s.append(slow.data)
		slow , fast = slow.next, fast.next.next
		
	if fast:
		slow = slow.next
		
	while s:
		if slow.data != s.pop():
			return False
		slow = slow.next
	return True
	
	
	
	
	
		
	
	
	
	
	
