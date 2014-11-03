# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        if root == None:
            return []
        node = root
        stack = []
        result = []
        while not node == None:
            result.append(node.val)
            if not node.right == None:
                stack.append(node.right)
            if not node.left == None:
                node = node.left
            else:
                if len(stack) == 0:
                    break
                node = stack.pop()
        return result