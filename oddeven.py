"""a=int(input())
b=int(input())
d=a+b
print(d)
if(d%2==0):
    print(d,"is","even")
else:
    print(d,"is","odd")
print("done!")"""

#without arithmetic op
a=int(input())
if((a and 1)==0):  #a&1==0
    print("even")
else:
    print("odd")
