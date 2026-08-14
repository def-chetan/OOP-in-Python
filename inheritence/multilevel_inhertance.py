class emp:
    a=1
    pass

class programmer(emp):
    b=2
    pass

class coder(programmer):
    c=3


obj=coder()

print(obj.a,obj.b, obj.c)