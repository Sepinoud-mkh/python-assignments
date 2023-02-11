def chessBoard(n,m):
    for i in range(n):
        for j in range(m):
            if (i%2==0 and j%2==0) or (i%2!=0 and j%2!=0):
                print("#",end="")
            else:
                print("*",end="")
        print("")

row,column=map(int,input("Enter row and column:").split())
chessBoard(row,column)