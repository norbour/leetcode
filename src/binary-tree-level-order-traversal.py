# Source : https://oj.leetcode.com/problems/binary-tree-level-order-traversal/
# Author : Cao Jin
# Date   : 2014-11-10

# ---------Title---------- 
# Binary Tree Level Order Traversal  
# ---------Description---- 
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
# ---------Tags----------- 
# Tree, Breadth-first Search

import copy

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        stack = []
        result = []
        if root != None:
            stack.append(root)
            cur = 0
            last = 1
            while cur < len(stack):
                last = len(stack)
                levelNodes = []
                while cur < last:
                    node = stack[cur]
                    levelNodes.append(node.val)
                    if node.left != None:
                        stack.append(node.left)
                    if node.right != None:
                        stack.append(node.right)
                    cur = cur + 1
#                print levelNodes
                result.append(levelNodes)
        return result