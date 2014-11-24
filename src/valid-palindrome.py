class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if s == None:
            return False
        length = len(s)
        if length <= 1:
            return True
        low = 0
        high = length - 1
        while low < high:
            while low < high and not self.isAlphanumeric(s[low]):
                low = low + 1
            while low < high and not self.isAlphanumeric(s[high]):
                high = high - 1
            if s[low] == s[high] or str.upper(s[low]) == str.upper(s[high]):
                low = low + 1
                high = high - 1
            else:
                return False
        return True
        
    def isAlphanumeric(self, char):
        if (char >= '0' and char <= '9') or (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
            return True
        else:
            return False