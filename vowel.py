"""a=input()
match a:
    case 'a':
        print("vowel") 
    case 'e':
        print("vowel")       
    case 'i':
        print("vowel")       
    case 'o':
        print("vowel")       
    case 'u':
        print("vowel")       
    case 'A':
        print("vowel")       
    case 'E':
        print("vowel") 
    case 'I':
        print("vowel")
    case 'O':
        print("vowel")           
    case 'U':
        print("vowel")
    case _:
        print("consonant")"""
a=input()
s='aeiouAEIOU'
if(a in s): #a in 'aeiouAEIOU'
    print("vowel")
else:
    print("consonant")
    