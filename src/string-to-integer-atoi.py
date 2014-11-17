class Solution:
    # @return an integer
    def atoi(self, str):
        if str == None:
            return 0
        length = len(str)
        if length == 0:
            return 0
        i = 0
        sum = 0
        sign = 1
        dict = { '0':0, '1':1, '2':2,
                 '3':3, '4':4, '5':5,
                 '6':6, '7':7, '8':8, '9':9 }
        while i < length and self.isSpace(str[i]):
            i = i + 1
        if str[i] == '-':
            sign = -1
            i = i + 1
        elif str[i] == '+':
            i = i + 1
        while i < length and self.isDigit(str[i]):
            sum = sum * 10 + dict[str[i]]
            i = i + 1
        #if i < length:
        #    return 0
        result = sum * sign
        if result >= 2147483647:
            return 2147483647
        elif result <= -2147483648:
            return -2147483648
        return result
    
    def isDigit(self, a):
        if a >= '0' and a <= '9':
            return True
        else:
            return False
    
    def isSpace(self, a):
        if a == ' ' or a == '\t' or a == '\n' or a == '\r':
            return True
        else:
            return False