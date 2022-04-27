# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 20:48:54 2021

@author: marym
"""
#tuples in python ......................................TUPLES RUELS
mytuples1=("mariam",)
mytuples2=("mariam")
print(type(mytuples1))#<class 'tuple'>
print(type(mytuples2))#<class 'str'>
mytablee=(5,6,7,8)
print(mytablee[0]) #5
print(mytablee[-1])#8
print(mytablee[-3])#6
#tuples conection 
a=(1,2,3,4)
b=(5,6)
c=b+a
print(c)#output(5, 6, 1, 2, 3, 4)
d=a+("a" ,"b","c",'true')+b
print(d)
#tuples , list , string**
mystring="  string    "
mylist=[1,2]
mytuples=("a","b")
print(mystring*6)
print(mylist*6)
print(mytuples*6)
#meyhod count
a=(1,2,4,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8)
print(a.count(8))#15
b=(1,2,3,4,5,6,7)
print(b.index(2))
#format ....
print( "the position of index is : {:d}".format(b.index(7)) )
print( f"the position of index is : {b.index(7)}")
#tuple destruct
s=("A","B",4 ,"c")
x,y,_,z=s
print(x)
print(y)
print(z)










