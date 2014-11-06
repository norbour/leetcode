# Source : https://oj.leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Author : Cao Jin
# Date   : 2014-11-07

# ---------Title---------- 
# Convert Sorted Array to Binary Search Tree 
# ---------Description---- 
# Given an array where elements are sorted in ascending order, convert it to a height 
# balanced BST.
# ---------Tags----------- 
# Tree, Deep-first Search

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param num, a list of integers
	# @return a tree node
	def sortedArrayToBST(self, num):
		if num == None:
			return None
		length = len(num)
		if length == 0:
			return None
		return self.sortedArrayToBSTCore(num, 0, length - 1)
		
	def sortedArrayToBSTCore(self, num, start, end):
		if num == None or start > end:
			return None
		length = len(num)
		if start < 0 or end >= length:
			return None
		mid = (start + end) / 2
		root = TreeNode(num[mid])
		root.left = self.sortedArrayToBSTCore(num, start, mid - 1)
		root.right = self.sortedArrayToBSTCore(num, mid + 1, end)
		return root