# Source : https://oj.leetcode.com/problems/swap-nodes-in-pairs/
# Author : Cao Jin
# Date   : 2014-11-13

# ---------Title---------- 
# Swap Nodes in Pairs
# ---------Description---- 
# Given a linked list, swap every two adjacent nodes and return its head.

# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself
# can be changed.
# ---------Tags----------- 
# Linked List

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param a ListNode
	# @return a ListNode
	def swapPairs(self, head):
		if head == None:
			return None
		if head.next == None:
			return head
		p1 = head
		p2 = head.next
		p1.next = p2.next
		p2.next = p1
		head = p2
		pre = p1
		p1 = p1.next
		p2 = p1
		while p1 != None:
			if p1.next == None:
				return head
			p2 = p1.next
			p1.next = p2.next
			p2.next = p1
			pre.next = p2
			pre = p1
			p1 = p1.next
			p2 = p1
		return head