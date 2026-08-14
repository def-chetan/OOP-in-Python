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
    c=5


obj=coder()
obj2=programmer()
obj3=emp()  #these will run thre respective constructor of the calss

#but some time we want we want that the constructor of the parant class is also run, so for that we use the super class


print(obj.a,obj.b, obj.c)

print()
print()
supobj=coder() #will run the constructor of the parent class also