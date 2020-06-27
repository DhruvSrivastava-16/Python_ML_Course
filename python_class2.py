# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 17:12:45 2020

@author: DHRUV
"""

class Dogs:
    tricks=[]
    
    def __init__(self,name):
        self.name=name;
        
    def addtricks(self,trick):
        self.tricks.append(trick)

class Cats:
    
    def __init__(self,name):
        self.name=name;
        self.tricks=[]
        
    def addtricks(self,trick):
        self.tricks.append(trick) 
        
dexter = Dogs("Dexter")
rambo = Dogs("Rambo")
dexter.addtricks("talk")
dexter.addtricks("dance")

print("Dexter knows how to: ",dexter.tricks)
print("But Rambo knows how to: ",rambo.tricks)
#from the above outputs you can see that it automatically gave Dexter's tricks to Rambo, so to tackle this declare tricks in the way done for Cats!

Bell = Cats("Bell")
Snowball = Cats("Snowball")
Bell.addtricks("talk")
Bell.addtricks("dance")

print("Bell knows how to: ",Bell.tricks)
print("Snowball Rambo knows how to: ",Snowball.tricks)
#Bell knows both and snowball doesnt know anything!