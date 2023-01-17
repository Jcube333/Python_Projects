import random

a=random.randrange(1,10)

x=int(input("Enter a number between 1 to 10 :"))

while x!=a:
    if a>x:
        print("Your number is too small")
        x=int(input("Enter a number again: "))
    elif a<x:
        print("Your Number is too large")
        x=int(input("Enter a number again: "))
   
print("Congrats, you've completed the game. The number matched.")   

