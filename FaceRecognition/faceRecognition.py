import cv2
import numpy as np
import sqlite3

def getProfile(id):
    conn=sqlite3.connect("faceBase.db")
    cmd="SELECT *FROM People WHERE ID="+str(id)
    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile
#load haarcascade
faceDetect=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cam=cv2.VideoCapture(0);
#load recognizer
recognizer=cv2.face.createLBPHFaceRecognizer()
recognizer.load("recognizer\\trainingData.yml")
id=0
#load font
font=cv2.FONT_HERSHEY_SIMPLEX

while(True):
    ret,img=cam.read();
    #convert to grayscale Image
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #detect faces 
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        #draw rects in faces
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        #recognition yo!!
        id,conf=recognizer.predict(gray[y:y+h,x:x+w])
        profile=getProfile(id)
        if(profile!=None):
            cv2.putText(img,profile[1],(x,y+h+50),font,1,(255,255,200),2,cv2.LINE_AA);       
    cv2.imshow("Face",img);
    if(cv2.waitKey(1)==ord('q')):
        break;
cam.release()
cv2.destroyAllWindows()
