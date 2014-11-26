class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        if s == None:
            return 0
        length = len(s)
        if length == 0:
            return 0
        tail = length - 1
        while tail > 0 and self.isSpace(s[tail]):
            tail = tail - 1
        head = tail
        while head >= 0 and not self.isSpace(s[head]):
            head = head - 1
        return tail - head

    def isSpace(self, char):
        if char == ' ' or char == '\n' or char == '\t':
            return True
        else:
            return False