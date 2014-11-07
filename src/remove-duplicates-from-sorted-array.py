# Source : https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array/
# Author : Cao Jin
# Date   : 2014-11-07

# ---------Title---------- 
# Remove Duplicates from Sorted Array  
# ---------Description---- 
# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this in place with constant memory.
# For example,
# Given input array A = [1,1,2],
# Your function should return length = 2, and A is now [1,2].
# ---------Tags----------- 
# Array, Two Pointers

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if A == None:
            return 0
        length = len(A)
        if length == 0:
            return 0
        if length == 1:
            return 1
        pos = 0
        for i in range(0, length - 1):
            if not A[i] == A[i + 1]:
                pos = pos + 1
                A[pos] = A[i + 1]
#        tail = length - 1
#        while tail > pos:
#            A.pop()
#            tail = tail - 1
        return pos + 1