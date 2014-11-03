# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root == None:
            return 0
        left = 0
        right = 0
        if root.left != None:
            left = self.maxDepth(root.left)
        if root.right != None:
            right = self.maxDepth(root.right)
            
        if left > right:
            return left + 1
        else:
            return right + 1