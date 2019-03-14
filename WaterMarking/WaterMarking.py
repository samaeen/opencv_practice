import numpy as np
import cv2
from matplotlib import pyplot as plt

hostImage=cv2.imread('einstein.jpg')
hostImage=cv2.resize(hostImage,None,fx=.5, fy=.5, interpolation = cv2.INTER_CUBIC)
watermark=cv2.imread('fruits.jpg')
watermark=cv2.resize(watermark,None,fx=.075, fy=.119, interpolation = cv2.INTER_CUBIC)
cv2.imwrite('watermark1.jpg',watermark)

add=cv2.add(hostImage+watermark)
cv2.imshow('add',add)
cv2.waitKey(0)
cv2.imshow('hostImage',hostImage)

watermark = cv2.imread('watermark1.jpg', cv2.IMREAD_UNCHANGED)
(wH, wW) = watermark.shape[:2]

(B, G, R) = cv2.split(watermark)
B = cv2.bitwise_and(B, B)
G = cv2.bitwise_and(G, G)
R = cv2.bitwise_and(R, R)
watermark = cv2.merge([B, G, R])

#add alpha transperency
image = hostImage
(h, w) = image.shape[:2]
image = np.dstack([image, np.ones((h, w), dtype="uint8") * 255])
# construct an overlay that is the same size as the input
# image, (using an extra dimension for the alpha transparency),
# then add the watermark to the overlay in the bottom-right
# corner
overlay = np.zeros((h, w, 4), dtype="uint8")
overlay[h-10:h,w-10:w] = watermark
# blend the two images together using transparent overlays
output = image.copy()
cv2.addWeighted(overlay,1, output, 1.0, 0, output)
														 
# write the output image to disk
#filename = imagePath[imagePath.rfind(os.path.sep) + 1:]
#p = os.path.sep.join(("output", filename))
cv2.imwrite('p.jpg', output)
cv2.imshow('watermark',watermark)
cv2.waitKey(0)