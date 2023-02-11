def multiply(n,m):
    for i in range(1,n+1):
        for j in range(1,m+1):
            print(i*j,end="")
        print("")

row,column=map(int,input("Enter row and column:").split())
multiply(row,column)