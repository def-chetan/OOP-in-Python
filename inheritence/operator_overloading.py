class number:

    def __init__(self,n):
        self.n=n

    def __add__(self, num):
        return self.n + num.n
        


n1= number(1)
n2= number(3)


print (n1+n2) # this means n1.__add__(n2)
c= n1.__add__(n2)

print(c)