import cv2

image_1 = cv2.imread("1.jpg")
width_1 = image_1.shape[0]
height_1 = image_1.shape[1]
print(width_1, height_1)

image_2 = cv2.imread("2.jpg")
width_2 = image_2.shape[0]
height_2 = image_2.shape[1]
print(width_2, height_2)

for i in range(width_1):
    for j in range(height_1):
        image_1[i][j] = 255- image_1[i][j]


for i in range(width_2):
    for j in range(height_2):
        image_2[i][j] = 255- image_2[i][j]


cv2.imshow("new 1", image_1)
cv2.imwrite("NEW 1.jpg", image_1)

cv2.imshow("new 2", image_2)
cv2.imwrite("NEW 2.jpg", image_2)
cv2.waitKey()