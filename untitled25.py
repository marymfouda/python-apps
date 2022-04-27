class employee:
    'common base class for all employee'
    empcount=0
    def __init__( self,name,salary):
        self.name= name
        self.salary= salary
        employee.empcount+=1

    def displaycount(self):
       print ("total employee %d" % employee.empcount)
       
    def displayemployee(self):
        print("name : " ,
              self.name ,"salary :" , self.salary )
        
        
emp1 = employee("zara",2000)     
emp2 = employee("mani ", 5000)  
emp1.display_count()
 



print("employee._doc_:" + employee._doc_)
print("employee.__name__ :" + employee.__name__)
print("employee._moudle_:" + employee._modle_)
print("employee.__bases__:" +employee.__bases__)
print("employee.__dict__:" +employee.__dict__)

 


 



              
    