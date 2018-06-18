
# TIME
# SPACE - O(n)


def BSTSequence(root):
	return BSTSequencePartial([],[root])

def BSTSequencePartial(partial,subtrees):
	if not len(subtrees):
		return [partial]
	sequences = []
	for index, subtree in enumerate(subtrees):
		nextPartial += subtrees[index]
		nextSubtrees = subtrees[:index] + subtrees[index+1:]
		if subtree.left:
			nextSubtrees.append(subtree.left)
		if subtree.right:
			nextSubtrees.append(subtree.right)
		sequences += BSTSequencePartial(nextPartial,nextSubtrees)
	return sequences
		
