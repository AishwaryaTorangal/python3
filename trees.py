#binary tree representation
class node:
    def __init__(self,data) -> None:
        self.data=data
        self.r=None
        self.l=None
root=node(4)
root.l=node(2)
root.l.l=node(1)
root.r=node(7)
root.r.l=node(9)
root.r.r=node(6)
root.l.r=node(3)
"""print(root.data)
print(root.l.data)
print(root.r.data)
print(root.l.l.data)
print(root.l.r.data)"""
#dfs(deapth first search) traversal
def dfs_preorder(root):
    if root==None:
        return
    print(root.data)
    dfs_preorder(root.l)
    dfs_preorder(root.r)

def dfs_inorder(root):
    if root==None:
        return
    dfs_inorder(root.l)
    print(root.data)
    dfs_inorder(root.r)
    
def dfs_postorder(root):
    if root==None:
        return
    dfs_postorder(root.l)
    dfs_postorder(root.r)
    print(root.data)

print("preorder_traversal")
dfs_preorder(root)
print("inorder_traversal")
dfs_inorder(root)
print("postorder_traversal")
dfs_postorder(root)


