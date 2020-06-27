# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 17:31:42 2020

@author: DHRUV
"""


import matplotlib.pyplot as plt
import numpy as np
import cv2

y=np.array([1,2,3,4,5])
x=y**2
plt.plot(x,y)
plt.show()

img=cv2.imread('dhruv.jpeg')
rgb_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(rgb_img)
plt.axis('off') 
print(img.shape)
plt.imshow(img[0:950,200:950,:])