str=input("Enter a string:")
revn=str[::-1]
if str == revn :
   print("Yes Palindrome")
else:
   print("Not a palindrome")
#str __eq__(rev)
print(str.__eq__(revn))
   
