# -*- coding: utf-8 -*-  # true true true true true 
"""
Created on Sat Oct 30 00:08:32 2021

@author: marym
"""
#if statement & while & for loop
x=int(input("enter the numx :"))
y=int(input("enter the numy :"))
if x > y :
    print (" x is greather ")
else:
    print (" y is greather ")
# while loop 
i=0
while i < 6 :
    i+=1
    if i==3:
        break
    print(i)
# second code in section 
i=0
while i < 6 :
    i+=1
    if i==4:
        continue
    print(i)
 #third code
i=1
while i < 8:
    print (i)
    i+=1
else :
    print (" the loop became false ")
# 4 code in section 
age =[ 19 , 14 ,20 ]   
name =[ "mariam " , " sara " , " hager "] 
for x in age :
    for y in name :
        print (x , y )
 #for code  
for x in range (6) :
    print ( x )
    
 