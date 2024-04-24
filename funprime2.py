a=int(input())
b=int(input())
def prime(n:int):
    for i in range(2,n):
        if(n%i==0):
            return False
    else:
        return True
for i in range(a,b+1):
    if prime(i):
        if i!=1:
            print(i)

    


    