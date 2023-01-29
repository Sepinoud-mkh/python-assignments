length=int(input("Enetr the wanted length of your snake:"))
for i in range(length):
    if(i%2==0):
        print("*",end="")
    else:
        print("#",end="")