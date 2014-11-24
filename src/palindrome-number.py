class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x <= 9:
            return True
        reverse_src = x
        reverse_dst = 0
        while reverse_src != 0:
            reverse_dst = reverse_dst * 10 + reverse_src % 10
            reverse_src = reverse_src / 10
        if reverse_dst == x:
            return True
        else:
            return False