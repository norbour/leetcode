class Solution:
    # @param s, a string
    # @return a string
    def reverse(self, s, st, ed):
        if s == None or st > ed:
            return None
        if st == ed:
            return s[st]
        return s[st:ed][::-1]
    
    def clear(self, s):
        st = 0
        ed = len(s) - 1
        while st < len(s) and s[st] == " ":
            st = st + 1
        while ed > -1 and s[ed] == " ":
            ed = ed - 1
        if st > ed:
            return ""
        return s[st:ed + 1]
        
    def reverseWords(self, s):
        if s == None:
            return None
        s = self.clear(s)
        length = len(s)
        if length == 0:
            return ""
        result = ""
        st = 0
        ed = 0
        while not st == length:
            if s[st] == " ":
                st = st + 1
                ed = ed + 1
            elif ed == length or s[ed] == " ":
                result = result + self.reverse(s, st, ed) + " "
                st = ed
            else:
                ed = ed + 1
        return self.reverse(result, 0, len(result) - 1)