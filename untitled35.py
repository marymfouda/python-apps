# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 21:24:30 2021

@author: marym
"""

nums = [5, 4, 3, 2, 1]
print(nums[2])
things = ["text", 0, [1, 2, 8], 4.56]
print(things[2][2])
x = "Python"
print(x[1] + x[4])
x = [2, 4]
x += [6, 8]
print(x[2]//x[0])
x = [2, 4]
x = x * 3
print(x[3])
nums = [10, 9, 8, 7, 6, 5]
nums[0] = nums[1] - 5
if 4 in nums:
  print(nums[3])
else:
  print(nums[4])
print("="*40)  
list = [2, 3, 4, 5, 6, 7]

for x in list:
   if(x%2==1 and x>4):
      print(x)
      break
nums = [1, 2, 3, 4]
res = 0

for x in nums:
    if(x%2==0):
        continue
    else:
        res += x
        
print(res)
print(range(20) == range(0, 20))
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[1::4])  
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[7:5:-1])
nums = [1, 2, 3, 4, 5, 6]
res = nums[::-1]
print(res[2])
list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]])
x = [6, 4, 2, 9]
x = x[::-1]
print(x[0]+x[2])
N=100
sum=0

for i in range(1, N+1):
	sum+=i
	
print(sum) 