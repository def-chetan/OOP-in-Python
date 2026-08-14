class emp:
    a=1
    @classmethod
    #this will access the direct class
    def show(cls):
        print(f"{cls.a}")

    @property
    def name(self):
        return f"{self.fname}{self.lname}"
    

    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]

obj=emp()
# obj2=programmer()
# obj3=emp()
obj.a = 33
obj.name="Chetan Lohia"
obj.show() 
print(obj.name)