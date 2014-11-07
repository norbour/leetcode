# Source : https://oj.leetcode.com/problems/trapping-rain-water/
# Author : Cao Jin
# Date   : 2014-11-07

# ---------Title---------- 
# Trapping Rain Water   
# ---------Description---- 
# Given n non-negative integers representing an elevation map where the width of each bar
# is 1, compute how much water it is able to trap after raining.

# For example, 
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
# ---------Tags----------- 
# Array, Stack, Two Pointers

class Solution:
	# @param A, a list of integers
	# @return an integer
	def trap(self, A):
		if A == None:
			return 0
		length = len(A)
		if length < 3:
			return 0
		water = 0
		topHigh = 0
		topHighPoint = 0
		for i in range(0, length):
			if A[i] > topHigh:
				topHigh = A[i]
				topHighPoint = i
		prevHigh = A[0]
		for i in range(0, topHighPoint):
			if A[i] < prevHigh:
				water = water + prevHigh - A[i]
			else:
				prevHigh = A[i]
		prevHigh = A[length - 1]
		for i in range(length - 1, topHighPoint, -1):
			if A[i] < prevHigh:
				water = water + prevHigh - A[i]
			else:
				prevHigh = A[i]
		return water