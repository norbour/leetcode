# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root == None:
            return False
        path = []
        curSum = 0
        return self.hasPathSumCore(root, path, curSum, sum)
        
    def hasPathSumCore(self, root, path, curSum, sum):
        curSum = curSum + root.val
        path.append(root.val)
        isLeaf = root.left == None and root.right == None
        if curSum == sum and isLeaf:
            return True
        checkLeft = False
        checkRight = False
        if root.left != None:
            checkLeft = self.hasPathSumCore(root.left, path, curSum, sum)
        if root.right != None:
            checkRight = self.hasPathSumCore(root.right, path, curSum, sum)
        curSum = curSum - root.val
        path.pop()
        
        return checkLeft or checkRight