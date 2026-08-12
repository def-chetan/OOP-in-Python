class Employee:
    name= "Chetan"      
    salary = 100000
    language = "python"

    # we can make finctions inside a class
    # def getInfo():
    #     print(f"name = {name} , salary= {salary}")    # this is wrong

    def getInfo(self):   # for that we need to pass a argument
        print(f"name = {self.name} , salary= {self.salary}")    # this is right


ch= Employee()

# the follow below both do the same
ch.getInfo()
ch.name='Hello'
Employee.getInfo(ch) #as instance attribute gets more priority