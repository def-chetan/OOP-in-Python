class calculator:

    def __init__(self,num):
        self.num= num

    def functions(self):
        a=self.num**2
        b=self.num**3
        c=self.num**(1/2)

        print(f"square={a},cube={b}, sqrt={c}")


num= calculator(9)
num.functions()

