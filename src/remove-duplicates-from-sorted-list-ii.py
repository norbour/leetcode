# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None:
            return None
        if head.next == None:
            return head
            
        node = ListNode(-1)
        node.next = head
        head = node
        
        p = node.next
        dup = False
        while not p == None and not p.next == None:
            while not p.next == None and p.val == p.next.val:
                p = p.next
                dup = True
            if dup:
                p = p.next
                dup = False
                node.next = p
            else:
                node.next = p
                node = p
                p = p.next
            
        return head.next