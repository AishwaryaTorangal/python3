"""class cse:
    def __init__(self,name,roll) -> None:
        self.n=name
        self.rn=roll
    def fun(self):
        print(self.n,s1.n)

    
s1=cse("aishu",7)
s2=cse("abc",9)
s1.fun()
print(s1.n,s2.n) """
"""class circle:
    def __init__(self,ra) -> None:
        self.R=r
    def printing(self):
        print(3.14*self.R**2)
class rectangle:
    def __init__(self,le,br) -> None:
        self.L=le
        self.B=br
    def printing(self):
        print(self.B*self.L)
l=int(input())
b=int(input())
r=int(input())
o=circle(r)
o1=rectangle(l,b)
o.printing()
o1.printing()"""
class circle:
    def printing(self,ra):
        self.R=r
        print(3.14*self.R**2)
class rectangle:
    def printing(self,le,br):
        self.L=le
        self.B=br
        print(self.B*self.L)
l=int(input())
b=int(input())
r=int(input())
o=circle()
o1=rectangle()
o.printing(r)
o1.printing(l,b)
