import numpy as np
import cv2


board = np.ones((480, 480)) * 255


#for i in range(0, 480):
#    for j in range(0, 100):
#        board[i][j] = 255
#    for j in range(380, 480):
#        board[i][j] = 255

#for i in range(0, 50):
#    for j in range(100, 380):
#        board[i][j] = 255

#for i in range(360, 480):
#    for j in range(120, 360):
#        board[i][j] = 255

#for j in range(100, 380):
#    for i in range(0, 50):
#        board[i][j] = 255
#    for i in range(430, 480):
#        board[i][j] = 255

for j in range(180, 300):
    for i in range(100, 160):
        board[i][j] = 0
for j in range(1kk)
cv2.imshow("", board)
cv2.imwrite("name.jpg", board)
cv2.waitKey()