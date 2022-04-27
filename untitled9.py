# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 21:35:04 2021

@author: marym
"""
##task1 section 5..Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3,
# leave it unchanged. 
def add_string(str1):
  length = len(str1)

  if length > 2:
    if str1[-3:] == 'ing':
      str1 += 'ly'
    else:
      str1 += 'ing'
  return str1
print(add_string('ab'))
print(add_string('abc'))
print(add_string('string'))
print("--" * 60)
####### task2 section 5
 # Write a Python program to remove the nth index character from a nonempty string
def remove_char(str, n):
      first_part = str[:n] 
      last_part = str[n+1:]
      return first_part + last_part
print(remove_char('Python', 1))
print(remove_char('Python', 3))
print(remove_char('Python', 4))

    
    
    