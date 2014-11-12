# Source : https://oj.leetcode.com/problems/maximum-product-subarray/
# Author : Cao Jin
# Date   : 2014-11-12

# ---------Title---------- 
# Maximum Product Subarray 
# ---------Description---- 
# Find the contiguous subarray within an array (containing at least one number) which has the largest product.

# For example, given the array [2,3,-2,4], the contiguous subarray [2,3] has the largest product = 6.
# ---------Tags----------- 
# Array, Dynamic Programming

class Solution:
	# @param A, a list of integers
	# @return an integer
	def maxProduct(self, A):
		if A == None:
			raise ValueError("Invalid array input!")
		length = len(A)
		if length == 0:
			raise ValueError("Invalid array input!")
		_max = A[0]
		_min = A[0]
		result = _max
		for i in range(1, length):
			tmpMax = _max * A[i]
			tmpMin = _min * A[i]
			_max = max(tmpMax, tmpMin, A[i])
			_min = min(tmpMin, tmpMax, A[i])
			result = max(result, _max)