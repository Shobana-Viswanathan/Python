n=int(input("Enter the value of n: "))
i=1
sum=0
while i <= n:
    num = int(input("Enter the user inputs: "))
    if num == 1:
        break
    else:
        sum=sum+num
        i=i+1
print("The sum of user input is: ",sum)
