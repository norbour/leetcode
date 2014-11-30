# Source : https://oj.leetcode.com/problems/word-break/
# Author : Cao Jin
# Date   : 2014-11-30

# ---------Title---------- 
# Word Break
# ---------Description---- 
# Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# For example, given
# s = "leetcode",
# dict = ["leet", "code"].

# Return true because "leetcode" can be segmented as "leet code".
# ---------Tags----------- 
# Dynamic programming

class Solution:
	# @param s, a string
	# @param dict, a set of string
	# @return a boolean
	def wordBreak(self, s, dict):
		if s == None or dict == None:
			return True
		length = len(s)
		wb = [0 for i in range(0, length + 1)]
		for i in range(1, length + 1):
			if wb[i] == 0 and s[0:i] in dict:
				wb[i] = 1
			if wb[i] == 1:
				if i == length:
					return True
				for j in range(i + 1, length + 1):
					if wb[j] == 0 and s[i:j] in dict:
						wb[j] = 1
					if j == length and wb[j] == 1:
						return True
		return False