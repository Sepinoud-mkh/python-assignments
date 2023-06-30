import numpy as np
import cv2

R = 8 #int(input("enter the number of the rows:"))
C = 8 #int(input("enter the number of the columns:"))

row = R*60
column = C*60

Board = np.zeros((row, column))

#سطر فرد

for i in range(1, R+1):
    for a in range(60*2*i, 60*(2*i+1)):
        for k in range(60*2*i, 60*(2*i+1)):
            Board[a][k] = 255
#for k in range(120,180):
#    Board[a][k] = 255
#for k in range(240,300):
#    Board[a][k] = 255
#for k in range(360,420):
#    Board[a][k] = 255
    #سطر زوج
#for a in range(60):
#    for k in range(60, 120):
#        Board[a][k] = 255
#    for k in range(180, 240):
#        Board[a][k] = 255
#    for k in range(300, 360):
#        Board[a][k] = 255
#    for k in range(420, 480):
#        Board[a][k] = 255

#for a in range(120, 180):
#    for k in range(60):
#        Board[a][k] = 255
#    for k in range(120,180):
#        Board[a][k] = 255
#    for k in range(240,300):
#        Board[a][k] = 255
#    for k in range(360,420):
#        Board[a][k] = 255
#


cv2.imshow("",Board)
cv2.imwrite("Chess Board.jpg", Board)

#input = cv2.imread("Chess Board.jpg", cv2.IMREAD_UNCHANGED)
#output = cv2.resize(input,[500, 500])
#cv2.imshow("",output)



cv2.waitKey()