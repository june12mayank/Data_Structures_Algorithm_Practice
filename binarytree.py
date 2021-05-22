# number of labeled trees: [(2n)!/(n+1)!n!]* n!
class Node:
    def __init__(self,key) -> None:
        self.left=None
        self.right=None
        self.val=key

def inorder(temp):
    if not temp:
        return
    inorder(temp.left)
    print(temp.val,end=" ")
    inorder(temp.right)

def insert(root,val):
    if not root:
        root= Node(val)
        return 
    q=[]
    q.append(root)
    while(len(q)):
        temp=q.pop(0)

        if(not temp.left):
            temp.left=Node(val)
            break
        else:
            q.append(temp.left)

        if(not temp.right):
            temp.right=Node(val)
            break
        else:
            q.append(temp.right)

def deleteDeepest(root,d_node):
    q=[root]
    while(len(q)):
        t=q.pop(0)
        if t==d_node:
            t=None
            return
        if t.right:
            if t.right==d_node:
                t.right=None
                return
            else:
                q.append(t.right)
        if t.left:
            if t.left==d_node:
                t.left=None
                return
            else:
                q.append(t.left)

def deletion(root,val):
    if not root:
        return
    if not root.left and not root.right:
        if root.val==val:
            return
        else:
            return root
    key_node=None
    q=[root]
    while(len(q)):
        temp=q.pop(0)
        if temp.val==val:
            key_node=temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
        
    if key_node:
        key_node.val=temp.val
        deleteDeepest(root,temp)
    return root


if __name__=='__main__':
    k=Node(6)
    for i in range(5):
        insert(k,i)
    print(inorder(k))
    deletion(k,3)
    print(inorder(k))
