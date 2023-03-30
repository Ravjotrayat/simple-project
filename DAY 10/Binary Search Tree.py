class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key
        
def inorder(root):
        if root is not None:
            inorder(root.left)
            print(str(root.key)+"->",end='')
            inorder(root.right)

def insert(node,key):
    if node is None:
        return Node(key)
    if key<node.key:
        node.left=insert(node.left,key)
    else:
        node.right=insert(node.right,key)
    return node

def deleteNode(node,key)::
    if root is None:
        return root
    if key<root.key:
        root.left=deleteNode(node.left,key)
    elif key>root.key:
        root.right=deleteNode(node.left,key)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp

        

root=None
root=insert(root,8)
root=insert(root,3)
root=insert(root,1)
root=insert(root,6)
root=insert(root,7)
root=insert(root,10)
root=insert(root,14)
root=insert(root,4)
            
inorder(root)
print()

print("\nDelete 10")
root=deleteNode(root,10)

inorder(root)
print()
