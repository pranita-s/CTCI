
# TIME - O(n)
# SPACE - O(D)

dict = {0:1}
def pathsWithSum(root,runningSum,target):
	if not root:
		return 0
	runningSum += root.data
	dict[runningSum] = dict.get((runningSum),0)+1
	totalPath = dict.get((runningSum-target),0)
	totalPath += pathsWithSum(root.left, runningSum,target)
	totalPath += pathsWithSum(root.right,runningSum,target)
	dict.pop(runningSum)
	return totalPath

	
