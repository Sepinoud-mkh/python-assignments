import numpy as np
import cv2


Board = np.zeros((480, 480))


#1
for a in range(0, 60):
    for k in range(60):
        Board[a][k] = 255
    for k in range(120,180):
        Board[a][k] = 255
    for k in range(240,300):
        Board[a][k] = 255
    for k in range(360,420):
        Board[a][k] = 255
#2
for a in range(60, 120):
    for k in range(60, 120):
        Board[a][k] = 255
    for k in range(180, 240):
        Board[a][k] = 255
    for k in range(300, 360):
        Board[a][k] = 255
    for k in range(420, 480):
        Board[a][k] = 255       
#3
for a in range(120, 180):
    for k in range(60):
        Board[a][k] = 255
    for k in range(120,180):
        Board[a][k] = 255
    for k in range(240,300):
        Board[a][k] = 255
    for k in range(360,420):
        Board[a][k] = 255
#4
for a in range(180, 240):
    for k in range(60, 120):
        Board[a][k] = 255
    for k in range(180, 240):
        Board[a][k] = 255
    for k in range(300, 360):
        Board[a][k] = 255
    for k in range(420, 480):
        Board[a][k] = 255 
#5
for a in range(240, 300):
    for k in range(60):
        Board[a][k] = 255
    for k in range(120,180):
        Board[a][k] = 255
    for k in range(240,300):
        Board[a][k] = 255
    for k in range(360,420):
        Board[a][k] = 255

#6
for a in range(300, 360):
    for k in range(60, 120):
        Board[a][k] = 255
    for k in range(180, 240):
        Board[a][k] = 255
    for k in range(300, 360):
        Board[a][k] = 255
    for k in range(420, 480):
        Board[a][k] = 255 
#7
for a in range(360, 420):
    for k in range(60):
        Board[a][k] = 255
    for k in range(120,180):
        Board[a][k] = 255
    for k in range(240,300):
        Board[a][k] = 255
    for k in range(360,420):
        Board[a][k] = 255      
#8
for a in range(420, 480):
    for k in range(60, 120):
        Board[a][k] = 255
    for k in range(180, 240):
        Board[a][k] = 255
    for k in range(300, 360):
        Board[a][k] = 255
    for k in range(420, 480):
        Board[a][k] = 255 




cv2.imshow("",Board)
cv2.imwrite("26-1\Chess Board.jpg", Board)

cv2.waitKey()