import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
	ret,image=cap.read()
	edges=cv2.Canny(image,100,100)
	#cv2.imshow('edgy',edges)
	(cnts, _) = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(image, [], -1, (0,255,0), 3)
	if cv2.waitKey(30)& 0xff==ord('q'):
		break

cap.release()
cv2.destroyAllWindows()