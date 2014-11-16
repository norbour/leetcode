# Source : https://oj.leetcode.com/problems/sort-colors/
# Author : Cao Jin
# Date   : 2014-11-14

# ---------Title---------- 
# Sort Colors
# ---------Description---- 
# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Note:
# You are not suppose to use the library's sort function for this problem.

# click to show follow up.

# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

# Could you come up with an one-pass algorithm using only constant space?
# ---------Tags----------- 
# Array, Two Pointers, Sort

class Solution:
	# @param A a list of integers
	# @return nothing, sort in place
	def sortColors(self, A):
		if A == None:
			return
		length = len(A)
		if length < 2:
			return
		p0 = 0
		p2 = length - 1
		cur = 0
		while cur <= p2:
			if A[cur] == 2:
				self.swap(A, cur, p2)
				p2 = p2 - 1
			elif A[cur] == 0:
				self.swap(A, cur, p0)
				p0 = p0 + 1
				cur = cur + 1
			else:
				cur = cur + 1
		                
	def swap(self, A, i, j):
		temp = A[i]
		A[i] = A[j]
		A[j] = temp