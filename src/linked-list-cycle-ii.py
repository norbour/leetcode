class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head == None:
            return None
        slow = head
        fast = head
        while not slow == None and not fast == None:
            slow = slow.next
            if not fast.next == None:
                fast = fast.next.next
            else:
                break
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None 