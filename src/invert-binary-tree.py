# Source : https://leetcode.com/problems/invert-binary-tree/
# Author : Cao Jin
# Date   : 2015-6-26

# ---------Title---------- 
# Invert Binary Tree 
# ---------Description---- 
# Invert a binary tree.

#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
#
# to
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
#
# Trivia:
# This problem was inspired by this original tweet by Max Howell:
# Google: 90% of our engineers use the software you wrote (Homebrew), but you # can’t invert a binary tree on a whiteboard so fuck off.

# For example, given
# s = "leetcode",
# dict = ["leet", "code"].

# Return true because "leetcode" can be segmented as "leet code".
# ---------Tags----------- 
# Dynamic programming

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param {TreeNode} root
	# @return {TreeNode}
	def invertTree(self, root):
		if root == None:
			return
		newRoot = TreeNode(root.val)
		newRoot.left = self.invertTree(root.right)
		newRoot.right = self.invertTree(root.left)
	        
		return newRoot