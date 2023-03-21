import pyfiglet

def show():
    for row in game_board:
        for cell in row:
            print(cell,end=" ")
        print()


def check_game():
    for i in range(3):
        if game_board[i][0]==game_board[i][1]==game_board[i][2]=="X" or game_board[0][i]==game_board[1][i]==game_board[2][i]=="X" or game_board[0][0]==game_board[1][1]==game_board[2][2]=="X" or game_board[0][2]==game_board[1][1]==game_board[2][0]=="X":
            print("player 1 Wins")
        elif game_board[i][0]==game_board[i][1]==game_board[i][2]=="O" or game_board[0][i]==game_board[1][i]==game_board[2][i]=="O" or game_board[0][0]==game_board[1][1]==game_board[2][2]=="O" or game_board[0][2]==game_board[1][1]==game_board[2][0]=="O":
            print("player 2 Wins")

title = pyfiglet.figlet_format("TicTacToe",font="bubble")

Player_1 = input("Please enter your name:")
Player_2 = input("Please enter your name:")


game_board = [["-", "-", "-"],
              ["-", "-", "-"],
              ["-", "-", "-"]]

show()

while True:
    print("%s,it's your turn"%Player_1)
    
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

    print("%s,it's your turn"%Player 2)

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