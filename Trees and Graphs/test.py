import random
class BinaryTreeNode:

    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
        self.count = 1


def insert(root,key):
  root.count += 1
  if key > root.data:
    if not root.right:
      root.right = BinaryTreeNode(key)
    else:
      insert(root.right,key)  
  else:
    if not root.left:
      root.left = BinaryTreeNode(key)
    else:
      insert(root.left,key)

def inorderSuccessor(root):
    while root.left:
      root = root.left
   return root.data

def delete(root,key):
  if key > root.val:
    return delete(root.right,key)
  else:
    return delete(root.left,key)
  
  if not root.left:
    return root.right
  elif not root.right:
    return root.left
 
  temp = inorderSuccessor(root.right)
  root.data = temp
  root.right = delete(root.right,temp)
  


def getIthNode(root,i):
  if i == 0:
    return root
  
  if root.left:
    if i-1 < root.left.count:
      return getIthNode(root.left,i-1)
    else:
      return getIthNode(root.right,i-root.left.count-1)
  
  elif root.right:
    return getIthNode(root.right,i-1)
  else:
    return None
    
    
def getRandomNode(root):
  i = random.randint(0,root.count-1)
  return getIthNode(root,i)
  
