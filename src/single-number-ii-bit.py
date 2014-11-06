# Source : https://oj.leetcode.com/problems/single-number-ii/
# Author : Cao Jin
# Date   : 2014-11-06

# ---------Title---------- 
# Single Number II
# ---------Description---- 
# Given an array of integers, every element appears three times except for one. Find that 
# single one.
# ---------Note-----------
# Your algorithm should have a linear runtime complexity. Could you implement it without 
# using extra memory?
# ---------Tags----------- 
# Bit Manipulation

import sys

class Solution:
	# @param A, a list of integer
	# @return an integer
	def singleNumber(self, A):
		length = len(A)
		bits = sys.getsizeof(A[0]) * 8
		bitNum = [0 for i in range(0, bits)]
		singleNumber = 0
		for i in range(0, bits):
			for j in range(0, length):
				bitNum[i] = bitNum[i] + ((A[j] >> i) & 1)
			singleNumber = singleNumber | ((bitNum[i] % 3) << i)
		return singleNumber
			
if __name__ == '__main__':
	slo = Solution()
	num = [2,2,3,2,3,3,5]
	print slo.singleNumber(num)