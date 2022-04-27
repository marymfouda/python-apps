#tasks in section four python # true true true true true 
# task one 
name1=(input(" person1 enter your name :"))
name2=(input(" person2 enter your name :"))
age1=int(input(" person1 enter your age :"))
age2=int(input(" person2 enter your age \n :"))
if age1>age2:
    print (" person 1 is older.  ")
elif age1==age2 : 
    print (" two person is the same age ")
else :
    print ("person 2 is older.  ")
# task three
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for x in a :
    if x<5:
        print (x)
# task two
num = int(input("enter a number to check: "))
check = int(input("enter a number to divide by: "))

if num % 4 == 0:
    print(num, "is a multiple of 4")
elif num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "does not divide evenly by", check)  
#task four 
      
num = int(input("Please choose a number to divide: "))

listRange = list(range(1,num+1))

divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)