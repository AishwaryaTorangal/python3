"""class node:
    def __init__(self,m) -> None:
        self.m=m
        self.l=None
a=node(1)
b=node(2)
c=node(3)
a.l=b
b.l=c
print(a,#<__main__.node object at 0x0000016A2AC25B80> 
      a.m,# 1 
      a.l,#<__main__.node object at 0x0000016A2AC25B20>
      b,#<__main__.node object at 0x0000026AD5F85B20> 
      a.l.m,# 2 
      a.l.l,# <__main__.node object at 0x0000016A2AC25BE0>
      b.l)# <__main__.node object at 0x0000016A2AC25BE0>"""
class node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
#insert at end
class IEnd:
    def __init__(self) -> None:
        self.head=None
    def insertAtEnd(self,data):
        new=node(data)
        if self.head==None:
            self.head=new
        else:
            i=self.head
            while i.next:
                i=i.next
            i.next=new 
    #printing linked list elements
    def printing(self):
        if self.head==None:
            return
        else:
            i=self.head
            while i:
                print(i.data)
                i=i.next
#insert at front
class IFrt:
    def __init__(self) -> None:
        self.head=None
    def insertAtFront(self,data):
        new=node(data)
        if self.head==None:
            self.head=new
        else:
            new.next=self.head
            self.head=new

    #printing linked list elements
    def printings(self):
        if self.head==None:
            return
        else:
            i=self.head
            while i:
                print(i.data)
                i=i.next
    #length of LL
    def length(self):
        c=0
        i=self.head
        while i:
            c=c+1
            i=i.next
        return c


l=[1,2,3,4,5]
a=IEnd()
b=IFrt()
for i in range(len(l)):
    a.insertAtEnd(l[i])
    b.insertAtFront(l[i])
a.printing()
b.printings()
print("no.of nodes=",b.length())
      
