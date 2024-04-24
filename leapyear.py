"""y=int(input())
if(y%4==0):
    if(y%100==0 and y%400==0):
        print("leap year")
    elif(y%4==0 and y%100!=0):
        print("leap year")
    else:
        print("not a leap year")
else:
    print("not a leap year")
print("done!")"""
y=int(input())
if(y%4):
    if(y%100==0):
        if(y%400==0):
            print("leap year")
        else:
            print("a leap year")
    else:
        print("leap year")       
else:
    print("not a leap year")

#python3 -m pip install PythonTurtle
#import colorsys