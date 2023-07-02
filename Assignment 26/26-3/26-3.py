import numpy as np
import cv2


image = cv2.imread("3.jpg")


print(image.shape)

width = int(image.shape[0])
height = int(image.shape[1])
depth = image.shape[2]



for i in range(1, width):
    for j in range(1, height):
        for k in range(1, depth):
            color_Code = image[i][j][k]
            #print(i, j, k, color_Code, width-i, height-j, depth-k)
            new_Width = width-i
            new_Height = height-j
            new_Depth = depth-k

            image[new_Width][new_Height][new_Depth]
            #print(image[new_Width][new_Height][new_Depth])


cv2.imshow("", image)
cv2.imwrite("NEW 3.jpg", image)

cv2.waitKey()








#cv2.imshow("", image)

#cv2.waitKey()