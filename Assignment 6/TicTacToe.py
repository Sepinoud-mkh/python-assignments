def show():
    for row in game_board:
        for cell in row:
            print(cell,end=" ")
        print()




game_board = [["-", "-", "-"],
              ["-", "-", "-"],
              ["-", "-", "-"]]

show()

while True:
    print("Player 1")
    
    while True:
        row = int(input("Enetr the desired number of row:"))
        col = int(input("Enetr the desired number of col:"))

        if 0<=row<=2 and 0<=col<=2:
            if game_board[row][col] == "-":
                game_board[row][col] ="X"
                break
            else:
                print("The desired place in full,please select another cell")
        else:
            print("Out of specified raneg,selet between 0 and 2")

    show()

    print("Player 2")

    while True:
        row = int(input("Enetr the desired number of row:"))
        col = int(input("Enetr the desired number of col:"))
        
        if 0<=row<=2 and 0<=col<=2:
            if game_board[row][col] == "-":
                game_board[row][col] = "O"
                break
            else:
                print("The desired place in full,please select another cell")
        else:
            print("Out of specified raneg,selet between 0 and 2")

    show()