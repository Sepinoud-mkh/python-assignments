import numpy as np
import cv2


board = np.ones((480, 480))*255

board[100:160, 300:360] = 0

board[40:100, 200:300] = 0
board[200:260, 200:300] = 0
board[340:400, 200:300] = 0

board[100:200, 140:200] = 0
board[260:340, 300:360] = 0

board[280:340, 140:200] = 0



cv2.imshow("", board)
cv2.imwrite("name.jpg", board)
cv2.waitKey()