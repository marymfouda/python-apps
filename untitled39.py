import untitled40
obj=untitled40.module1('module1',2)
print(obj.sum(1,10))



class person:
    def __init__(self , name , age , level):
        self.name=name
        self.age=age
        self.level=level
    def myfunc (self,x,y)  :
        print("my name is ",self.name)
        return x*y
obj1=person(name='mariam',age='6',level='2')
obj2=person('mariam',5,8)
pv=person('mary',8,8)
print(pv.myfunc(6,7))
print(obj1.name , obj1.age ,obj1.level)
print(obj2.name)