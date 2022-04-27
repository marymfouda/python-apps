# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 00:56:12 2021

@author: marym
""" 
#print len of string
name="mariam"
print(len(name))
# program to count the num of char 
xx="google.com"
dict = { }
for x in xx :
    if x in dict:
        dict[x] +=1
    else:
        dict[x]=1
print(dict) #no space here
# print first or last char
y="mariam"
if len(y)<2:
    print("empty")
else :
    print (y [:2] + y [-2:])
    
#if character repeted remove and get $
y="mariam"
h= y.replace (y[0] ,'$')
print ( y[0] + h[1:])

        
