class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        if A == None:
            return False
        length = len(A)
        if length == 0:
            return False
        pos = 0
        while pos < length - 1:
            if A[pos] != 0:
                if pos + A[pos] <= length - 1:
                    pos = self.positionGreedySearch(A, pos + 1, pos + A[pos])
                else:
                    pos = self.positionGreedySearch(A, pos + 1, length - 1)
                if pos < length - 1 and A[pos] == 0:
                    return False
            else:
                return False
        return True

    def positionGreedySearch(self, A, begin, end):
        max = begin + A[begin]
        pos = begin
        for i in range(begin, end + 1):
            if i + A[i] > max:
                max = i + A[i]
                pos = i
        return pos