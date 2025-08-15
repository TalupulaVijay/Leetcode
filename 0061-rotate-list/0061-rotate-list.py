# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k==0:
            return head
        c=1
        temp=head
        while temp.next:
            temp=temp.next
            c+=1
        k=k%c
        if k==0:
            return head
        new_last=head
        for _ in range(c-k-1):
            new_last=new_last.next 
        new_head=new_last.next
        new_last.next=None
        temp.next=head
        return new_head  
        