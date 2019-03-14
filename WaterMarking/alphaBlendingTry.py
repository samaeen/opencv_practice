import cv2
import numpy as np

# Read the images
foreground = cv2.imread("einstein.jpg")
background = cv2.imread("fruits.jpg")

img2gray = cv2.cvtColor(background,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(background, 100, 255, cv2.THRESH_BINARY_INV)
cv2.imwrite('new.jpg',mask)
alpha = cv2.imread("new.jpg")
 
# Convert uint8 to float
foreground = foreground.astype(float)
background = background.astype(float)
 
# Normalize the alpha mask to keep intensity between 0 and 1
alpha = alpha.astype(float)/255
 
# Multiply the foreground with the alpha matte
foreground = cv2.multiply(alpha, foreground)
 
# Multiply the background with ( 1 - alpha )
background = cv2.multiply(1.0 - alpha, background)
 
# Add the masked foreground and background.
outImage = cv2.add(foreground, background)
 
# Display image
cv2.imshow("outImg", outImage/255)
cv2.waitKey(0)