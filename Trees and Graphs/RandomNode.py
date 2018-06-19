# TIME - O(D) D - max depth of tree
# SPACE - O(D)

import random
class BinaryTreeNode:

    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
        self.count = 1

class BST:

    def __init__(self):
        self.root = None

    def insert(self,root,key):
            root.count += 1
            if key > root.data:
                if not root.right:
                    root.right = BinaryTreeNode(key)
                else:
                    self.insert(root.right,key)
            else:
                if not root.left:
                    root.left = BinaryTreeNode(key)
                else:
                    self.insert(root.left,key)

    def inorderSuccessor(self,node):
        while node.left:
            node = node.left
        return node.data

    def delete(self,root,key):
        if not root:
            return None
        root.count -= 1
        if key < root.data:
            return self.delete(root.left,key)

        if key > root.data:
            return self.delete(root.right,key)

        if not root.right:
            return root.left
        if not root.left:
            return root.right

        temp = self.inorderSuccessor(root.right)
        root.data = temp
        root.right = self.delete(root.right,temp)
        return root

    def getIthNode(self,root,i):
        if i == 0:
            return root
        if root.left:
            if i-1 < root.left.count:
                return self.getIthNode(root.left,i-1)
            else:
                return self.getIthNode(root.right, i - root.left.count-1)
        elif root.right:
            return self.getIthNode(root.right,i-1)
        else:
            return None


    def getrandom(self,root):
        i = random.randint(0,root.count-1)
        return self.getIthNode(root,i)



obj = BST()
root = BinaryTreeNode(20)
obj.insert(root,10)
obj.insert(root,30)
obj.insert(root,5)
obj.insert(root,15)
obj.insert(root,17)
obj.insert(root,35)
obj.insert(root,3)
obj.insert(root,7)
obj.delete(root,15)
obj.delete(root,5)

print(obj.getrandom(root).data)
print(obj.getrandom(root).data)
print(obj.getrandom(root).data)






