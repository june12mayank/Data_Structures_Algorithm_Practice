#Write a function to delete a node in a singly-linked list. 
# You will not be given access to the head of the list, 
# instead you will be given access to the node to be deleted directly.

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        node.val=node.next.val
        node.next=node.next.next
        