# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 14:08:26 2021

@author: marym
"""

x = [2, 4, 5, 7, 4]
y = x.index(4)
print(y)
list = [8, 4, 2, 6]
list.remove(2)
print(len(list)+list.count(6))
nums = [2,4,8,9,5]

nums.insert(1, 3)
nums.remove(9)
nums.insert(0, nums.count(8))
print(nums[3])
print("{0}{1}{0}".format("abra", "cad"))
def msg(num, ch):
  print(ch+str(num))

msg(18, 'A')
def print_numbers():
  print(1)
  print(2)
  return
  print(4)
  print(6)
def sum(x):
    res = 0
    for i in range(x):
        res+=i
    return res
    
print(sum(4))
def print_nums(x):
  for i in range(x):
    print(i)
    return
print_nums(10)
def func(x):
  res = 0
  for i in range(x):
     res += i
  return res

print(func(3))  