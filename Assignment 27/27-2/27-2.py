import cv2
import numpy as np

tv = cv2.imread("old_Tv.jpg")
tv = cv2.cvtColor(tv, cv2.COLOR_BGR2GRAY)
rows, cols = tv.shape

writer = cv2.VideoWriter('noise.mp4', cv2.VideoWriter_fourcc(*'mpv4'), 10, (cols, rows))

while True:
    image = np.random.random((195, 252)) * 255
    image = np.array(image, dtype = np.uint8)
    tv[55:250, 88:340] = image

    writer.write(tv)
    cv2.imshow("result", tv)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

writer.release()