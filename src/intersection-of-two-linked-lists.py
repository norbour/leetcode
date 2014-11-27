# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None:
            return None
        lengthA = self.getLinkedListLength(headA)
        lengthB = self.getLinkedListLength(headB)
        nodeA = headA
        nodeB = headB
        if lengthA > lengthB:
            for i in range(0, lengthA - lengthB):
                nodeA = nodeA.next
        elif lengthB > lengthA:
            for i in range(0, lengthB - lengthA):
                nodeB = nodeB.next
        while nodeA != None and nodeB != None:
            if nodeA == nodeB:
                return nodeA
            nodeA = nodeA.next
            nodeB = nodeB.next
        return None
    
    def getLinkedListLength(self, head):
        if head == None:
            return 0
        length = 0
        node = head
        while node != None:
            length = length + 1
            node = node.next
        return length