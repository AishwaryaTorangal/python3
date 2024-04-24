"""#binary search
l=[1,2,3,4,5,6]
se=4
si=0
li=len(l)-1
while si<=li:
    mid=(si+li)//2
    if l[mid]==se:
        print("ele found",l[mid])
        break
    elif l[mid]<se:
        si=mid+1
    else:
        li=mid-1
else:
    print("ele not found")"""
#stack implementation
l=[1,2,3,4,5]
l.append(9)
print(l)
l.pop()
print(l)