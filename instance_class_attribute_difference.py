
class Employee:
    name= "Chetan"      # These are class attribute
    salary = 100000
    language = "python"

ch= Employee()

print(ch.name,ch.salary,ch.language)

ch.age = 20     # this is a instance attribute 
ch.name='Hello'
print (ch.age)
print(ch.name) # It prints the new name as instance attribute takes over class attribute