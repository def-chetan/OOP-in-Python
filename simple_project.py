#GUESS THE NUMBER

import random
n=random.randint(1,100)
a=-1
g=0
list=[1,100]
while (a!=n):
    a= int(input("Guess a number:"))
    if(a>=1 and a<=100):
        g+=1
        if (a<n):
            if(a>list[0]):
                list[0]=a
            print("The number is grater")
        elif (a>n):
            if(a<list[1]):
                list[1]=a
            print("The number is smaller")
        elif (a==n):
            list.append(a)
            print (f"BINGO!!!!!! CORRECT GUESS!!!\nAttempts:{g} ")
    else:
        print("Something went wrong")


    print ("your numebr is in between " , list)





