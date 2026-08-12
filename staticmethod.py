class Employee:
    name= "Chetan"      
    salary = 100000
    language = "python"

    def getInfo(self):  
        print(f"name = {self.name} , salary= {self.salary}")  

    # some funstions dont need any parameter , is doesnt need to use any of the variables , for that we use staticmethod and for that we use @staticmethod
    @staticmethod
    def hi():
        print("hello brother")

ch= Employee()

# the follow below both do the same
ch.getInfo()
ch.name='Hello'
Employee.getInfo(ch) #as instance attribute gets more priority
ch.hi()