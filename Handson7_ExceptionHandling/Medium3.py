class ZeroError(Exception):
    pass
#valueerror- invalid integer
try:
    qty=int(input("Enter quantity of books: "))
    print("Quantity:",qty)
except ValueError:
    print("Error: Input should be a valid integer")

#format change -valueerror
try:
    price=float(input("Enter price of the book: "))
    print("Price:",price)
except ValueError:
    print("Error: Invalid price format")

#index out of bound
try:
    l=list(map(int,input("Enter list elements: ").split()))
    index=int(input("Enter index: "))
    print(l[index])
except IndexError:
    print("Error: Index out of bounds")

#division by zero error 
try:
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    if b==0:
        raise ZeroError
    print(a/b)
except ZeroError:
    print("Error: Division by zero")
