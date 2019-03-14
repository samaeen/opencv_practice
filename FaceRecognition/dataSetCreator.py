import cv2
import numpy as np
import sqlite3

def insertOrUpdate(ID,Name):
    conn=sqlite3.connect("faceBase.db")
    cmd="SELECT * FROM People WHERE ID="+str(ID)
    cursor=conn.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd="UPDATE People SET Name="+str(Name)+"WHERE ID="+str(ID)
    else:
        cmd="INSERT INTO People(ID,Name) Values(?,?)",("+str(ID)+","+str(Name)+")
    conn.execute(cmd)
    conn.commit()
    conn.close()


#initialize sample number and get user input
id=input('enter User Id: ')
name=input('enter your name: ')
insertOrUpdate(id,name)
#load cascade
faceDetect=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cam=cv2.VideoCapture(0);
sampleNum=0;
while(True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    #detect face and draw rects
    for(x,y,w,h) in faces:
        sampleNum=sampleNum+1;
        #write image names to dataset folder yo!
        cv2.imwrite("dataSet/User."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.waitKey(100)
    cv2.imshow("Face",img)
    if(sampleNum>20):
        break;
cam.release()
cv2.destroyAllWindows()
