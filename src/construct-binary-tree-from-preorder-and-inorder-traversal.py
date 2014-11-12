# Source : https://oj.leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Author : Cao Jin
# Date   : 2014-11-11

# ---------Title---------- 
# Construct Binary Tree from Preorder and Inorder Traversal  
# ---------Description---- 
# Given preorder and inorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.
# ---------Tags----------- 
# Tree, Array, Depth-first Search

# Definition for a  binary tree node

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param preorder, a list of integers
	# @param inorder, a list of integers
	# @return a tree node
	def buildTree(self, preorder, inorder):
		if preorder == None or inorder == None:
			return None
		pre_length = len(preorder)
		in_length = len(inorder)
		if pre_length != in_length or in_length < 0 or pre_length < 0:
			raise ValueError("Traversal Sequence is invalid!")
		if pre_length == 0:
			return None
		return self.buildTreeCore(preorder, 0, pre_length - 1,
	                              inorder,  0, in_length - 1)

	def buildTreeCore(self, preorder, pre_st, pre_ed, 
	                        inorder,  in_st,  in_ed):
		# 前序遍历中第一个数字为根节点的值
		rootValue = preorder[pre_st]
		root = TreeNode(rootValue)
		if pre_st == pre_ed:
			if in_st == in_ed and preorder[pre_st] == inorder[in_st]:
				return root
			else:
				raise ValueError("Traversal Sequence is invalid!")
		# 在中序遍历序列中找根节点位置
		rootInorder = in_st
		while (rootInorder <= in_ed and inorder[rootInorder] != rootValue):
			rootInorder = rootInorder + 1
		if rootInorder == in_ed and inorder[rootInorder] != rootValue:
			raise ValueError("Traversal Sequence is invalid!")
		leftLength = rootInorder - in_st
		left_pre_ed = pre_st + leftLength
		if leftLength > 0:
			root.left = self.buildTreeCore(preorder, pre_st + 1, left_pre_ed,
	                                       inorder,  in_st,      rootInorder - 1)
		if leftLength < pre_ed - pre_st:
			root.right = self.buildTreeCore(preorder, left_pre_ed + 1, pre_ed,
	                                        inorder,  rootInorder + 1, in_ed)
		return root