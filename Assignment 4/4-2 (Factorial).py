number=int(input())
num=number
while num>1:
    for i in range(2,num+1):
        if num%i==0:
            num=num/i
        else:
            break
if (num==1):
    print("yes")
else:
    print("no")