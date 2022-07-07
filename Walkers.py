import cv2
import numpy as np

vid = cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier('frontalface.xml')
while(True):
   
   
    ret, frame = vid.read()
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(grey,1.1,5)
    print(faces)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)

   
    cv2.imshow("Web cam", frame)
 
    if cv2.waitKey(25) == 32:
        break
  

vid.release()
