import cv2
import numpy as np
import os

scaleFactor=8
myImage=cv2.imread("F:\important photos\MobileSmart\mobile memori\ImageCollage\me.jpg")

width,height=myImage.shape[:2]
w=int(width/scaleFactor)
h=int(height/scaleFactor)


for x in range(w):
	for y in range(h):
		color=myImage[x,y]
		print(color)
		cv2.rectangle(myImage
			,(x*scaleFactor,y)
			,(x,y*scaleFactor+scaleFactor)
			,(int(color[0]),int(color[1]),int(color[2])),0) 
cv2.imshow("myImage",myImage)
cv2.waitKey()


'''
import os


def create_collages(image_dir):
    image_paths = os.listdir
    n = len(image_paths)
    # find nearest square
    collage_size = int(math.floor(math.sqrt(len(good_paths))))

    # horizontally stacking images to create rows
    rows = []
    k = 0 # counter for number of rows
    for i in range(collage_size**2):
        if i % collage_size == 0: # finished with row, start new one
            if k > 0:
                rows.append(cur_row)

            cur_row = cv2.imread(os.path.join(image_dir, image_paths[i]))
            k += 1
        else:             # continue stacking images to current row
            cur_img = cv2.imread(os.path.join(image_dir, image_paths[i]))
            cur_row = np.hstack([cur_row, cur_img])

        # vertically stacking rows to create final collage.
        collage = rows[0]

        for i in range(1, len(rows)):
            collage = np.vstack([collage, rows[i]])

    return collage
    '''


