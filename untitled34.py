# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 20:49:17 2021

@author: marym
"""

i = 5
while True:
  print(i)
  i = i - 1
  if i <= 2:
    break
print("=="*40)
i=0
while True:
    i+=1
    if(i == 2):
        continue
    if(i == 5):
        break
    
    print(i)
print("=="*40)   
while False:
  print("Looping...")
i = 0
x = 0
while i < 4:
    x+=i
    i+=1

print(x)

weight = int(input());
height = float(input());
x = weight/float(height*height);
if x < 18.5:
    print('Underweight')
if x>=18.5 and x<25:
    print("Normal")
if x >= 25 and x < 30:
   print('Overweight')
if x >= 30:
   print('Obesity')
   