import numpy as np
import cv2

Board = np.zeros((255, 255))


for i in range(0, 255):
    Board[i, :] = int(255-i)




cv2.imshow("", Board)
cv2.imwrite("gradient.jpg", Board)

cv2.waitKey()