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
	            
        table = []
        for i in range(0, 1000):
            table.append(0)

        node = head
        table[node.val] = 1
	        
        while not node.next == None:
            if not table[node.next.val]:
                node = node.next
                table[node.val] = 1
            else:
                node.next = node.next.next
        return head