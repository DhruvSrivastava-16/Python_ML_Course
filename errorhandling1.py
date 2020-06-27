# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 18:14:18 2020

@author: DHRUV
"""


for i in range(0,3):
    try:
        print (8/i)
    except:
        print("error!")
    finally:
        print("phew, done!\n")
        
for i in range(0,3):
    try:
        print (8/i)
    except Exception as e:
        print("e: ",e)