class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        i = 1
        result = A[0]
        while i <= len(A) - 1:
            result = result^A[i]
            i = i + 1
        return result