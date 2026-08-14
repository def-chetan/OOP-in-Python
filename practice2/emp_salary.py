class emp:
    percent=10
    # def __init__(self,sal):
    #     self.sal=sal
        

    # def s_double(self):
    #     return self.sal*2

    @property
    def salaryinc(self):
        return (self.s+(self.s * self.percent/100))

    @salaryinc.setter
    def salaryinc(self,s):
        self.s=s
        if s>=1000 and s<=10000:
            self.percent = 20
        else:
            self.percent=30
    

ob1=emp()
# print(ob1.sal)
# a=ob1.s_double()

# print(a)
ob1.salaryinc=10000
print(ob1.salaryinc)