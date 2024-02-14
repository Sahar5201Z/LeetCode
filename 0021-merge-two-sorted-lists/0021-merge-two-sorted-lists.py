# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        sortlist=dummy
        while (list1 and list2):
            if(list1.val<list2.val):
                sortlist.next=list1
                list1=list1.next
            else:
                sortlist.next=list2
                list2=list2.next
            sortlist = sortlist.next
        if list1:
            sortlist.next=list1
            
        if list2:
            sortlist.next=list2
            

        return dummy.next

######if it was 2 array instead of 2 linklist
"""class Solution:
    def mergeTwoLists(self, list1: List[int], list2: List[int]) -> List[int]:
        sortlist=[]
        i=0
        j=0
        while i< len(list1) and j< len(list2): 

            if(list1[i]<=list2[j]):
                sortlist.append(list1[i])
                i+=1
                
            else:
                sortlist.append(list2[j])
                j+=1

        while(i< len(list1)):
            sortlist.append(list1[i])
            i+=1            
                
        while(j< len(list2)):    
            sortlist.append(list2[j])
            j+=1

        return sortlist"""


        