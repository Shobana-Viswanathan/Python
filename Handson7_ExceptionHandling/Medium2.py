class InputError(Exception):
    pass

class ZeroError(Exception):
    pass

class MultiplyError(Exception):
    pass

try:
    op=input("Enter operation: ")

    a=int(input("Enter a: "))
    b=int(input("Enter b: "))

    if op=="+":
        print(a+b)

    elif op=="-":
        print(a-b)

    elif op=="/":
        if b==0:
            raise ZeroError
        print(a/b)

    elif op=="*":
        if a==0 or a==1 or b==0 or b==1:
            raise MultiplyError
        print(a*b)

except ValueError:
    print("Error: Input is not a number")

except ZeroError:
    print("Error: Division by zero")

except MultiplyError:
    print("Error: Invalid multiplier")

