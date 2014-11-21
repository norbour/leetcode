# Source : https://oj.leetcode.com/problems/search-in-rotated-sorted-array/
# Author : Cao Jin
# Date   : 2014-11-21

# ---------Title---------- 
# Search in Rotated Sorted Array
# ---------Description---- 
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.
#-------------Tags--------
# Array, Binary search

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        if A == None:
            return False
        length = len(A)
        if length == 0:
            return False
   
        start = 0
        end = length - 1

        minIndex = self.findMinIndex(A)
        
        if minIndex == start:
            return self.binarySearch(A, start, end, target)
        if target >= A[start]:
            end = minIndex - 1
            return self.binarySearch(A, start, end, target)
        else:
            start = minIndex
            return self.binarySearch(A, start, end, target)

    def binarySearch(self, num, start, end, key):
        if num == None or start > end:
            return -1
        while start <= end:
            mid = start + (end - start) / 2
            if num[mid] == key:
                return mid
            elif key < num[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1


    def findMinIndex(self, num):
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
        return index
        
    def findMinByTraversal(self, num, low, high):
        index = low
        minNum = num[low]
        for i in range(low, high + 1):
            if num[i] < minNum:
                index = i
        return index