# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        p1 = l1
        p2 = l2
        l3 = ListNode(0)
        p3 = l3
        while not p1 == None and not p2 == None:
            if p1.val < p2.val:
                p3.next = p1
                p1 = p1.next
            else:
                p3.next = p2
                p2 = p2.next
            p3 = p3.next
        if not p1 == None:
            while not p1 == None:
                p3.next = p1
                p1 = p1.next
                p3 = p3.next
        if not p2 == None:
            while not p2 == None:
                p3.next = p2
                p2 = p2.next
                p3 = p3.next
        return l3.next
            
            