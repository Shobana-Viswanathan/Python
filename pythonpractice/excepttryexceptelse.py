try:
   a=int(input())
   b=int(input())
   c = a/ b
   print("a/b",c)
except:
   print("Can't divide with zero")
else:
   print("I will execute when no exception occurs")
print("Sucessfully handled")
