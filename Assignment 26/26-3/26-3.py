import numpy as np
import cv2


image = cv2.imread("3.jpg")
newImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

width, height = newImage.shape



for i in range((width//2)+1):
    for j in range(1, height):
            
            color_Code = newImage[i][j]
            newImage[i][j] = newImage[width-i-1, height-j-1]
            newImage[width-i-1, height-j-1] = color_Code
            if (i==width//2 and j==height//2):
                  break


cv2.imshow("", newImage)
cv2.imwrite("NEW 3.jpg", newImage)
cv2.waitKey()

