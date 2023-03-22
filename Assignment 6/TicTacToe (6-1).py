import pyfiglet
import random
import time
from termcolor import colored


def show():
    for row in game_board:
        for cell in row:
            print(cell,end=" ")
        print()


def check_game():
    num=0
    for i in range(3):
        if game_board[i][0]==game_board[i][1]==game_board[i][2]==colored("X","red") or game_board[0][i]==game_board[1][i]==game_board[2][i]==colored("X","red") or game_board[0][0]==game_board[1][1]==game_board[2][2]==colored("X","red") or game_board[0][2]==game_board[1][1]==game_board[2][0]==colored("X","red"):
            print("%s wins"%Player_1)
            end=time.time()
            print("Time:",end-start)
            exit()
        elif game_board[i][0]==game_board[i][1]==game_board[i][2]==colored("O","blue") or game_board[0][i]==game_board[1][i]==game_board[2][i]==colored("O","blue") or game_board[0][0]==game_board[1][1]==game_board[2][2]==colored("O","blue") or game_board[0][2]==game_board[1][1]==game_board[2][0]==colored("O","blue"):
            print("%s wins"%Player_2)
            end=time.time()
            print("Time:",end-start)
            exit()
        for j in range(3):
            if game_board[i][j]=="-":
                num=num+1
    if num==0:
        if not(game_board[i][0]==game_board[i][1]==game_board[i][2]=="X" or game_board[0][i]==game_board[1][i]==game_board[2][i]=="X" or game_board[0][0]==game_board[1][1]==game_board[2][2]=="X" or game_board[0][2]==game_board[1][1]==game_board[2][0]=="X" or game_board[i][0]==game_board[i][1]==game_board[i][2]=="O" or game_board[0][i]==game_board[1][i]==game_board[2][i]=="O" or game_board[0][0]==game_board[1][1]==game_board[2][2]=="O" or game_board[0][2]==game_board[1][1]==game_board[2][0]=="O"):
            print("no one wins")
            end=time.time()
            print("Time:",end-start)
            exit()


title=pyfiglet.figlet_format("TicTacToe",font="bubble")
print(title)

computer_Or_Player=int(input("Do you want to play with computer or with a player?\nif you want to play with computer please enter 1,if not please enter 2:"))

Player_1=input("\nPlease enter your name:")

if computer_Or_Player==2:
    Player_2=input("Please enter your name:")
else:
    Player_2="Computer"


game_board=[["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]]

show()

start=time.time()

while True:
    print("%s,it's your turn"%Player_1)
    
    while True:
        row=int(input("Enetr the desired number of row:"))
        col=int(input("Enetr the desired number of col:"))

        if 0<=row<=2 and 0<=col<=2:
            if game_board[row][col]=="-":
                game_board[row][col]=colored("X","red")
                break
            else:
                print("The desired place in full,please select another cell")
        else:
            print("Out of specified range,selet between 0 and 2")

    show()
    check_game()

    print("%s,it's your turn"%Player_2)

    while True:
        if computer_Or_Player==2:
            row=int(input("Enetr the desired number of row:"))
            col=int(input("Enetr the desired number of col:"))
        else:
            row=random.randint(0,2)
            col=random.randint(0,2)

        if 0<=row<=2 and 0<=col<=2:
            if game_board[row][col]=="-":
                game_board[row][col]=colored("O","blue")
                break
            else:
                print("The desired place in full,please select another cell")
        else:
            print("Out of specified raneg,selet between 0 and 2")

    show()
    check_game()