import cv2
import numpy as np
import random

image = cv2.imread("lonely-japanese-cherry.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.resize(image, (600, 400))

print(image.shape)
# for row in range(0, 600, 50):
#     for col in range(0, 400, 20):
#         cv2.circle(image, (row, col), 1, 200, 2)

# cv2.imshow("result", image)
# cv2.waitKey()

while True:


    col = 0
    while col != 600:

        row = random.randint(0, 400)
        cv2.circle(image, (col, row), 1, 0, 2)
        col = col + 10

    cv2.imshow("result", image)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break


