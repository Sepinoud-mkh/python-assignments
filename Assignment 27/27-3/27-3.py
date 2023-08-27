import cv2
import numpy as np
import random

image = cv2.imread("lonely-japanese-cherry.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.resize(image, (600, 400))

rows, cols = image.shape

#writer = cv2.VideoWriter('snow.mp4', cv2.VideoWriter_fourcc(*'mpv4'), 10, (cols, rows))





while True:

    r = 0
    row = random.randint(0, 400)
    col = random.randint(0, 600)
   

    while r != row:

        temp = image[r, col]
        temp =  int(temp)
        cv2.circle(image, (col, r), 1, 0, 2)
        cv2.circle(image, (col, r + 10), 1, 100, 2)

        cv2.waitKey(15)
        cv2.circle(image, (col, r), 1, temp, 2)
        if r <= 390:
            r = r + 10
        else:
            row = random.randint(0, 400)
            print("hi")


        cv2.imshow("result", image)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break


#writer.release()