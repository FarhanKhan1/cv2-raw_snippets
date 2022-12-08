import cv2 as cv
import numpy as np

my_img = cv.imread('sudoku.png',0)
_, tresh_hold1 = cv.threshold(my_img, 127, 255, cv.THRESH_BINARY)
tresh_hold2 = cv.adaptiveThreshold(my_img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2);
tresh_hold3 = cv.adaptiveThreshold(my_img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2);

cv.imshow("Image", my_img)
cv.imshow("THRESH_BINARY", tresh_hold1)
cv.imshow("ADAPTIVE_THRESH_MEAN_C", tresh_hold2)
cv.imshow("ADAPTIVE_THRESH_GAUSSIAN_C", tresh_hold3)

cv.waitKey(0)
cv.destroyAllWindows()