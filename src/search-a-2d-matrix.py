# Source : https://oj.leetcode.com/problems/search-a-2d-matrix/
# Author : Cao Jin
# Date   : 2014-11-13

# ---------Title---------- 
# Search a 2D Matrix
# ---------Description---- 
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# For example,

# Consider the following matrix:

# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.
# ---------Tags----------- 
# Array, Binary Search

class Solution:
	# @param matrix, a list of lists of integers
	# @param target, an integer
	# @return a boolean
	def searchMatrix(self, matrix, target):
		if matrix == None:
			return False
		rowDim = len(matrix)
		if rowDim == 0:
			return False
		colDim = len(matrix[0])
		if colDim == 0:
			return False
		low = 0
		high = rowDim * colDim - 1
		if target < matrix[low / colDim][low % colDim] or target > matrix[high / colDim][high % colDim]:
			return False
		while low <= high:
			mid  = (low + high) >> 1
			if low + 1 == high:
				if target == matrix[low / colDim][low % colDim] or target == matrix[high / colDim][high % colDim]:
					return True
				else:
					return False
			if target == matrix[mid / colDim][mid % colDim]:
				return True
			if target > matrix[mid / colDim][mid % colDim]:
				low = mid
			elif target < matrix[mid / colDim][mid % colDim]:
				high = mid
		return False