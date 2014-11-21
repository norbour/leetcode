# Source : https://oj.leetcode.com/problems/rotate-image/
# Author : Cao Jin
# Date   : 2014-11-20

# ---------Title---------- 
# Rotate Image 
# ---------Description---- 
# You are given an n x n 2D matrix representing an image.

# Rotate the image by 90 degrees (clockwise).

# Follow up:
# Could you do this in-place?
# ---------Tags----------- 
# Array

class Solution:
	# @param matrix, a list of lists of integers
	# @return a list of lists of integers
	def rotate(self, matrix):
		if matrix == None:
			return [[]]
		n = len(matrix);
		if n > 1:
			for i in range(0, n/2):
				for j in range(i, n-1-i): 
					temp = matrix[j][n-i-1];
					matrix[j][n-i-1] = matrix[i][j];
					matrix[i][j] = matrix[n-j-1][i];
					matrix[n-j-1][i] = matrix[n-i-1][n-j-1];
					matrix[n-i-1][n-j-1] = temp;
		return matrix