# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 16:21:04 2020

@author: DHRUV
"""

n=int(input("enter no. of students: "))
students=[]
for i in range(0,n):
    rno=int(input("roll no: "))
    name=input("name: ")
    students.append({"rno":rno,"name":name})
    
    