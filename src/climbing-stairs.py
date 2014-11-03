class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n < 1:
            return 0
        solution = [1, 2]
        if n <= 2:
            return solution[n - 1]
        nMinusOne = 2
        nMinusTwo = 1
        wayN = 0
        for i in range(3, n + 1):
            wayN = nMinusOne + nMinusTwo
            nMinusTwo = nMinusOne
            nMinusOne = wayN
        return wayN