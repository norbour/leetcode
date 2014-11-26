# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        p1 = head
        p2 = head
        pre = head
        for i in range(1, n):
            if p2.next != None:
                p2 = p2.next
            else:
                return head
        while p2.next != None:
            pre = p1
            p1 = p1.next
            p2 = p2.next
        if head == p1:
            return p1.next
        else:
            pre.next = p1.next
            return head