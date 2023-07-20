import numpy as np
import cv2

board_size = 480
board = np.zeros((board_size, board_size))

squares_per_side = 9
square_size = board_size // squares_per_side

for row in range(squares_per_side):
    for col in range(squares_per_side):
        if (row + col) % 2 == 0:
            board[row * square_size: (row + 1) * square_size, col * square_size: (col + 1) * square_size] = 255

cv2.imshow("", board)
cv2.imwrite("26-1\Chess Board.jpg", board)

cv2.waitKey()