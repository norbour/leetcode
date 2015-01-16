# Source : https://oj.leetcode.com/problems/excel-sheet-column-number/
# Author : Cao Jin
# Date   : 2015-01-16

# ---------Title---------- 
# Excel Sheet Column Number
# ---------Description---- 
# Related to question Excel Sheet Column Title

# Given a column title as appear in an Excel sheet, return its corresponding column number.

# For example:

#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 
# ---------Tags----------- 
# Math

class Solution:
    # @param s, a string
    # @return an integer
	def titleToNumber(self, s):
		if s == None:
			return 0
			
		length = len(s)
		if length == 0:
			return 0
		
		trans_table = {}

		for  i in xrange(26):
			trans_table[chr(i + ord('A'))] = (i + 1)
			
		colunm = 0
		for i in xrange(length):
			colunm = colunm * 26 + trans_table[ s[i] ]
		
		return colunm
		
		if num > 0:	
			result_list.append(trans_table[num])
		
		str = ""
		
		return str.join(result_list)