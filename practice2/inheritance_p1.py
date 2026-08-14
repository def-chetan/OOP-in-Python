class animal:
    def __init__(self):
        print("animal")
        

class pet(animal):
    def __init__(self):
        super().__init__()
        print("pet is animal")

class dog(pet):
    def __init__(self):
        super().__init__()
        print("dog is pet")

    @staticmethod
    def bark():
        print("dog is barking")


o1= dog()
o1.bark()

