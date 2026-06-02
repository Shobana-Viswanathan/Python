def get_positive_integer(a):
    if a>0:
        print(a)
try:
    a=int(input("Enter a:"))
    get_positive_integer(a)
    
except ValueError:
    print("Error: Invalid input! Please enter a positive integer.")
