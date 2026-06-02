def multiply(a, b):
     if type(a)!=int or type(b)!= int:
        raise TypeError
     c=a*b
     print(c)
try:
    a=eval(input("Enter a: "))
    b=eval(input("Enter b: "))
    multiply(a,b)
except TypeError:
    print("Error: Invalid operand type!")
