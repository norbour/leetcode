# Source : https://oj.leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
# Author : Cao Jin
# Date   : 2014-11-13

# ---------Title---------- 
# Swap Nodes in Pairs
# ---------Description---- 
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# Find the minimum element.

# The array may contain duplicates.
# ---------Tags----------- 
# Array, Binary Search

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if num == None:
            raise ValueError("Invalid array input!")
        length = len(num)
        if length == 0:
            raise ValueError("Invalid array input!")
        low = 0
        high = length - 1
        index = 0
        while num[low] >= num[high]:
            if low + 1 == high:
                index = high
                break
            mid = (low + high) / 2
            if num[mid] == num[low] and num[mid] == num[high]:
                index = self.findMinByTraversal(num, low ,high)
                break
            if num[mid] >= num[low]:
                low = mid
            elif num[mid] <= num[high]:
                high = mid
        return num[index]
        
    def findMinByTraversal(self, num, low, high):
        index = low
        minNum = num[low]
        for i in range(low, high + 1):
            if num[i] < minNum:
                index = i
        return index