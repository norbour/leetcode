# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        if root == None:
            return []
        node = root
        stack = []
        result = []
        index = 0
        while True:
            while not node == None:
                stack.append(node)
                node = node.left
            if not len(stack) == 0:
                node = stack.pop()
                result.append(node.val)
                node = node.right
            if node == None and len(stack) == 0:
                break
        return result