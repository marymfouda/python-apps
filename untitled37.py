# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 22:17:44 2021

@author: marym
"""
class member :
    def __init__(self ,first_n , mid_n , last_n ,gender2):

        self.fname=first_n
        self.mname=mid_n
        self.lname=last_n
        self.gender=gender2
    def  full_name(self)  :
        return f"{self.fname} {self.mname} {self.lname} "  
    def name_with_title(self) :
        if self.gender == "male" :
            return f"hello mr {self.fname}"
        elif self.gender == "female" :
            return f"hello miss{self.fname}"   
        else:
            return f"hello {self.fname}" 


member1=member('mai' , 'mohamed','ali','male')   
member2=member('osama','ahmed','ali','male')    
member3=member('marym','magdy','fouda','female') 

print(member1.gender)
print(member2.full_name())
print(member3.fname)
x=10
print(type(str(x)))
d={'m':8 ,'v':5}
print('m' in d)
x=1
y='1'
print(x+y)