import cv2
import numpy as np

MIN_MATCH_COUNT=10

#initialize SIFT/SURF matcher
detector = cv2.xfeatures2d.SIFT_create()
FLANN_INDEX_KDTREE = 0
flannParams = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
searchParams = dict(checks=50)   # or pass empty dictionary

#initialize flann based matcher..it has two parameters 
#flannParams is important searchParam can be an empty dictionary
flann = cv2.FlannBasedMatcher(flannParams,searchParams)


trainImg=cv2.imread('TrainData/TI.jpg',0)
trainKP,trainDecs=detector.detectAndCompute(trainImg,None)

cam=cv2.VideoCapture(0)

while True:
	ret,QueryImgColored=cam.read()
	QueryImg=cv2.cvtColor(QueryImgColored,cv2.COLOR_BGR2GRAY)
	queryKP,queryDesc=detector.detectAndCompute(QueryImg,None)
	matches=flann.knnMatch(queryDesc,trainDecs,k=2)

	goodMatch=[]
	for m,n in matches:
		if(m.distance<0.75*n.distance):
			goodMatch.append(m)

	if(len(goodMatch)>MIN_MATCH_COUNT):
		tp=[]
		qp=[]
		for m in goodMatch:
			tp.append(trainKP[m.trainIdx].pt)
			qp.append(queryKP[m.queryIdx].pt)
		tp,qp=np.float32((tp,qp))
		H,status=cv2.findHomography(tp,qp,cv2.RANSAC,3.0)
		h,w=trainImg.shape
		trainBorder=np.float32([[[0,0],[0,h-1],[w-1,h-1],[w-1,0]]])
		queryBorder=cv2.perspectiveTransform(trainBorder,H)
		cv2.polylines(QueryImgColored,[np.int32(queryBorder)],True,(255,255,0),5)

	else:
		print("No Match")
	cv2.imshow('Final',QueryImgColored)

	if cv2.waitKey(30)& 0xff==ord('q'):
		break

cam.release()
cv2.destroyAllWindows()

print("working so far")
