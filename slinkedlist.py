class node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
class a:
    def __init__(self) -> None:
        self.head=None
    def IEnd(self,data):
        new=node(data)
        if self.head==None:
            self.head=new
        else:
            i=self.head
            while i.next:
                i=i.next 
            i.next=new
    
    def IFrnt(self,data):
        new=node(data)
        if self.head==None:
            self.head=new
        else:
            new.next=self.head
            self.head=new
    
    def printing(self):
        c=0
        if self.head==None:
            print("list is empty")
        i=self.head
        while i:
            print(i.data)
            c=c+1
            i=i.next
        print("number of nodes:",c)
    
    def DEnd(self):
        if self.head==None:
            return
        elif self.head.next==None:
            self.head=None
        else:
            i=self.head
            prev=None
            while i.next:
                prev=i
                i=i.next
            prev.next=None
    def DFrnt(self):
        if self.head==None:
            return
        elif self.head.next==None:
            self.head=None
        else:
            self.head=self.head.next
    def rev(self):
        p=None
        curr=self.head
        n=self.head.next
        while curr:
            curr.next=p
            p=curr
            curr=n
            if n:
                n=n.next
            self.head=p
l=[1,2,3,4,5]
p=a()
for i in range(len(l)):
    p.IEnd(l[i])
    p.IFrnt(l[i])
p.printing()
p.DEnd()
p.printing()
p.DFrnt()
p.printing()
p.printing()
p.rev()
p.printing()

                
                
            

            
            
