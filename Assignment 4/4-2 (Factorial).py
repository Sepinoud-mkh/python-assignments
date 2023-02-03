number=int(input())
fact=1
i=0
while True:
    i=i+1
    fact=fact*i
    if fact==number:
        print("yes")
        break
    elif fact>number:
        print("no")
        break