import cv2

image = cv2.imread("bat.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

max = max(image.shape)

_, new_Image= cv2.threshold(image, 139, 255, cv2.THRESH_BINARY_INV)

cv2.putText(new_Image, "BATMAN", (350, 530), cv2.FONT_HERSHEY_DUPLEX, 3, (255, 255, 255))


cv2.imshow("result", new_Image)
cv2.waitKey()
cv2.imwrite("batman.jpg", new_Image)