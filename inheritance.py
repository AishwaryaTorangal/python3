class a:
    def __init__(self) -> None:
        pass
    def fun1(self):
        print("fun1")
        #self.fun1() recurrsion
    def fun2(self):
        print("fun2")
class b(a):
    def fun3(self):
        print("fun3")
        self.fun2()
    def fun4(self):
        print("fun4")
class c(b,a):
    def fun5(self):
        print("fun5")
    def fun6(self):
        print("fun6")
class d(b):
    def fun7(self):
        print("fun7")
    def fun8(self):
        print("fun8")        
p=a()
q=b()
r=c()
s=d()
p.fun1()
p.fun2()
q.fun1()
q.fun2()
q.fun3()
q.fun4()
