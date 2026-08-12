class Employee:
    name= "Chetan"      
    salary = 100000
    language = "python"

    # we can make finctions inside a class
    # def getInfo():
    #     print(f"name = {name} , salary= {salary}")    # this is wrong

    def getInfo(self):   # for that we need to pass a argument
        print(f"name = {self.name} , salary= {self.salary}")    # this is wrong

ch= Employee()

# the follow below both do the same
ch.getInfo()
Employee.getInfo(ch)