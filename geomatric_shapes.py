import numpy as np
import cv2

#my_image = cv2.imread('lena.jpg', 1)
my_image = np.zeros([512, 512, 3], np.uint8)

my_image = cv2.line(my_image, (255,255), (255,255), (255, 255, 0), 10) # 44, 96, 147
my_image = cv2.arrowedLine(my_image, (255,0), (255,255), (255, 0, 0), 10)
my_image = cv2.arrowedLine(my_image, (255,0), (0,255), (200, 200, 200), 10)
my_image = cv2.circle(my_image, (447, 63), 63, (0, 255, 0), -1)
my_font = cv2.FONT_HERSHEY_PLAIN
my_image = cv2.putText(my_image, 'My text', (10, 500), my_font, 4, (200, 255, 255), 10)
 
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
my_image = cv2.polylines(my_image,[pts],True,(255,255,255))
cv2.imshow('my_image_window', my_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
