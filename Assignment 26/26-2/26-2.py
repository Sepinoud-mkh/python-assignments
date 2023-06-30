import cv2


image_1 = cv2.imread("1.jpg")
print(image_1.shape)
image_2 = cv2.imread("2.jpg")
print(image_2.shape)

for i in range(645):
    for j in range(645):
        image_1[i][j] = 255- image_1[i][j]


for i in range(1202):
    for j in range(900):
        image_2[i][j] = 255- image_2[i][j]


cv2.imshow("new 1", image_1)
cv2.imwrite("NEW 1.jpg", image_1)

cv2.imshow("new 2", image_2)
cv2.imwrite("NEW 2.jpg", image_2)
cv2.waitKey()