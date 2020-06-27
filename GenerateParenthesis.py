# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 18:56:24 2020

@author: DHRUV
"""

class Solution:
    def __init__(self,n):
        self.n=n
        self.l=n;
        self.r=n;
    
    def solution1(self):
        result=[]
        self.solutionutil(self.l,self.r,"",result)
        print("answer is: ",result)
        
    def solutionutil(self,l,r,temp,result):
    
        if l==0 and r==0:
            result.append(temp)
            return  
        
        if l>0:
            self.solutionutil(l-1,r,temp+'(',result)
            
        if r>l:
            self.solutionutil(l,r-1,temp+')',result)
                
        
        

n=int(input("Enter no. of balanced () you want: "))
a=Solution(n)
a.solution1()