class member:
    def __init__(self , f1 , f2 ,f3):
        self.fname=f1
        self.lname=f2
        self.mname=f3
    def myfun (self ,x,y):
        print ("my name is  " + self.fname +"  "+ self.lname )
        return x*y
obj=member('maryam','ali','ahmed')
print(obj.myfun(6,7))     
m1=member('mai' , 'ali','ahmed')  
m2=member("mai" , 'mona', ' ola')
print(m1.fname , m1.lname , m1.mname)
print(m2.fname , m2.lname , m2.mname)
print(obj.fname)