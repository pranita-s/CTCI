
# TIME - O(n**2)
# SPACE - O(1)

def removeDups(head):
	first = second = head
	while first:
		while second.next:
			if second.next.val == first.val:
				second.next = second.next.next
			else:
				second = second.next
		first = second = first.next
	return head

# TIME - O(n)
# SPACE - O(n)

def removeDupsWithBuffer(head):
	lookup = {}
	first = head
	if not first:
		return head
	lookup[first.val] = 1
	while first and first.next:
		if first.next.val in lookup:
			first.next = first.next.next
		else:
			lookup[first.next.val] = 1
			first = first.next
	return head
