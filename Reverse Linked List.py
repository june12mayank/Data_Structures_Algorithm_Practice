#Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev=None
        temp=head
        while(temp):
            nxt=temp.next
            temp.next=prev
            prev=temp
            temp=nxt
        return prev
            