# Source : https://oj.leetcode.com/problems/container-with-most-water/
# Author : Cao Jin
# Date   : 2014-11-06

# ---------Title---------- 
# Container With Most Water
# ---------Description---- 
# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.

#Note: You may not slant the container.
# ---------Tags----------- 
# Array, Two Pointers

class Solution:
    # @return an integer
    def maxArea(self, height):
        if height == None:
            return 0
        length = len(height)
        if length <= 1:
            return 0
        maxV = 0
        start = 0
        end = length - 1
        while start < end:
            v = min(height[end], height[start]) * (end - start)
            maxV = max(maxV, v)
            if height[start] < height[end]:
                start = start + 1
            else:
                end = end - 1
        return maxV
        