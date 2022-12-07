import numpy as np
import cv2

my_image = cv2.imread("lena.jpg")
my_img1 = cv2.imread("cards.png")
print(my_image.shape)
print(my_image.size)
print(my_img1.shape)
my_image =  cv2.resize(my_image, (256,256))
my_img1 =  cv2.resize(my_img1, (256,256))

print(my_image.shape)
print(my_image.size)
print(my_img1.shape)
new_img = cv2.addWeighted(my_image, .8,my_img1, .2, 0)
cv2.imshow("image",new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
#there are number of arithmetic operations in it

