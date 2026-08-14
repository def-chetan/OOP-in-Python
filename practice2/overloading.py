class complex:
    def __init__(self,n):
        self.n = n


    def __add__(self, another):
        return self.n +another.n

    def __mul__(self, another):
        return self.n * another.n


n1=int(input())

n2=int(input())

print(n1+n2)    #this calls n1._add_(n2)
print (n1*n2)
