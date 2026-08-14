class emp:

    def __init__(self):
        print("thisis a constructur of emp class")
    a=1
    pass

class programmer(emp):
    def __init__(self):
            print("thisis a constructur of programmer class")
    b=2
    pass

class coder(programmer):
    def __init__(self):
            super().__init__()

            print("thisis a constructur of coder class")
    c=4


obj=coder()
# obj2=programmer()
# obj3=emp()

print(obj.a,obj.b, obj.c)