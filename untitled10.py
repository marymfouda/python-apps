# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 14:55:57 2021

@author: marym
"""
#convert a list to a tuple
l=[3,9,8,12]
a=tuple(l)
print(a)
#check an element
t=(1,3,8,9)
print ('a' in t)
print(t.index(3))
#rrr
t=(1,6,8,9,8,7,5)
print(t[3],t[-4])
#tuple in list
x=[(1,2,3),(4,5,6),(7,8,9)]
print([t[:2]+(50,) for t in x])
#differance
x={"mariam","hager","sara"}
y={"orange", "yellow","mariam"}
print(x.difference(y))
print(x.symmetric_difference(y))
print(y.symmetric_difference(x))
print(y.difference(x))