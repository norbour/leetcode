# Source : https://oj.leetcode.com/problems/balanced-binary-tree/
# Author : Cao Jin
# Date   : 2014-11-08

# ---------Title---------- 
# Balanced Binary Tree 
# ---------Description---- 
# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of
# the two subtrees of every node never differ by more than 1.
# ---------Tags----------- 
# Tree, Depth-first Search

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class TreeNodeWithDepth:
	def __init__(self, node):
		self.node = node
		self.depth = 0

class Solution2:
	# @param root, a tree node
	# @return a boolean
	def isBalanced(self, root):
		rootNode = TreeNodeWithDepth(root)
		return self.isBalancedCore(rootNode)
			
	def isBalancedCore(self, rootNode):
		if rootNode.node == None:
			rootNode.depth = 0
			return True
		leftNode = TreeNodeWithDepth(rootNode.node.left)
		rightNode = TreeNodeWithDepth(rootNode.node.right)
		if self.isBalancedCore(leftNode) and self.isBalancedCore(rightNode):
			diff = leftNode.depth - rightNode.depth
			if diff >= -1 and diff <= 1:
				rootNode.depth = 1 + max(leftNode.depth, rightNode.depth)
				return True
		return False