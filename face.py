#FACE RECOGNITION

import cv2
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#in the above line we import the haarcascade model

img=cv2.imread('abc.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,1.1,9)

#1.1 -scalefactor
#9-minineighboures
for x,y,w,h in faces:
    img =cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,225),5)

cv2.imshow('FACE RECOGNTION',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
