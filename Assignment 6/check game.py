game_board = [["X", "X", "X"],
              ["O", "-", "O"],
              ["-", "O", "-"]]

for i in range(3):
    if game_board[i][0]==game_board[i][1]==game_board[i][2]=="X" or game_board[0][i]==game_board[1][i]==game_board[2][i]=="X" or game_board[0][0]==game_board[1][1]==game_board[2][2]=="X" or game_board[0][2]==game_board[1][1]==game_board[2][0]=="X":
        print("player 1 Wins")
    elif game_board[i][0]==game_board[i][1]==game_board[i][2]=="O" or game_board[0][i]==game_board[1][i]==game_board[2][i]=="O" or game_board[0][0]==game_board[1][1]==game_board[2][2]=="O" or game_board[0][2]==game_board[1][1]==game_board[2][0]=="O":
        print("player 2 Wins")