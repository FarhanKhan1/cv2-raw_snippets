import cv2
import numpy as np

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1,(200, 0), (300, 100), (255, 255, 255), -1)
img3 = np.ones((250,500,3), np.uint8)

bit_And = cv2.bitwise_and(img3, img1)
bit_Or = cv2.bitwise_or(img3, img1)


cv2.imshow("img1", img1)

cv2.imshow("img3", img3)
cv2.imshow('bitAnd', bit_And)
cv2.imshow('bitOr', bit_Or)

cv2.waitKey(0)
cv2.destroyAllWindows()