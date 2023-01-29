import random
a=input("Would you like to throw a dice?\nPlease enter YES if you like:")
if a=="YES":
    num=random.randint(1,6)
    if num=="6":
        num=random.randint(1,6)
    else:
        num=num
    print(num)
else:
    print("We'll try again later :)")