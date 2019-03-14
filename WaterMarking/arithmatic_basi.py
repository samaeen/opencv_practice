import cv2
import numpy as np

# Load two images
hostImage=cv2.imread('einstein.jpg')
hostImage=cv2.resize(hostImage,None,fx=.5, fy=.5, interpolation = cv2.INTER_CUBIC)
img1 = hostImage
img2 = cv2.imread('mainlogo.png')

#watermark=cv2.imread('fruits.jpg')
#watermark=cv2.resize(watermark,None,fx=.075, fy=.119, interpolation = cv2.INTER_CUBIC)
#cv2.imwrite('watermark1.jpg',watermark)
#img2 = cv2.imread('watermark.jpg')

# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows,0:cols]

# Now create a mask of logo and create its inverse mask
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# add a threshold
ret, mask = cv2.threshold(img2gray, 100, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

cv2.imshow('res',img1)
cv2.waitKey(0)
#cv2.destroyAllWindows()