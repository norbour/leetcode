# Source : https://oj.leetcode.com/problems/single-number-ii/
# Author : Cao Jin
# Date   : 2014-11-05

# ---------Title---------- 
# Single Number II
# ---------Description---- 
# Given an array of integers, every element appears three times except for one. Find that single one.
# ---------Note-----------
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
# ---------Tags----------- 
# Bit Manipulation

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        length = len(A)
        ones = 0
        twos = 0
        threes = 0
        for i in range(0, length):
            twos = twos | (ones & A[i])
            ones = ones ^ A[i]
            threes = ones & twos
            ones = ones & (~threes)
            twos = twos & (~threes)
        return ones