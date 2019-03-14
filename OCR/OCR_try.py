import pytesseract
import cv2
import numpy as np
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
img=cv2.imread('new.png')
#img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#kernel=np.ones((1,1),np.uint8)
#img=cv2.dilate(img,kernel,iterations=1)
#img=cv2.erode(img,kernel,iterations=1)
#cv2.imwrite("new.png",img)
#img=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
#cv2.imwrite("neww.png",img)
#c=Image.open("neww.png")
print(pytesseract.image_to_string(Image.open('neww.png'),lang='eng'))