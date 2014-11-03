# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head == None:
            return False
        slow = head
        fast = head
        cycle = False
        while not slow == None and not fast == None:
            slow = slow.next
            if not fast.next == None:
                fast = fast.next.next
            else:
                break
            if slow == fast:
                cycle = True
                break
        return cycle