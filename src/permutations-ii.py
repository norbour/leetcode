# Source : https://oj.leetcode.com/problems/permutations-ii/
# Author : Cao Jin
# Date   : 2014-11-06

# ---------Title---------- 
# Permutations 
# ---------Description---- 
# Given a collection of numbers that might contain duplicates, return all possible unique 
# permutations.

# For example,
# [1,1,2] have the following unique permutations:
# [1,1,2], [1,2,1], and [2,1,1].
# ---------Tags----------- 
# Backtracking

class Solution:
	# @param num, a list of integer
	# @return a list of lists of integers
	def permuteUnique(self, num):
		if num == None:
			return None
		result = []
		self.permuteCore(num, 0, len(num), result)
		return result
	
	def permuteCore(self, num, begin, length, result):
		if begin == length:
			result.append(copy.copy(num))
		else:
			dict = {}
			for i in range(begin, length):
				if not num[i] in dict:
					dict[num[i]] = "true"
					temp = num[i]
					num[i] = num[begin]
					num[begin] = temp
				
					self.permuteCore(num, begin + 1, length, result)
				
					temp = num[i]
					num[i] = num[begin]
					num[begin] = temp