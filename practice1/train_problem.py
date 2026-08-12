class train:

    def __init__(self, tn, fr, to):
        self.tn=tn
        self.fr = fr
        self.to= to

    def book(self):
        print(f"train no {self.tn} from {self.fr} to { self.to} is booked")

    def getstatus(self):
        print(f"train no {self.tn} from {self.fr} to { self.to} is riunning in time")

    def getfare(self):
        print(f"train no {self.tn} from {self.fr} to { self.to} fare is 2222")


t= train(1001,"chennai","pondicherry")
t.book()
t.getstatus()
t.getfare()
