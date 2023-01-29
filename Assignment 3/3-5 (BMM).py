num_1,num_2=map(int,(input("Please enter 2 numbers:")).split())
if num_1>num_2:
    num_1,num_2=num_2,num_1
for i in range(1,(num_1)+1):
    if (num_1)%i==0 and (num_2)%i==0:
        BMM=i
print("The bmm is:",BMM)