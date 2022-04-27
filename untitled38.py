x="marym"
print (x)
x=3
print(x)
#python is my life 
x = str(3) # x will be '3’
y = int(3) # y will be 3
z = float(3)
print(x,y,z)
u=3
U='3'
r=(5)  #int
o=(5,) #tuple
print(type(u)) # int
print(type(U)) #str
print(type(r)) 
print(type(o))
x=9
y=1
print(x+y)
#python list 
mylist=['app','banan','cherry','kiwi','zara']
print(mylist[:3])  #['app', 'banan', 'cherry']
print(mylist[1])   # banan
print(mylist[-1])  # zara
print(mylist[1:3]) # ['banan', 'cherry']
print(mylist[:-1]) # ['app', 'banan', 'cherry', 'kiwi']
print(mylist[-1:]) # ['zara']
print(mylist[:-2])
print(mylist[-2:])
print(len(mylist)) #5
mylist[3]='bbaass'
print(mylist) #['app', 'banan', 'cherry', 'bbaass', 'zara']
list1=['m','z','a','hh']
list2=[9,8,7,6,5,4]
list3=[True , False , 6 , 'mmju']
print(list1) #['m', 'z', 'a', 'hh']
print(list2) #[9, 8, 7, 6, 5, 4]
print(list3) #[True, False, 6, 'mmju']
mylist7 = ["apple", "banana", "cherry"]
print(type(mylist))
mylist7.append('orange') #adding at the end of the list
print(mylist7) #['apple', 'banana', 'cherry', 'orange']
list11 = list('hello')
print(list11)
list12=[2445,133,12454,123]
print(max(list12))
# if condation in python
a=8
b=9
if a>b:
    print(a)
else:
    print(b)
# while loop 
i=0
while i < 6 :
    i+=1
    if i==3:
        break
    print(i)
# second code in section 
i=0
while i < 6 :
    i+=1
    if i==4:
        continue
    print(i)
#for loop
fmylist=['orange','red','bink','yellow'] 
for x in fmylist:
    print(x)
for y in 'banana'  :
    print (y)
# break in for loop    
fruits = ["apple", "banana", "cherry"]
for x in fruits:
 if x == "banana":
  break
print(x)    
#continue in for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
   continue
print(x)    
#in range in for loop 
for x in range(6):
    print (x)
else:
    print('finally finished!!')
for x in range(3,9,2)  :
    print(x)
for x in range (2,8) :
    print (x)
#a nested 
list2=['lk','iu','jj','ff']
list4=['k','i','j','f']
for x in list2:
    for y in list4:
        print(x,y)
# a function in python 
def my_function():
    print("my function is a block of code")
my_function()   
def myfunction(fname):
    print('hello'+"  "+fname)
myfunction("marym")
myfunction("sara")  
myfunction("hager")
def myfunction1(fname , lname):
    print(fname +" "+lname)
myfunction1('mariam' ,' fouda')   
#if the number of arr is unknown
def myfunction6(*kids):
    print("the youngest child"+" "+kids[2])
myfunction6('adam','mostafa','mohamed','ali')
#the index here not important    
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)
my_function(child1 = "ali", child2 = "anas", child3 = "soha")
def my_function(country = "Egypt"):
    print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
def my_function(x):
   return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))
x= lambda a : a + 10
print(x(4))
x= lambda a,b : a*b
print(x(2,3))
x= lambda a,b,c : a+b+c
print(x(1,2,3))
class Person:
 def __init__(self, name, age):
  self.name = name
  self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)
class animals:
    def __init__(self ,kind , color):
        self.kind=kind
        self.color=color
p1=animals('cat','white') 
print(p1.kind)
print(p1.color)      

