
import cv2

my_img = cv2.imread('gradient.png',0)
_, th1 = cv2.threshold(my_img, 50, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(my_img, 200, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(my_img, 127, 255, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(my_img, 127, 255, cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(my_img, 127, 255, cv2.THRESH_TOZERO_INV)


cv2.imshow("main_image", my_img)
cv2.imshow("thwindow1", th1)
cv2.imshow("thwindow2", th2)
cv2.imshow("thwindow3", th3)
cv2.imshow("thwindow4", th4)
cv2.imshow("thwindow5", th5)

cv2.waitKey(0)
cv2.destroyAllWindows()