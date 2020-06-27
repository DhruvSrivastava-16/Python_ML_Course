# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 20:19:39 2020

@author: DHRUV
"""


class Complex: 
    def __init__(self,r,i):
        self.real=r
        self.imag=i
        
    def complex(self):
        print(str(self.real)+'+'+str(self.imag)+'j')
        
    def __add__(self,n):
        print(str(self.real+n.real)+'+'+str(self.imag+n.imag)+'j')

        
a=Complex(2,3)
a.complex()
b=Complex(4,9)
b.complex()
a+b