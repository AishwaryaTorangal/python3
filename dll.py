class node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
        self.prev=None
class dll:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
    def IFrnt(self, data):
        new = node(data)
        if self.head==None:
            self.head=new 
            self.tail=self.head
        else:
            new.next=self.head
            self.head.prev=new
            self.head=new
    def IEnd(self,data):
        new=node(data)
        if self.head==None:
            self.head=new
            self.tail=self.head
        else:
            self.tail.next=new
            new.prev=self.tail
            self.tail=new
    def Print(self):
        c=0
        if self.head==None:
            print("list is empty")
        i=self.head
        while i:
            print(i.data)
            c=c+1
            i=i.next
        print("number of nodes:",c)
    def DFrnt(self):
        if self.head == None:
            print("List is empty")
        elif self.head.next == None:  # Only one node in the list
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def DEnd(self):
        if self.head == None:
            print("list is empty")
        elif self.head == self.tail:  # Only one node in the list
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None  # Update next pointer of new tail

    def rev(self):
        if self.head!=None:
            p=None
            curr=self.head
            n=self.head.next
            while curr:
                curr.next=p
                p=curr
                curr.prev=p
                curr=n
                if n:
                    n=n.next
            self.head=p
        else:
            print("list is empty")
        
l=[1,2,3,4,5]
p=dll()
for i in range(len(l)):
    p.IEnd(l[i])
    #p.IFrnt(l[i])
p.Print()
p.DFrnt()
p.Print()
p.DEnd()
p.Print()
p.rev()
p.Print()



#swap a,b=b,a
#curr.next,curr.prev=curr.prev,curr.next
#curr=curr.prev
