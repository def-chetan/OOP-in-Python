class Employee:
    def __init__(self,name,salary):
         self.name=name
         self.salary=salary

    company = "Apple"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")


# class Programmer:
#     company = "Ball "
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")


class Programmer(Employee):
    company = "Ball "
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee("ram",123)
b = Programmer("syam",234)
b.show()


print(a.company, b.company)