def safe_division(a, b):
    c=a/b
    print(float(c))
try:
    a=int(input("Enter a:"))
    b=int(input("Enter b: "))
    safe_division(a,b)
except ZeroDivisionError:
    print("Error: Division by zero!")