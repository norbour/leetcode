# Source : https://oj.leetcode.com/problems/excel-sheet-column-title/
# Author : Cao Jin
# Date   : 2015-01-16

# ---------Title---------- 
# Excel Sheet Column Title
# ---------Description---- 
# Given a positive integer, return its corresponding column title as appear in an Excel sheet.

# For example:

#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 
# ---------Tags----------- 
# Math

class Solution:
    # @return a string
    def convertToTitle(self, num): 			
		result_list = []
		while num > 0:
			num = num - 1
			result_list.append( chr(num % 26 + ord('A') ) )
			num = num / 26
		
		str = ""
		
		return str.join(result_list[::-1])