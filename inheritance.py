# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 20:08:07 2020

@author: DHRUV
"""

class Transport:
    def __init__(self,segment,name,cap):
        self.segment=segment;
        self.name=name;
        self.cap=cap;
        
    def cap_sqr(self):
        print(self.cap**2)
        
class Car(Transport):
    def __init__(self,segment,name,cap,color,model):
        super().__init__(segment,name,cap)
        self.color=color
        self.model=model
    
    def print_capsqr(self):
        self.cap_sqr()
        
b=Car("car","honda",4,"red","civic")
b.print_capsqr()
print(b.segment)