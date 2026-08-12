class tryclass:
    name= "Chetan"      
    salary = 100000
    language = "python"


#init is a dunder method, the things that start with '__' are called dunder method
# a dunder method is automatically called


    def __init__(self,name,salary,age):   
        self.name=name
        self.salary=salary
        self.age= age
        print("This also will be printed whatever you do")
        print(f"name={self.name} , slary={self.salary} , age= {self.salary}")

# ch= tryclass()
ab=tryclass("ram",40000,12)
