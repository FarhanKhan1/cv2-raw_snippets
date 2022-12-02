import cv2

my_img  =cv2.imread("lena.jpg", -1)

cv2.imshow("MyImg",my_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("copy_of_lena.jpg", my_img)
