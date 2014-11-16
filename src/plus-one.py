# Source : https://oj.leetcode.com/problems/plus-one/
# Author : Cao Jin
# Date   : 2014-11-16

# ---------Title---------- 
# Plus One
# ---------Description---- 
# Given a non-negative number represented as an array of digits, plus one to the number.

# The digits are stored such that the most significant digit is at the head of the list.
# ---------Tags----------- 
# Array, Math

class Solution:
	# @param digits, a list of integer digits
	# @return a list of integer digits
	def plusOne(self, digits):
		result = []
		if digits == None:
			return result
		length = len(digits)
		result.append(0)
		for i in range(0, length):
			if digits[i] < 0 or digits[i] > 9:
				raise ValueError("Invalid digit!")
			result.append(digits[i])
		result[length] = result[length] + 1
		if result[length] >= 10:
			temp = 1
			result[length] = result[length] - 10
			i = length - 1
			while temp != 0:
				result[i] = result[i] + temp
				temp = 0
				if result[i] >= 10:
					temp = 1
					result[i] = result[i] - 10
					i = i - 1
		if result[0] == 0:
			result.pop(0)
		return result