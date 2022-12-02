import cv2 

capture = cv2.VideoCapture(0)

while True:
    bool_return, frame = capture.read()
    cv2.imshow('frame_window',frame)

    key = cv2.waitKey(0)
    if key == 27:
        break
    else:
        continue

