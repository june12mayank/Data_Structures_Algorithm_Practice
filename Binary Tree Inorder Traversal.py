#Given the root of a binary tree, return the inorder traversal of its nodes' values.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        lst=[]
        curr=root
        q=[]
        while True:
            if curr:
                q.append(curr)
                curr=curr.left
            elif q:
                curr=q.pop()
                lst.append(curr.val)
                curr=curr.right
            else:
                break
        return lst
            