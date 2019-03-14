import numpy as np
import cv2

cap=cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    canny = cv2.Canny(gray,80,240,3)
    fgmask = fgbg.apply(frame)

    cv2.imshow('frame',fgmask)
    if cv2.waitKey(30)& 0xff==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
