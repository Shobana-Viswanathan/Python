n=int(input())
if n<0:
    print("Invalid Age")
elif n <= 10 :
    print("Cartoon Club")
elif n>=10 and n<=20:
    print("Teens Club")
else:
    print("Not Allowed")