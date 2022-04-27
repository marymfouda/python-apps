#task in python list
a=[]
n=int(input("enter number of element in list : "))
for i in range(0,n):
    print("enter element num{}".format(i+1))
    elements=int(input())
    a.append(elements)
print("your list is : ",a)
print("your  lenght list is : ",len(a))
s=0
for i in a:
    s=s+1
print("the summation of list element is :",s)    
print("the sorted list is :")
a.sort()
print(a)
print("the reverse list is :")
a.reverse()
print(a)
    
    