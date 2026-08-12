class tryclass:
    name= "Chetan"      
    salary = 100000
    language = "python"


#init is a dunder method, the things that start with '__' are called dunder method
# a dunder method is automatically called


    def __init__(self):   
        print("This will be printed whatever you do")


ch= tryclass() # this will auto call the dunder method
ab=tryclass()
