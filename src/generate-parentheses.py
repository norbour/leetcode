# Source : https://oj.leetcode.com/problems/generate-parentheses/
# Author : Cao Jin
# Date   : 2014-11-21

# ---------Title---------- 
# Generate Parentheses
# ---------Description---- 
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# "((()))", "(()())", "(())()", "()(())", "()()()"
# ---------Tags----------- 
# String, Backtracking

class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        result = []
        if n <= 0:
            return result
        self.generateParenthesisCore(result, "", n, n)
        return result
    
    def generateParenthesisCore(self, result, cur, lnum, rnum):
        if lnum == 0 and rnum == 0:
            result.append(cur)
        else:
            if lnum != 0:
                self.generateParenthesisCore(result, cur + '(', lnum - 1, rnum)
            if lnum < rnum and rnum != 0:
                self.generateParenthesisCore(result, cur + ')', lnum, rnum - 1)
        