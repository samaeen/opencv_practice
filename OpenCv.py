import cv2
import numpy as np

img=cv2.imread('Me.jpg',cv2.IMREAD_COLOR)
kaloizValo=cv2.imread('Me.jpg',cv2.IMREAD_GRAYSCALE)

cv2.imshow('fodu',img)
cv2.imshow('Balamar',kaloizValo)

cv2.waitKey()
print('hello')
