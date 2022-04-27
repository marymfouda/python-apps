"""
Created on Mon Nov 22 15:51:02 2021

@author: marym
"""
#print dic in result
dic={}
for x in range(1,16):
   dic[x]=x**2
print(dic)
# add number in dic 
thisdic={0:10
         ,1:20}
thisdic.update({2:30})
print(thisdic)
#min ,max
dic4={0: 10, 1: 20, 2: 30}
print(max(dic4.values()))
print(min(dic4.values()))  
      
      
      
          