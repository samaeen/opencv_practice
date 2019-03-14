import numpy as np
import cv2
 
template = cv2.imread('GB.jpg')
 
cap=cv2.VideoCapture(0)
# resize images

template = cv2.resize(template, (0,0), fx=0.5, fy=0.5) 
 
# Convert to grayscale
while True:
	ret,image=cap.read()
	image = cv2.resize(image, (0,0), fx=0.5, fy=0.5) 
	imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
 
	# Find template
	result = cv2.matchTemplate(imageGray,templateGray, cv2.TM_CCOEFF)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)		
	top_left = max_loc
	h,w = templateGray.shape
	bottom_right = (top_left[0] + w, top_left[1] + h)
	cv2.rectangle(image,top_left, bottom_right,(25,25,255),4)
 
	# Show result
	cv2.imshow("Template", template)
	cv2.imshow("Result", image)
 
 
	if cv2.waitKey(30)& 0xff==ord('q'):
		break

cap.release()
cv2.destroyAllWindows()