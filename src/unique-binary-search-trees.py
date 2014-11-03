class Solution:
    # @return an integer
    def numTrees(self, n):
        if n < 1:
            return 0
        if n == 1:
            return 1
        sum = 0
        for r in range(1, n + 1):
            left = self.numTrees(r - 1)
            right = self.numTrees(n - r)
            if not left == 0 and not right == 0:
                sum = sum + right * left
            elif left == 0:
                sum = sum + right
            elif right == 0:
                sum = sum + left
        return sum