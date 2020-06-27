# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 17:02:10 2020

@author: DHRUV
"""

file = open("testfile.txt","r")
print(file.read())
print("\n Now we'll skip the first 10bytes: ")
file.seek(10)
print(file.read())
file.close()

print("\n Going to the with block")

with open("testfile.txt","a+") as file:
    file.write("I am adding this to the end of the file")
    print(file.read())
    
    
