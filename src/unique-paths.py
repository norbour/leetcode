# Source : https://oj.leetcode.com/problems/unique-paths/
# Author : Cao Jin
# Date   : 2014-11-21

# ---------Title---------- 
# Unique Paths
# ---------Description---- 
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?

# Note: m and n will be at most 100.
# ---------Tags----------- 
# Array, Dynamic programming

class Solution:
	# @return an integer
	def uniquePaths(self, m, n):
		if m <= 0 or n <= 0:
			return 0
		grid = [0 for i in range(0, m*n)]
		for i in range(0, m):
			grid[i] = 1
		for j in range(0, n):
			grid[j * m] = 1
		print grid
		for i in range(1, m):
			for j in range(1, n):
				grid[m * j + i] = grid[m * (j - 1) + i] + grid[m * j + i - 1]
				print grid
		return grid[m * n - 1]