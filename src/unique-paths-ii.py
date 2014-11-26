# Source : https://oj.leetcode.com/problems/unique-paths-ii/
# Author : Cao Jin
# Date   : 2014-11-26

# ---------Title---------- 
# Unique Paths II
# ---------Description---- 
# Follow up for "Unique Paths":

# Now consider if some obstacles are added to the grids. How many unique paths would there be?

# An obstacle and empty space is marked as 1 and 0 respectively in the grid.

# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.

# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.

# Note: m and n will be at most 100.
# ---------Tags----------- 
# Array, Dynamic programming

import copy

class Solution:
	# @param obstacleGrid, a list of lists of integers
	# @return an integer
	def uniquePathsWithObstacles(self, obstacleGrid):
		if obstacleGrid == None:
			raise ValueError("Invalid obstacleGrid input!")
		m = len(obstacleGrid)
		if m == 0:
			raise ValueError("Invalid obstacleGrid input: 0 row!")
		n = len(obstacleGrid[0])
		if n == 0:
			raise ValueError("Invalid obstacleGrid input: 0 column!")
		pathGrid = copy.copy(obstacleGrid)
		for i in range(0, m):
			if obstacleGrid[i][0] == 1 or (i > 0 and pathGrid[i - 1][0] == -1):
				pathGrid[i][0] = -1
			else:
				pathGrid[i][0] = 1
		for j in range(1, n):
			if obstacleGrid[0][j] == 1 or (j > 0 and pathGrid[0][j - 1] == -1):
				 pathGrid[0][j] = -1
			else:
				 pathGrid[0][j] = 1
		for i in range(1, m):
			for j in range(1, n):
				if obstacleGrid[i][j] == 1:
					pathGrid[i][j] = -1
				elif pathGrid[i - 1][j] == -1:
					pathGrid[i][j] = pathGrid[i][j - 1]
				elif pathGrid[i][j - 1] == -1:
					pathGrid[i][j] = pathGrid[i - 1][j]
				else:
					pathGrid[i][j] = pathGrid[i][j - 1] + pathGrid[i - 1][j]
		return max(0, pathGrid[m - 1][n - 1])