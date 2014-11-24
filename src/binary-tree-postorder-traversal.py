# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of integers
	def postorderTraversal(self, root):
		if root == None:
			return []
		stack = []
		result = []
		pre = None
		cur = None
		stack.append(root)
		while len(stack) != 0:
			cur = stack[len(stack) - 1]
			if (cur.right == None and cur.left == None) or (pre != None and (pre == cur.left or pre == cur.right)):
				result.append(stack.pop().val)
				pre = cur
			else:
				if cur.right != None:
					stack.append(cur.right)
				if cur.left != None:
					stack.append(cur.left)
		return result