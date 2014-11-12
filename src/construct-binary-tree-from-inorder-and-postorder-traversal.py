# Source : https://oj.leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# Author : Cao Jin
# Date   : 2014-11-11

# ---------Title---------- 
# Construct Binary Tree from Inorder and Postorder Traversal   
# ---------Description---- 
# Given inorder and postorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.
# ---------Tags----------- 
# Tree, Stack, Depth-first Search

# Definition for a  binary tree node
# class TreeNode:
# 	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param inorder, a list of integers
	# @param postorder, a list of integers
	# @return a tree node
	def buildTree(self, inorder, postorder):
		if postorder == None or inorder == None:
			return None
		post_length = len(postorder)
		in_length = len(inorder)
		if post_length != in_length or in_length < 0 or post_length < 0:
			raise ValueError("Traversal Sequence is invalid!")
		if post_length == 0:
			return None
		return self.buildTreeCore(postorder, 0, post_length - 1,
		                          inorder,  0, in_length - 1)
		    
	def buildTreeCore(self, postorder, post_st, post_ed, 
		                    inorder,  in_st,  in_ed):
		# the last node in postorder list is root
		rootValue = postorder[post_ed]
		root = TreeNode(rootValue)
		if post_st == post_ed:
			if in_st == in_ed and postorder[post_st] == inorder[in_st]:
				return root
			else:
				raise ValueError("Traversal Sequence is invalid!")
		# find root node position in inorder list
		rootInorder = in_st
		while (rootInorder <= in_ed and inorder[rootInorder] != rootValue):
			rootInorder = rootInorder + 1
			if rootInorder == in_ed and inorder[rootInorder] != rootValue:
				raise ValueError("Traversal Sequence is invalid!")
			leftLength = rootInorder - in_st
			left_post_ed = post_st + leftLength - 1
			if leftLength > 0:
				root.left = self.buildTreeCore(postorder, post_st, left_post_ed,
		                                       inorder,   in_st,   rootInorder - 1)
			if leftLength < post_ed - post_st:
				root.right = self.buildTreeCore(postorder, left_post_ed + 1, post_ed - 1,
		                                        inorder,   rootInorder + 1,  in_ed)
		return root