# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
	# @param root, a tree node
	# @return nothing
	def connect(self, root):
		if root == None:
			return
		nodeQueue = []
		nodeQueue.append(root)
		cur = 0
		tail = 1
		
		while cur < len(nodeQueue):
			tail = len(nodeQueue)
			
			while cur < tail:
				if cur == tail - 1:
					nodeQueue[cur].next = None
				else:
					nodeQueue[cur].next = nodeQueue[cur + 1]
					
				if not nodeQueue[cur].left == None:
					nodeQueue.append(nodeQueue[cur].left)
				if not nodeQueue[cur].right == None:
					nodeQueue.append(nodeQueue[cur].right)
					
				cur = cur + 1
		return
        