
# TIME - O(n)
# SPACE - O(1)


def sumLists(l1,l2):
	carry = 0
	res_head = result = ListNode(0)
	while l1 or l2 or carry:
		total = carry + (l1.data if l1) + (l2.data if l2)
		result.next = ListNode(total  % 10)
		l1 = l1.next if l1 else None
		l2 = l2.next if l2 else None
		carry = total / 10
		result = result.next
	return res_head


# FOLLOW UP
def sumLists(l1,l2):
	s1 , s2 = [], []
	res_head = result = ListNode(0)
	while l1:
		s1.append(l1.data)
		l1 = l1.next
	
	while l2:
		s2.append(l2.data)
		l2 = l2.next
	carry = 0
	while s1 or s2 or carry:
		total = carry + (s1.pop() if s1) + (s2.pop() if s2)
		result.next = ListNode(total % 10)
		result = result.next
		carry = total // 10
	return res_head
