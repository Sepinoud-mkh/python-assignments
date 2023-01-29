num_1,num_2=map(int,(input("Please enter 2 numbers:")).split())
if num_1>num_2:
    Bnumber=num_1
else:
    Bnumber=num_2
for i in range(Bnumber,((num_1)*(num_2))+1):
    if i%(num_1)==0 and i%(num_2)==0:
        KMM=i
print("The kmm is:",KMM)