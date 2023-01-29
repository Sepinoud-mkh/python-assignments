import random


n=int(input())
array=[]
for i in range(n):
    num=random.randint(0,100)
    if num not in array:
        array.append(num)
print(array)
