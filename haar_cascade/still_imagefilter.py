# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 20:10:20 2020

@author: DHRUV
"""


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
#nose_cascade = cv2.CascadeClassifier("Nose18x15.xml")

skip = 0 
face_data = []
face_section=0  
moustache = cv2.imread('moustache.png')
        
img = cv2.imread('Before.png')
X_s = []
Y_s = []

eyes = eye_cascade.detectMultiScale(img,1.3,5)
#nose = nose_cascade.detectMultiScale(img,1.5,5)

for i in eyes[:,:]:
    x,y,w,h = i;
    x_c=(2*x+w)//2
    y_c=(2*y+h)//2
    cv2.circle(img,(x_c,y_c),5,(255,0,0),4)
    X_s.append(x_c)
    Y_s.append(y_c)
        
x,y,w,h = eyes[0] 
x2,y2,w2,h2 = eyes[1]
cv2.imshow('Read',img)
#cv2.imshow('M',moustach

overlay=cv2.imread("glasses.png",cv2.IMREAD_UNCHANGED)
overlay=cv2.cvtColor(overlay,cv2.COLOR_BGRA2RGBA)

overlay=cv2.resize(overlay,(x,y))

for i in range(overlay.shape[0]):
    for j in range(overlay.shape[1]):
        if(overlay[i,j,3]>0):
            img[y2+i-25,x2+j-15,:]=overlay[i,j,:-1]
            
# x,y,w,h = nose[0]
# moustache=cv2.resize(moustache,(w,h))

# for i in range(moustache.shape[0]):
#     for j in range(moustache.shape[1]):
#         if(moustache[i,j,3]>0):
#             img[y+i,x+j,:]=moustache[i,j,:-1]

cv2.imshow('output',img)




cv2.waitKey(0)

