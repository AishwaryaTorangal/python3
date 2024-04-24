a=int(input())
for i in range(2,a):
    if(a%i==0):
        print(a,"is not a prime num")
        break
else:
    print(a,"is prime num")
