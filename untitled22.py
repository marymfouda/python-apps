# sum of dic value
"""
Created on Mon Dec 13 06:36:24 2021
@author: marym
"""
mydic = {'num1':10,'num2':20,'num3':25}
print(sum(mydic.values()))
print(max(mydic.values()))
print(min(mydic.values()))

#dic value in form x:x*x

n=int(input("Input a number "))
d = dict()

for x in range(1,n+1):
    d[x]=x*x

print(d)
