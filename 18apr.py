"""s='abcpkjhuog'
s=s+'kk'
print(s)
print(s[1:5])
print(s[1:7:2])
print(s[7:1:-1])
print(s[-1])
print(s[::-1])"""
s="aishWaryA t"
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.capitalize())
m="5ais hWa ryA T"
print(m.title())
print(m.capitalize())
print(m.isupper())
print(m.isalnum())
print(m.isalpha())
print(m.isspace())
print(m.islower())
print(m.index('W'))
print(m.rindex('a'))
print(m.find('a'))
print(m.rfind('k'))
print(m.startswith('s ',3,6))
print(m.count('a'))
print(m.endswith('T'))
print(m.split('a'))
print(m.split())
print(s.partition('a'))
#type conversion
a=["1","2","3","4"]
a=" ".join(a)
print(a,type(a),a[0])
a="".join(a)
print(a,type(a),a[0])