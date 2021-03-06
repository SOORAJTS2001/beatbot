import cv2 as cv
from cv2 import VideoCapture
import mediapipe as mp
import time
cap = VideoCapture(0)#records video from the camera
ptime =0
mpDraw = mp.solutions.drawing_utils#to draw the condours
mPose= mp.solutions.pose
pose = mPose.Pose()#it gets the pose postions

while True:
    success,img = cap.read()
    imRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)#it converts to rgb for processing
    result = pose.process(imRGB)
    #print(result.pose_landmarks)#it is to get the landmarks of the individual points in the ratio to the whole body 
    if(result.pose_landmarks):
        mpDraw.draw_landmarks(img,result.pose_landmarks,mPose.POSE_CONNECTIONS)
        for id,lm in enumerate(result.pose_landmarks.landmark):
            h, w, c = img.shape#height width for the image
            cx, cy = int(lm.x * w), int(lm.y * h)
            print("id :",id,"cx:",cx,"cy:",cy)#roi points
    ctime = time.time()
    fps = 1/(ctime-ptime)#it is to find the fps
    ptime = ctime
    cv.putText(img,str(int(fps)),(70,40),cv.FONT_HERSHEY_COMPLEX,1,(255,255,0),1)
    cv.imshow("Positions",img)#to see the image
    cv.waitKey(1)



