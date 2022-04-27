"""            # trueeeeee
Created on Sat Nov 20 19:33:06 2021
@author: marym
"""
if 5 > 4:
    print("5 is biggest") #5 is biggest
#python casting
x=str('o')  # 'o'
y=int(3) #3
z=float(3) #3.0
print(x,y,z)
#type
t="mariam" 
p='n'
l=7
f=8.9
n=("mm","kk","nn")
b=["m","n",9,8.9]
j=(8)
gg=3+5j
print(type(t))#<class 'str'>
print(type(p))#<class 'str'>
print(type(l))#<class 'int'>
print(type(f))#<class 'float'>
print(type(n))#<class 'tuple'>
print(type(b))#<class 'list'>
print(type(j))#int
print(type(gg))
print(gg)
#variable in function
x="mariam"
def myfunc():
    print("name is :"+x)
myfunc()    
#input from user
x=input(" enter your name : ")
print(x)
y=int(input("enter your age:"))
print(y)
ii=int(input("enter your mopile num:"))
print(ii)
#operathion in python
print ("operation num1*num2+num3 = ") 
g=int(input("enter num 1 : "))
u=int(input('enter num2 : '))
i=int(input("enter num 3 : "))
z=g*u+i

print(z)
