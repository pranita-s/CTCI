
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
