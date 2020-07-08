# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 18:07:18 2020

@author: DHRUV
"""
import numpy as np 
import pandas as pd
import cv2
import matplotlib.pyplot as plt

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
skip = 0 
face_data = []
face_section=0  

#initiate the camera 
cap = cv2.VideoCapture(0)


while True:   
    ret,frame = cap.read()
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame,1.3,5)
    eyes = eye_cascade.detectMultiScale(gray_frame,1.3,5)
    
    if ret==False:
        continue
    
      #  cv2.imshow('Gray Frame',gray_frame)
    faces = sorted(faces, key = lambda f: f[2]*f[3]) #to sort in terms of face size
    print(faces)
    eyes = sorted(eyes, key = lambda f: f[2]*f[3]) #to sort in terms of face size
    print(eyes)

        
    for face in faces[-1:]: #picking the last face since its largest in terms of size (area) -- w and h ~ f2 and f3
        x,y,w,h = face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
     #  cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

      # Extract region of interest and store it:
        offset = 10
        face_section = frame[y-offset:y+h+offset,x-offset:x+w+offset]
        face_section = cv2.resize(face_section,(100,100))
        
        skip+=1
        if(skip%10): #store every 10th face
            face_data.append(face_section)
            print(len(face_data))
    
    for eye in eyes[-1:]: #picking the last face since its largest in terms of size (area) -- w and h ~ f2 and f3
        x,y,w,h = eye
        x = (x+x+w)/2
        y= (y+y+h)/2
        cv2.circle(frame,(int(x),int(y)),2,(255,255,0),6)
        cv2.circle(frame,(int(x),int(y)),2,(255,255,0),6)

       # cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),3)

      #  cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)

      # Extract region of interest and store it:

 
    
    cv2.imshow('a',frame)
    
    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()