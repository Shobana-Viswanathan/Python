#Example: Number datatype
num1 = 10
print(type(num1))
num2 = -1127
print(type(num2))
var1 = True
print(type(var1))
#boolean literal
x=(1==True)
print(x)
y=(1==False)
print(y)
a=True+4
print(a)
b=False+10
print(b)
#example of identity operator
num1=5
print(type(num1) is int)
num2=num1
id(num1)
id(num2)
print(num1 is not num2 )
#example of membership operator
a=[1,2,3]
print(2 in a)
print('1' in a)
print(10 not in a)
print(1 not in a) 
#Explicit type conversion
num1 = 10 
num2 = 20
num3 = num1+num2
print(type(num3))
num4=float(num1+num2)
print(type(num4))
#input function
name=input("your name: ")
age=input("your age: ")
print(type(age))
print("hello world")
#print multiple values
x=5
y=10
print("the value of x: ",x,"and y value",y)
#formatting with f-strings 
name="Shobana"
age=21
print("My name is {name} and I am {age} years old")
#using the sep and end parameters
print("apple","orange","banana", sep="*" ,end=".\n")
