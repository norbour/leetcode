class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        if word1 == None or word2 == None:
            raise ValueError("Invalid word input occured!")
        m = len(word1)
        n = len(word2)
        grid = [ [0 for i in range(0, n + 1)] for j in range(0, m + 1) ]
        for i in range(0, m + 1):
            grid[i][0] = i
        for j in range(0, n + 1):
            grid[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    grid[i][j] = min(grid[i - 1][j] + 1, grid[i][j - 1] + 1, grid[i - 1][j - 1])
                else:
                    grid[i][j] = min(grid[i - 1][j] + 1, grid[i][j - 1] + 1, grid[i - 1][j - 1] + 1)
        return grid[m][n]
        
# reference http://blog.csdn.net/huaweidong2011/article/details/7727482
#           http://blog.csdn.net/hackbuteer1/article/details/6686931