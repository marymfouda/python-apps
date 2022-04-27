"""
Created on Sat Nov 20 20:38:10 2021
@author: marym
"""  # trueeeeeeeeeeeeeeeeeeeeeee
# random num in python 
import  random
x=random.randrange(1,10)
print(x)
x=9
y=8
#arthimatic operator
h=x+y
j=x*y
p=x%y
o=x/y
u=x**y
f=x//y
print(h,j,p,o,u,f)
#condition
x=4
y=2
if x>y:
    x+=1
    result=("x has a new value :{}") #important to put it for int num 
    print(result.format(x)) # important 
#if condition
o=7
t=9
if o>t:
    print("o is greather than t")
#else if ==>elif
v=7
c=9
if v > c:  
    print ("v is greather than c")
elif v==c:
    print (" two num is equal")    
else:
    print("c is greather than v")    
#simple statment
w=7
r=8
print("T") if w>r else print ("f")    