class food :
    def __init__(self , name , price):
        self.n=name
        self.p=price
        print(self.n ,self.p)
        
    def eat(self)    :
        print(" in base class")
        
class apple (food):
    def __init__(self , name , price) :
    
        food.__init__(self, name , price)
        #print (self.n ,self.p)

obj1=food("banana",5)
obj2=apple("mango",7)        
obj2.eat()
x = 'abcd'
for i in range(len(x)):
 x[i].upper()
print (x)
string = "my name is x"
for i in string:
 print (i, end=", ")
a = [0, 1, 2, 3]
for a[-1] in a:
 print(a[-1])
 #-What will be the output of the following Python code?
print('abcdefcdghcd'.split('cd', 0))
def f (x,y,z):
    return x+y+z
print(f(2 ,30 , 400))