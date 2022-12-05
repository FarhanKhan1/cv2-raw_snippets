import cv2
cap = cv2.VideoCapture(0)
cap.set(3, 3100)
cap.set(4, 3100)

print(cap.get(3))
print(cap.get(4))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

       cv2.imshow('frame', frame)
       key = cv2.waitKey(0)
       if key == ord('e'):
         break
    else:
        break

cap.release()
cv2.destroyAllWindows()