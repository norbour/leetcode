class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if A == None:
            return 0
        length = len(A)
        if length == 0:
            return 0
        if length == 1:
            return 1
        pos = 0
        duplicates = 0
        for i in range(0, length - 1):
            if A[i] != A[i + 1]:
                duplicates = 0
                pos = pos + 1
                A[pos] = A[i + 1]
            else:
                duplicates = duplicates + 1
                if duplicates < 2:
                    pos = pos + 1
                    A[pos] = A[i + 1]
        return pos + 1