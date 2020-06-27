# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 23:16:08 2020

@author: DHRUV
"""

def show(*args):
    print(args)
    
def show2(a,b,c,*args,d,e):
    print("a: ",a,"b: ",b,"c: ",c)
    print("args: ",args)
    print("d: ",d)
    
def show3(a,b,c,*args,d,**kwargs):
    print("a: ",a,"b: ",b,"c: ",c)
    print("args: ",args)
    print("d: ",d)
    print("kwargs: ",kwargs)
    
    
show("hello",1,2,3,4)
show(1,9,11,"byee")
show(0)
print("----------------")
show2(3,4,5,6,7,8,"helloo",d=12,e=9)
show2(1,2,9,"hellotwo",11,"byee",d="niceD",e=4)
print("----------------")
show3(2,5,6,"hi",d="byeee",e=9923,f=12,z="dhruv")


