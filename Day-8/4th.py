# 12 34 54 67 78 79 90
# 900



#codeforces 1843C
def totalSum(self,root):
  if root is None:
    return 0
  else:
    leftSum=totalSum(root.left)
    rightSum=totalSum(root.right)
    return root.data+leftSum+rightSum
def treeMax(self,root):
  if root is None:
    return 0
  else:
    leftMax=treeMax(root.left)
    rightMax=treeMax(root.right)
  return max(root.data,leftMax,rightMax)

def treeHeight(self,root):
  if root is None:
    return 0
  else:
    leftHeight=treeHeight(root.left)
    rightHeight=treeHeight(root.right)
    return 1 + max(leftHeight,rightHeight)
