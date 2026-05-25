n=int(input())
fact=1


if(n>0):
    for i in range(1,n+1):
        fact = fact * i
else:
    print("1")
print(fact)
     
