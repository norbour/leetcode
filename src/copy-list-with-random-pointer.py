# Source : https://oj.leetcode.com/problems/copy-list-with-random-pointer/
# Author : Cao Jin
# Date   : 2014-11-05

# ---------Title---------- 
# Copy List with Random Pointer
# ---------Description---- 
# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
# Return a deep copy of the list.
# ---------Tags----------- 
# Hash Table, Linked List

# Definition for singly-linked list with a random pointer.
class RandomListNode:
	def __init__(self, x):
		self.label = x
		self.next = None
		self.random = None

class Solution:
	# @param head, a RandomListNode
	# @return a RandomListNode
	def copyRandomList(self, head):
		self.copyNodes(head)
#		print "Copy nodes done!"
		self.copyRandomLink(head)
#		print "Copy random link done!"
		return self.resetNodeLink(head)

	def copyNodes(self, head):
		if head == None:
			return
		pNode = head
		while not pNode == None:
			nodeCopy = RandomListNode(pNode.label)
			nodeCopy.next = pNode.next
			pNode.next = nodeCopy
			pNode = nodeCopy.next

	def copyRandomLink(self, head):
		if head == None:
			return
		pNode = head
		while not pNode == None:
			pNodeCopy = pNode.next
			if not pNode.random == None:
				pNodeCopy.random = pNode.random.next
			pNode = pNodeCopy.next

	def resetNodeLink(self, head):
		if head == None:
			return None
		pNode = head
		pNodeCopy = head.next
		pHeadCopy = pNodeCopy

		pNode.next = pNodeCopy.next
		pNode = pNode.next
		while not pNode == None:
			pNodeCopy.next = pNode.next
			pNodeCopy = pNodeCopy.next
			pNode.next = pNodeCopy.next
			pNode = pNode.next
		return pHeadCopy