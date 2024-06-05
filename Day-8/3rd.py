#1)Tree construction
#2)Tree Traversals-Level order,Vectical order
#3)Tree views-Left,Right,Top and Bottom views
#4)check given Binary tree is BST
#5)check mirrored Binary tree
#6)Height of the binary tree
#7)print al nodes at level k


#45,23,8,54,21,80,56,33,20,89,99   BST

#Search in BST
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def search(root, val):
    if root is None:
        return None
    if val == root.val:
        print(True)
        return
    elif val < root.val:
        search(root.left, val)
    else:
        search(root.right, val)
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.right = TreeNode(8)
search(root, 5)  
search(root, 3)  
search(root, 8)  
search(root, 6)

