# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 16:55:38 2020

@author: DHRUV
"""

class Car:
    def __init__(self,name,cost):
        self.name=name;
        self.cost=cost;
        
    def __add__(self,other):
        return self.cost+other.cost
    
    def __eq__(self,other):
        if self.cost==other.cost:
            return True
        else:
            return False
        
a=Car("Honda",1200)
b=Car("Hyundai",1400)
c=Car("Tata",1200)

print (a==b)
print (a==c)

#Making cout with python

class Output:
        
    def __lshift__(self,other):
        print (other)
        return self
    
cout = Output()