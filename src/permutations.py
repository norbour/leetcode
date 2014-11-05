# Source : https://oj.leetcode.com/problems/permutations/
# Author : Cao Jin
# Date   : 2014-11-05

# ---------Title---------- 
# Permutations 
# ---------Description---- 
# Given a collection of numbers, return all possible permutations.

# For example,
# [1,2,3] have the following permutations:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
# ---------Tags----------- 
# Backtracking

class Solution:
	# @param num, a list of integer
	# @return a list of lists of integers
	def permute(self, num):
		if num == None:
			return None
		result = []
		self.permuteCore(num, 0, len(num), result)
		return result
	
	def permuteCore(self, num, begin, length, result):
		if begin == length:
			result.append(copy.copy(num))
		else:
			for i in range(begin, length):
				dict[num[i]] = "true"
				temp = num[i]
				num[i] = num[begin]
				num[begin] = temp
				
				self.permuteCore(num, begin + 1, length, result)
				
				temp = num[i]
				num[i] = num[begin]
				num[begin] = temp