# Store info of 5 students in a school

class School:
    school_name="ABC School"
    def __init__(self, name , age, grade):
        self.name=name
        self.age = age
        self.grade= grade
s1= School("jonny",12, 5)

print(s1.name,s1.age,s1.grade,s1.school_name)
s2= School("toni",16, 7)
print(s2.name,s2.age,s2.grade,s2.school_name)
s3= School("moni",15, 6)
print(s3.name,s3.age,s3.grade,s3.school_name)
s4= School("soni",11, 4)
print(s4.name,s4.age,s4.grade,s4.school_name)
s5= School("roni",16, 8)
print(s5.name,s5.age,s5.grade,s5.school_name)
        

