# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root == None:
            return 0
        leftDepth = 0
        rightDepth = 0
        if root.left != None and root.right != None:
            leftDepth = self.minDepth(root.left)
            rightDepth = self.minDepth(root.right)
            if leftDepth > rightDepth:
                return rightDepth + 1
            else:
                return leftDepth + 1
        elif root.right != None:
            return 1 + self.minDepth(root.right)
        elif root.left != None:
            return 1 + self.minDepth(root.left)
        else:
            return 1 + 0