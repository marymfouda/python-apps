# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 17:42:20 2021

@author: marym
"""
#function in python
def function_name():
    return " hello python from inside function "
x=function_name()
print (x)
#function 
def function_name():
      print(" hello python from inside function ")
function_name()  
#function
def addition(n1,n2):
    print(n1+n2)    
addition(488,2)
#function 
def say_hello(name):
    print( f"hello {name}")
say_hello("mariam")    
#function multiplay
def multiply(n1,n2):
    print(n1*n2)
multiply(4,5) 
#function name
def full_name(first,middle,last):
    print (f"hello {first.strip().capitalize()} {middle.strip()} {last.capitalize()}")
full_name("mariam", "magdy", "fouda")    
#lambda function
#def say_hello(name):
hello = lambda name:f"hello{name}"
print(hello (" nany"))
#function
def my_function(*child):
    for n in child:
        print(n)
my_function("many","nany","mody","sasa")

    