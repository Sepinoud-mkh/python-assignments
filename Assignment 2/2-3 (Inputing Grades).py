a=True
sum=0
num=0
while(a):
    grade=input("Enter a grade:")
    if grade=="exit":
        break
    else:
        sum=sum+int(grade)
        num=num+1
print(sum/num)