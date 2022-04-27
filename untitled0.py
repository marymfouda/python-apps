# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 20:06:16 2021

@author: marym
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 19:09:49 2021

@author: marym
"""
# know if number odd or even ( task 1)
num=int (input(" enter your num :"))

if num%2==0 :
    print (" even ")
else :
    print (" odd  ")
# ask user to 2 num and make 4 oper 
x=int (input  (" enter x : "))
y=int (input  (" enter y : "))
z = x+y 
h = x-y 
j = x*y 
d = x/y
print (z)
print (h)
print (j)
print (d)
# comper which num is greather between 2 num 
num1=int (input (" enter num1 :"))
num2=int (input (" enter num2 :"))
 
if num1>num2 :
    print (" number 1 is greather : ")
else :
     print (" number 2 is greather : ")   
# 2 variable and get left or right shift
x = 5
y = 4 
print ( x>>y)
print ( x<<y)
      