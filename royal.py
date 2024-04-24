class royalenfield:
    def __init__(self,model_name,colour,milage) -> None:
        self.mo=model_name
        self.c=colour
        self.mi=milage
r1=royalenfield("a","maroon",80)
r2=royalenfield("b","black",85)
r3=royalenfield("c","browm",90)
print(r1.mo,r1.c,r1.mi)
print(r2.mo,r2.c,r2.mi)
print(r3.mo,r3.c,r3.mi)