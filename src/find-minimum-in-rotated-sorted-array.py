# Source : https://oj.leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Author : Cao Jin
# Date   : 2014-11-08

# ---------Title---------- 
# Find Minimum in Rotated Sorted Array   
# ---------Description---- 
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# Find the minimum element.

# You may assume no duplicate exists in the array.
# ---------Tags----------- 
# Array, Binary Search

class Solution:
	# @param num, a list of integer
	# @return an integer
	def findMin(self, num):
		if num == None:
			return -1
		length = len(num)
		if length == 0:
			return -1
		low = 0
		high = length - 1
		index = low
		while num[low] > num[high]:
			if low + 1 == high:
				index = high
				break
			mid = (low + high) / 2
			if num[mid] > num[low]:
				low = mid
			elif num[mid] < num[high]:
				high = mid
		return num[index]