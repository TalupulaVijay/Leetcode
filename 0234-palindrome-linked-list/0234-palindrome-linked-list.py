# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True
        slow=fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        curr=slow
        prev=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        first=head
        second=prev
        while second:
            if first.val!=second.val:
                return False
            first=first.next
            second=second.next
        return True                

        