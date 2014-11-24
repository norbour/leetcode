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
		return pathCostGrid[m - 1][n - 1]