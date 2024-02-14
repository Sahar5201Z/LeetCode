# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head 

        result = ListNode()
        current =result
        while head:
            while head.next and head.val == head.next.val:
                head = head.next
            current.next =ListNode(head.val)
            current = current.next

            head=head.next

        return result.next


        