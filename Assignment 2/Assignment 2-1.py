import random

a=True
attempts=0
print("Welcome!\nThe computer thinks about a number,Can you guess it?")
com_Num=random.randint(1,100)
print("Here is a hint:The number is between 1 and 100")
while(a):
    num=int(input("Enter the number?:"))
    if com_Num<num:
        attempts=attempts+1
        print("go down")
    elif com_Num>num:
        attempts=attempts+1
        print("go up")
    elif com_Num==num:
        attempts=attempts+1
        a=False
print("You guessed it correctly after %d attempts"%attempts)