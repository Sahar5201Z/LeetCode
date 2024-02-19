# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        '''pointerA = headA
        while pointerA:
            pointerB = headB
            while pointerB:
                if(pointerA is pointerB):
                    return pointerA
                pointerB=pointerB.next
            pointerA=pointerA.next
        
        return None'''
        
        seen = set()
        pointerA = headA
        while pointerA:
            seen.add(pointerA)
            pointerA = pointerA.next
        
        pointerB = headB
        while pointerB:
            if pointerB in seen:
                return pointerB
            pointerB = pointerB.next
        
        return None
        