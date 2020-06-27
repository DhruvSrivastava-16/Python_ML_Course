# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 02:33:21 2020

@author: DHRUV
"""

users={'dhruv':'123@om','surabhi':'34@shivji'}
def show(username,password):
    if username in users and users[username]==password:
        print("authenticated!")
    else:
        print("you are not allowed!")
        
def login_required(func):
    def wrapper(username,password,*args,**kwargs):
        
        if username in users and users[username]==password:
            func(*args,**kwargs)
        
        else: 
            print("not authenticated!")
    
    return wrapper
            
def add(a,b):
    print (a+b)
add(1,2)
protected_add=login_required(add) #.............(1)
protected_add('dhruv','123@om',1,2)
protected_add('dhruv','123@om21',1,2)            
add=login_required(add) #............(2)

#Both (1) and (2) will do the same thing!

@login_required  #.............(3)  This is called DICTATORS
def mul(a,b):
    print(a*b);
    
#(3) and (2) are EXACTLY SAME!!!    
    
mul('dhruv','123@om',9,8)