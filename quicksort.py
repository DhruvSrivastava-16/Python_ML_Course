# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 15:45:38 2020

@author: DHRUV
"""

def partition(a,l,h):
    i=l-1
    p=a[h]
    for j in range(l,h):
        if(a[j]<=p):
            i+=1;
            a[i],a[j]=a[j],a[i]
    a[i+1],a[h]=a[h],a[i+1]
    return i+1
        
def quicksort(a,l,h):
    if l<h:
        pi=partition(a,l,h)
        quicksort(a,l,pi-1)
        quicksort(a,pi+1,h)
        
if __name__=="__main__":
    a=[1,5,2,9,3,5,9]
    quicksort(a,0,len(a)-1)
    print("ans: ",a)