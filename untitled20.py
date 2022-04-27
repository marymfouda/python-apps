# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 16:15:49 2021

@author: marym
"""
dic1={1:7}
dic2={5:6}
dic3={9:8}

dic4={}
for x in dic1,dic2,dic3:
    dic4.update(x)
print(dic4)
#check is already

x=int(input("enter the num that you want to check :"))
dic5={7:8,
      8:5,
      3:6}
if x in dic5.keys():
       print("exsit" )
else:
       print(" not exsit" )
        