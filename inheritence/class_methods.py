# class emp:
#     a=1
#     def show(self):
#         print(f"{self.a}")
    

# obj=emp()
# # obj2=programmer()
# # obj3=emp()
# obj.a = 33
# obj.show() # this will print 33 as. instance attribute gets more priority

class emp:
    a=1
    @classmethod
    #this will access the direct class
    def show(cls):
        print(f"{cls.a}")
    

obj=emp()
# obj2=programmer()
# obj3=emp()
obj.a = 33
obj.show() # this will print 33 as. instance attribute gets more priority

