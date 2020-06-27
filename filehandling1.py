# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 21:48:49 2020

@author: DHRUV
"""


file = open("testfile.txt","r")
print(file)
#print("only first 3 bytes are read now: ",file.read(3))
#file.write("I am adding this to the text file!")
print(file.readlines())
file.close();