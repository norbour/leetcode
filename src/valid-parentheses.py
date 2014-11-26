class Solution:
    # @return a boolean
    def isValid(self, s):
        if s== None:
            return True
        length = len(s)
        if length == 0:
            return True
        if length % 2 != 0:
            return False
        if self.isRightParentheses(s[0]) or self.isLeftParentheses(s[length - 1]):
            return False
        i = 0
        stack = []
        while i < length:
            while i < length and self.isLeftParentheses(s[i]):
                stack.append(s[i])
                i = i + 1
            while i < length and self.isRightParentheses(s[i]):
                if not self.match(stack.pop(), s[i]):
                    return False
                else:
                    i = i + 1
        if i >= length and len(stack) == 0:
            return True
        else:
            return False

    def match(self, left, right):
        if (left == '(' and right == ')') or (left == '{' and right == '}') or (left == '[' and right == ']'):
            return True
        else:
            return False

    def isLeftParentheses(self, char):
        if char == '(' or char == '{' or char == '[':
            return True
        else:
            return False

    def isRightParentheses(self, char):
        if char == ')' or char == '}' or char == ']':
            return True
        else:
            return False