# TIME - O(n)
# SPACE - O(1)

class Tree:
	
	def __init__(self, data, left = None, right = None):
		self.data= data
		self.left = left
		self.right = right


	def minimalTree(arr,start,end)
		if start > end:
			return None
		mid = (start+end)//2
		tree = Tree(arr[mid])
		tree.left = self.minimalTree(arr[start:mid-1], start, mid-1)
		tree.right = self.minimalTree(arr[mid+1:end],mid+1 , end)
		return tree
		

if __name__ == '__main__':
	t = Tree()
	arr = [1,2,3,4,5,6,7,8,9,10]
	t.minimalTree(arr,0,len(arr))
	
