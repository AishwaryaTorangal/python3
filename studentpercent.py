a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
sum=a+b+c+d+e
p=sum/500
p=p*100
if(p>=75):
    print("grade A")
elif(p>=60 and p<=74):
    print("grade B")
elif(p>=35 and p<=59):
    print("grade C")
else:
    print("fail!")   