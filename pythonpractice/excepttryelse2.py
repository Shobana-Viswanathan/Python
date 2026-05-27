try:
   a=int(input())
   b=int(input())
   c = a/ b
except NameError:
   print("This value is error")
except Exception:
   print("Can't divide by zero")
   print(Exception)
else:
   print("I wil excetue when no exception occurs")
print("Sucessfully handled")
