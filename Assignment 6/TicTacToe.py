def show():
    for row in game_board:
        for cell in row:
            print(cell,end=" ")
    print()

game_board = [["-", "-", "-"],
              ["-", "-", "-"],
              ["-", "-", "-"]]

show()

print("Player 1")

row = int(input("Enetr the desired number of row:"))
col = int(input("Enetr the desired number of col:"))

game_board[row][col]="X"

show()

print("Player 2")

row = int(input("Enetr the desired number of row:"))
col = int(input("Enetr the desired number of col:"))

game_board[row][col]="O"

show()