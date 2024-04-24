def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age < 18:
        raise ValueError("You must be at least 18 years old")
    else:
        print("Welcome! You are eligible.")

try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except ValueError :
    print("hello")
def fun(a:int,b:int):
    try:
        s=a/b
    except ValueError:
        print("value mistake")
a=input()
b=input()
try:
    fun(a,b)
except TypeError:
    print("only int can be accepted")
finally:
    print("done!")