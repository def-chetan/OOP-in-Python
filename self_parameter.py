class Employee:
    name= "Chetan"      
    salary = 100000
    language = "python"

    # we can make finctions inside a class
    def getInfo():
        print(f"name = {name} , salary= {salary}")    # this is wrong

ch= Employee()

print(ch.name,ch.salary,ch.language)

ch.age = 20     
ch.name='Hello'
print (ch.age)
print(ch.name)