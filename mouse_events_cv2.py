import numpy as np
import cv2
m_events = []
for i in dir(cv2):
    if 'MOUSE' in i or 'EVENT' in i:
        m_events.append(i)
print(m_events)

def click_event(event, x, y, flags, param):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        print("You have a left mouse click")
    if event == cv2.EVENT_RBUTTONDOWN:
        print("You have a right mouse button click")
 
img = cv2.imread('lena.jpg')
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)
 
cv2.waitKey(0)
cv2.destroyAllWindows()