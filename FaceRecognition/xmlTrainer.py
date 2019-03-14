import os
import cv2
import numpy as np
from PIL import Image

#initialize face recognizer
recognizer=cv2.face.createLBPHFaceRecognizer();
path='dataSet'

def getImagesWithID(path):
    #get image path
    imagePaths=[os.path.join(path,f)for f in os.listdir(path)]
    faces=[]
    IDs=[]
    for imagePath in imagePaths:
        #open image paths in faceImg and convert it into imagePath numpy array
        faceImg=Image.open(imagePath).convert('L');
        faceNp=np.array(faceImg,'uint8')
        ID=int(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(faceNp)
        print (ID)
        IDs.append(ID)
        cv2.imshow("training",faceNp)
        cv2.waitKey(10)
    return np.array(IDs),faces

Ids,faces=getImagesWithID(path)
recognizer.train(faces,Ids)
recognizer.save('recognizer/trainingData.yml')
cv2.destroyAllWindows()
