class twod:
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def show(self):
        print(f"{self.i}i+ {self.j}j")

    
class threed(twod):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k

    def show(self):
            print(f"{self.i}i+ {self.j}j + {self.k}k")

    
m=twod(1,2)
m.show()

n=threed(1,2,3)
n.show()


