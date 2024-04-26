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
#breadth first search
q=[]
q.append(root)
while q:
    a=q.pop(0)
    print(a.data)
    if a.l!=None:
        q.append(a.l)
    if a.r!=None:
        q.append(a.r)
    