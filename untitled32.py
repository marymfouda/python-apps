# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 21:24:34 2021

@author: marym
"""

x = "a"
x *= 3
print(x)
spam = "7"
spam = spam + "0"
eggs = int(spam) + 3
print(float(eggs))
age = int(input())
print(age+8)
x = 5
y = x + 3
y = int(str(y) + "2")
print(y)
x = 3
num = 17
print(num % x)
print("hey" < "hay")
num = 7
if num > 3:
   print("3")
   if num < 5:
      print("5")
      if num ==7:
         print("7")
x = 'a'
if(x < 'c'):
    x += 'b'
if(x > 'z'):
    x += 'c'
    
print(x)         