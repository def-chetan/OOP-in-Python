#Syntax for making class is 
#   class class_name:

class Employee:
    name= "Chetan"      # These are class attribute
    salary = 100000
    language = "python"

# Syntax for making object is 
# variabe = class_name()

ch= Employee()

# to use the attribute of a class we use '.' 
# variable.attribute
print(ch.name,ch.salary,ch.language)

#object attribute

ch.age = 20     # this is a object attribute 

print (ch.age)