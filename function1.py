# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 23:16:08 2020

@author: DHRUV
"""


def sheldon_knocks_for(name,no_of_times=3): #2nd argument is default argument
    for i in range(0,no_of_times):
        print("Sheldon knocks for {}".format(name));
        
def div(a,b):
    try:     #if this is successful, except is ignored 
        print(a/b);
    except: #if try fails, the code under except is executed
        print("Error!")
    finally:              #no matter what happens in try/except, finally always runs
        print("Div function ends here...")

x=10    
def local_global(): 
    global x #without this it gives error
    x+=1
    print("I am in local_global",x);
#read about non-local and function inner function!
        
sheldon_knocks_for('Penny')
print("\n\n")
sheldon_knocks_for('Dhruv',4)

print("\n\n")
div(5,2)
print("\n\n")
div(5,0)

local_global()