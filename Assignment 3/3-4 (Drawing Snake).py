length=int(input("Enetr the length of your snake:"))
for i in length:
    if(i%2==0):
        print("*",end="")
    else:
        print("#",end="")