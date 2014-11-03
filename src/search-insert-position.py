class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def bianrySearch(self, A, target, st, ed):
        mid = (st + ed) / 2
        if A[mid] == target:
            return mid
        elif A[mid] > target:
            if mid == st or A[mid - 1] < target:
                return mid
            else:
                return self.bianrySearch(A, target, st, mid - 1)
        elif A[mid] < target:
            if mid == ed or A[mid + 1] > target:
                return mid + 1
            else:
                return self.bianrySearch(A, target, mid + 1, ed)
        
    def searchInsert(self, A, target):
        if A == None:
            return -1
        length = len(A)
        return self.bianrySearch(A, target, 0, length - 1)