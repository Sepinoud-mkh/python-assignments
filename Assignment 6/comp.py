import random


computer_Or_Player=int(input("Do you want to play with computer or with a player?\nif you want to play with computer please enter 1,if not please enter 2"))

if computer_Or_Player==2:
    






def show():
    for row in game_board:
        for cell in row:
            print(cell,end=" ")
        print()

player_1=input("Enter your name:")

game_board=[["-","-","-"],
            ["-","-","-"],
            ["-","-","-"]]

show()

while True:
    print("\n%s"%player_1)

    while True:
        
        row=int(input("row:"))
        col=int(input("col:"))

        if 0<=row<=2 and 0<=col<=2:
            if game_board[row][col]=="-":
                game_board[row][col]="X"
                break
            else:
                print("It's full,enter another number")
        else:
            print("between 0 and 2")

    show()

    print("computer has played and the board game is like this now:")
    while True:
        row=random.randint(0,2)
        col=random.randint(0,2)
        if game_board[row][col]=="-":
            game_board[row][col]="O"
            break
    show()
