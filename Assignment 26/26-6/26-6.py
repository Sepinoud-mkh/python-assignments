import cv2

img = cv2.imread("download.jpg")

black = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print(black.shape)

for i in range(25, 55):
    for j in range(0, 60):
        black[i-j][j] = 0


cv2.imshow("", black)
cv2.imwrite("RIP.jpg", black)
cv2.waitKey()