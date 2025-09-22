# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import Counter
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        res=[]
        curr=head
        while curr:
            res.append(curr.val)
            curr=curr.next
        fre=Counter(res)
        unique=[val for val in res if fre[val]==1]    
        dummy=ListNode(0)
        temp=dummy
        for i in unique:
            temp.next=ListNode(i)
            temp=temp.next
        return dummy.next    
                                

        