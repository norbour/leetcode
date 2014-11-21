# Source : https://oj.leetcode.com/problems/minimum-path-sum/
# Author : Cao Jin
# Date   : 2014-11-22

# ---------Title---------- 
# Minimum Path Sum
# ---------Description---- 
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which 
# minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.
# ---------Tags----------- 
# Array, Dynamic programming

import copy

class Solution:
	# @param grid, a list of lists of integers
	# @return an integer
	def minPathSum(self, grid):
		if grid == None:
			raise ValueError("Invalid grid input!")
		m = len(grid)
		if m == 0:
			raise ValueError("Invalid grid input!")
		n = len(grid[0])
		if n == 0:
			raise ValueError("Invalid grid input!")
		pathCostGrid = copy.copy(grid)
		for i in range(1, m):
			pathCostGrid[i][0] = pathCostGrid[i - 1][0] + pathCostGrid[i][0]
		for j in range(1, n):
			pathCostGrid[0][j] = pathCostGrid[0][j - 1] + pathCostGrid[0][j]
		for i in range(1, m):
			for j in range(1, n):
				pathCostGrid[i][j] = pathCostGrid[i][j] + min(pathCostGrid[i - 1][j], pathCostGrid[i][j - 1])
		print pathCostGrid